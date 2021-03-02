...
"proxmox": {
            "proxmox": {
                "username": String(""),
                "password": String("", sanitize=True),
                "host": String(""),
                "nodename": String(""),
                "machines": List(String, ""),
            },
            "*": {
                "__section__": "",
                "label": String(""),
                "platform": String(""),
                "ip": String(""),
                "snapshot": String(),
                "interface": String(),
                "resultserver_ip": String(),
                "resultserver_port": Int(),
                "tags": String(),
                "options": List(String, None, ",\\s"),
                "osprofile": String(required=False),
            },
            "__star__": ("proxmox", "machines"),
        },
...