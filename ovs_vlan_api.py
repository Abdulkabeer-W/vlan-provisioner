from flask import Flask, request, jsonify
import paramiko

app = Flask(__name__)

HOSTS = [
    {'host':'192.168.100.11','username':'ubuntu','password':'2002'},
    {'host':'192.168.100.12','username':'ubuntu','password':'2002'}
]

def run_ssh_command(h, cmd):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(h['host'], username=h['username'], password=h['password'])
    stdin, stdout, stderr = ssh.exec_command(cmd)
    output = stdout.read().decode() + stderr.read().decode()
    ssh.close()
    return output

@app.route('/vlan/create', methods=['POST'])
def create_vlan():
    vid = request.json.get('id')
    results = {}
    for h in HOSTS:
        cmd = (
            f"sudo ovs-vsctl add-port br0 vlan{vid} tag={vid} && "
            f"sudo ip link set vlan{vid} up"
        )
        results[h['host']] = run_ssh_command(h, cmd)
    return jsonify(results)

@app.route('/vlan/delete', methods=['POST'])
def delete_vlan():
    vid = request.json.get('id')
    results = {}
    for h in HOSTS:
        cmd = f"sudo ovs-vsctl del-port br0 vlan{vid}"
        results[h['host']] = run_ssh_command(h, cmd)
    return jsonify(results)

@app.route('/vlan/list', methods=['GET'])
def list_vlans():
    results = {}
    for h in HOSTS:
        cmd = "sudo ovs-vsctl list-ports br0"
        results[h['host']] = run_ssh_command(h, cmd)
    return jsonify(results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
