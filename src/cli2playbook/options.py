from enum import Enum, auto

class OptType(Enum):
    FLAG = auto()
    VALUE = auto()
    LIST = auto()
    MAP = auto()

# Option rules mapping CLI flags directly to Ansible community.docker.docker_container keys and types
OPTION_RULES = [
    # 1. LIST Options
    { "flags": ["-p", "--publish"],      "type": OptType.LIST,  "key": "published_ports" },
    { "flags": ["-v", "--volume"],       "type": OptType.LIST,  "key": "volumes" },
    { "flags": ["--device"],             "type": OptType.LIST,  "key": "devices" },
    { "flags": ["--cap-add"],            "type": OptType.LIST,  "key": "cap_add" },
    { "flags": ["--cap-drop"],           "type": OptType.LIST,  "key": "cap_drop" },
    { "flags": ["--dns"],                "type": OptType.LIST,  "key": "dns_servers" },
    { "flags": ["--ulimit"],             "type": OptType.LIST,  "key": "ulimits" },
    { "flags": ["--security-opt"],       "type": OptType.LIST,  "key": "security_opts" },
    { "flags": ["--tmpfs"],              "type": OptType.LIST,  "key": "tmpfs" },

    # 2. VALUE Options
    { "flags": ["--name"],               "type": OptType.VALUE, "key": "name" },
    { "flags": ["--memory"],             "type": OptType.VALUE, "key": "memory" },
    { "flags": ["--cpus"],               "type": OptType.VALUE, "key": "cpus" },
    { "flags": ["--shm-size"],           "type": OptType.VALUE, "key": "shm_size" },
    { "flags": ["--mac-address"],        "type": OptType.VALUE, "key": "mac_address" },
    { "flags": ["--ip"],                 "type": OptType.VALUE, "key": "ip_address" },
    { "flags": ["--log-driver"],         "type": OptType.VALUE, "key": "log_driver" },
    { "flags": ["--network", "--net"],   "type": OptType.VALUE, "key": "network_mode" },
    { "flags": ["--restart"],            "type": OptType.VALUE, "key": "restart" },
    { "flags": ["--workdir", "-w"],      "type": OptType.VALUE, "key": "working_dir" },
    { "flags": ["--hostname"],           "type": OptType.VALUE, "key": "hostname" },
    { "flags": ["--user", "-u"],         "type": OptType.VALUE, "key": "user" },

    # 3. FLAG Options
    { "flags": ["--detach", "-d"],       "type": OptType.FLAG,  "key": "detach" },
    { "flags": ["--read-only"],          "type": OptType.FLAG,  "key": "read_only" },
    { "flags": ["--init"],               "type": OptType.FLAG,  "key": "init" },
    { "flags": ["--privileged"],         "type": OptType.FLAG,  "key": "privileged" },
    { "flags": ["--rm"],                 "type": OptType.FLAG,  "key": "auto_remove" },

    # 4. MAP Options
    { "flags": ["-e", "--env"],          "type": OptType.MAP,   "key": "env", "sep": "=" },
    { "flags": ["-l", "--label"],        "type": OptType.MAP,   "key": "labels", "sep": "=" },
    { "flags": ["--add-host"],           "type": OptType.MAP,   "key": "extra_hosts", "sep": ":" },
    { "flags": ["--sysctl"],             "type": OptType.MAP,   "key": "sysctls", "sep": "=" },
    { "flags": ["--log-opt"],            "type": OptType.MAP,   "key": "log_options", "sep": "=" },
]
