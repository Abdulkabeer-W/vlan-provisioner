# VLAN Provisioner via Voice Agent

This project lets you speak “Create VLAN 10” and automatically provisions VLANs on two Open vSwitch instances via a REST API.

## Features
- **Create VLAN**: `POST /vlan/create`  
- **Delete VLAN**: `POST /vlan/delete`  
- **List VLANs**: `GET /vlan/list`

## Prerequisites
- Python 3.9+, Flask, Paramiko  
- Two Ubuntu VMs with Open vSwitch (IPs `192.168.100.11` & `192.168.100.12`)  
- Host-only networking configured in VirtualBox

## Setup

1. Clone this repo:  
   ```bash
   git clone https://github.com/YourUsername/vlan-provisioner.git
   cd vlan-provisioner
