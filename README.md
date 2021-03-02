# proxmox-cuckoo-configurations
collection of config files for the cuckoo proxmox configuration. Credit goes to Scot Nusbaum for his groundwork: https://github.com/snus-b/proxmoxcuckoo

config-snippet.py --> The snippet has to be added to config.py where the virtualizations are defined (e.g. virtualbox)
proxmox.conf --> example configuration. Important for Proxmox is the `machinery = proxmox` part
proxmox.py --> proxmox module for cuckoo.
cuckoo.conf --> Configuratino for your cuckoo instance - vm configurations dependant on your VMs in your proxmox environment. 

