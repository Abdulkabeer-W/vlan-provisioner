# Voice-Driven VLAN Provisioner

A lightweight Flask-based API to remotely create, delete, and list VLANs on multiple Ubuntu VMs using SSH and Open vSwitch (OVS). This version includes the core networking logic, without voice integration.

---

## 🚀 Features

* Remotely manage VLANs on multiple VMs
* Uses Paramiko to SSH and execute privileged commands
* Open vSwitch (OVS) used for software-based switching
* Logs all requests and responses to a local `.log` file

---

## 🧱 Stack

* **Flask**: Python web framework
* **Paramiko**: SSH communication with remote Ubuntu machines
* **Open vSwitch**: For VLAN management
* **VirtualBox / GNS3**: For VM and virtual network simulation

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/vlan-provisioner.git
cd vlan-provisioner
```

### 2. Create Virtual Environment

```bash
python -m venv .venv
.venv\Scripts\activate  # On Windows
source .venv/bin/activate  # On Linux/Mac
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Configure VMs

Update the `HOSTS` list in `ovs_vlan_api.py` with your VM IPs and credentials:

```python
HOSTS = [
  {'host': '192.168.56.108', 'username': 'ubuntu', 'password': '2002'},
  {'host': '192.168.56.104', 'username': 'ubuntu', 'password': '2002'}
]
```

### 5. Start the Server

```bash
python ovs_vlan_api.py
```

The Flask server will run on `http://localhost:5000`

---

## 📡 API Endpoints

### Create VLAN

**POST** `/vlan/create`

```json
{
  "id": 30
}
```

### Delete VLAN

**POST** `/vlan/delete`

```json
{
  "id": 30
}
```

### List VLANs

**GET** `/vlan/list`
Response:

```json
{
  "192.168.56.104": ["vlan10", "vlan30"],
  "192.168.56.108": ["vlan10", "vlan30"]
}
```

---

## 📁 Directory Structure

```
vlan-provisioner/
├── ovs_vlan_api.py         # Core Flask app
├── requirements.txt        # Python dependencies
├── .gitignore              # Ignored files
├── README.md               # You're reading it
└── vapi_requests.log       # Auto-generated request logs
```

---

## 🧠 Learning Goals

This project is designed to:

* Build hands-on experience with Open vSwitch (OVS)
* Learn secure SSH automation using Paramiko
* Understand VLAN provisioning through scripting
* Set the stage for voice + AI-driven networking (in the next branch)

---

## 📌 Next Steps

✅ This branch: `main` contains pure Flask + SSH logic
🔜 Next: merge voice/Vapi/n8n integration in `feature/voice-integration`

---

## 📜 License

MIT

---

## 🤝 Contributions

PRs welcome! Drop a GitHub issue or feature request anytime.

---

## 👨‍💻 Maintainer

**@Abdulkabeer-W**
Project: *Voice-Controlled Network Automation*