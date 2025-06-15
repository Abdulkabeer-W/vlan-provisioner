from flask import Flask, request, jsonify
import paramiko

app = Flask(__name__)

HOSTS = [
    {'host':'<host-1-ip-address>','username':'<host-1-username>','password':'<host-1-password>'},
    {'host':'<host-2-ip-address>','username':'<host-1-username>','password':'<host-2-password>'}
]

# Function to run remote SSH command with sudo support
def run_ssh_command(h, cmd):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(h['host'], username=h['username'], password=h['password'])

        # Use sudo -S and write password to stdin
        stdin, stdout, stderr = ssh.exec_command(f"sudo -S sh -c \"{cmd}\"")
        stdin.write(h['password'] + "\n")
        stdin.flush()

        output = stdout.read().decode().strip()
        error = stderr.read().decode().strip()

        filtered_error = "\n".join([
            line for line in error.splitlines()
            if not line.strip().startswith("[sudo]")
        ]).strip()

        ssh.close()

        if filtered_error:
            return f"⚠️ {filtered_error}"
        elif output:
            return output
        else:
            return "✅ Command executed successfully"

    except Exception as e:
        return f"❌ Error: {str(e)}"


# Create VLAN
@app.route('/vlan/create', methods=['POST'])
def create_vlan():
    vid = request.json.get('id')
    if not vid:
        return jsonify({"error": "Missing VLAN ID"}), 400

    results = {}
    for h in HOSTS:
        cmd = (
                f"ovs-vsctl add-port br0 vlan{vid} tag={vid} -- set interface vlan{vid} type=internal && "
                f"ip link set br0 up && "
                f"ip link set vlan{vid} up"
        )   

        results[h['host']] = run_ssh_command(h, cmd)
    return jsonify(results)

# Delete VLAN
@app.route('/vlan/delete', methods=['POST'])
def delete_vlan():
    vid = request.json.get('id')
    if not vid:
        return jsonify({"error": "Missing VLAN ID"}), 400

    results = {}
    for h in HOSTS:
        cmd = f"ovs-vsctl del-port br0 vlan{vid}"
        results[h['host']] = run_ssh_command(h, cmd)
    return jsonify(results)

# List VLANs
@app.route('/vlan/list', methods=['GET'])
def list_vlans():
    results = {}
    for h in HOSTS:
        cmd = "ovs-vsctl list-ports br0"
        results[h['host']] = run_ssh_command(h, cmd)
    return jsonify(results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)