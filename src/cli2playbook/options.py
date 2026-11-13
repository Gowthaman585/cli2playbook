from enum import Enum, auto

class OptType(Enum):
    FLAG = auto()
    VALUE = auto()
    LIST = auto()
    MAP = auto()

# Option rules mapping CLI flags to internal storage keys and types
OPTION_RULES = [
    # 1. LIST Options
    { "flags": ["-p", "--publish"],     "type": OptType.LIST,  "key": "ports" },
    { "flags": ["-v", "--volume"],      "type": OptType.LIST,  "key": "volumes" },
    { "flags": ["--device"],            "type": OptType.LIST,  "key": "devices" },
    { "flags": ["--cap-add"],           "type": OptType.LIST,  "key": "cap_adds" },
    { "flags": ["--cap-drop"],          "type": OptType.LIST,  "key": "cap_drops" },
    { "flags": ["--dns"],               "type": OptType.LIST,  "key": "dns_servers" },
    { "flags": ["--ulimit"],            "type": OptType.LIST,  "key": "ulimits" },
    { "flags": ["--security-opt"],      "type": OptType.LIST,  "key": "security_opts" },
    { "flags": ["--tmpfs"],             "type": OptType.LIST,  "key": "tmpfs_mounts" },

    # 2. VALUE Options
    { "flags": ["--name"],              "type": OptType.VALUE, "key": "container_name" },
    { "flags": ["--memory"],            "type": OptType.VALUE, "key": "memory_limit" },
    { "flags": ["--cpus"],              "type": OptType.VALUE, "key": "cpus_limit" },
    { "flags": ["--shm-size"],          "type": OptType.VALUE, "key": "shm_size" },
    { "flags": ["--mac-address"],       "type": OptType.VALUE, "key": "mac_address" },
    { "flags": ["--ip"],                "type": OptType.VALUE, "key": "ip_address" },
    { "flags": ["--log-driver"],        "type": OptType.VALUE, "key": "log_driver" },
    { "flags": ["--network", "--net"],  "type": OptType.VALUE, "key": "network_mode" },
    { "flags": ["--restart"],           "type": OptType.VALUE, "key": "restart_policy" },
    { "flags": ["--workdir", "-w"],     "type": OptType.VALUE, "key": "workdir" },
    { "flags": ["--hostname"],          "type": OptType.VALUE, "key": "host_name" },
    { "flags": ["--user", "-u"],        "type": OptType.VALUE, "key": "user" },

    # 3. FLAG Options
    { "flags": ["--detach", "-d"],      "type": OptType.FLAG,  "key": "detach_mode" },
    { "flags": ["--read-only"],         "type": OptType.FLAG,  "key": "read_only_mode" },
    { "flags": ["--init"],              "type": OptType.FLAG,  "key": "init_mode" },
    { "flags": ["--privileged"],        "type": OptType.FLAG,  "key": "priv_mode" },
    { "flags": ["--rm"],                "type": OptType.FLAG,  "key": "auto_remove" },

    # 4. MAP Options
    { "flags": ["-e", "--env"],         "type": OptType.MAP,   "key": "envs", "sep": "=" },
    { "flags": ["-l", "--label"],       "type": OptType.MAP,   "key": "labels", "sep": "=" },
    { "flags": ["--add-host"],          "type": OptType.MAP,   "key": "extra_hosts", "sep": ":" },
    { "flags": ["--sysctl"],            "type": OptType.MAP,   "key": "sysctls", "sep": "=" },
    { "flags": ["--log-opt"],           "type": OptType.MAP,   "key": "log_opts", "sep": "=" },
]

