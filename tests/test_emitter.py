import unittest
from cli2playbook.emitter import generate_ansible_task

class TestEmitter(unittest.TestCase):
    def test_emit_all_lists(self):
        parsed_data = {
                "lists": {
                    "published_ports": ["80:80", "443:443"],
                    "volumes": ["/data:/app/data"],
                    "devices": ["/dev/sda"],
                    "cap_add": ["NET_ADMIN"],
                    "cap_drop": ["MKNOD"],
                    "dns_servers": ["8.8.8.8"],
                    "ulimits": ["nofile=1024:2048"],
                    "security_opts": ["no-new-privileges"],
                    "tmpfs": ["/run"]
                    },
                    
                "values": {
                    "name": "my-app",
                    "memory": "1g",
                    "cpus": "2",
                    "shm_size": "64m",
                    "mac_address": "92:d0:c6:0a:29:33",
                    "ip_address": "172.17.0.2",
                    "log_driver": "json-file",
                    "network_mode": "bridge",
                    "restart": "always",
                    "working_dir": "/app",
                    "hostname": "node1",
                    "user": "1000:1000"
                    },
                "flags": {
                    "detach": True,
                    "read_only": True,
                    "init": True,
                    "privileged": True,
                    "auto_remove": True
                    },
                "maps": {
                    "env": {
                        "ENV_VAR": "production",
                        "DEBUG": "true"
                        },
                    "extra_hosts": {
                        "myhost": "192.168.1.10"
                        },
                    "labels": {
                        "tier": "backend",
                        "stage": "production"
                        },
                    "sysctls": {
                        "net.core.somaxconn": "1024"
                        },
                    "log_options": {
                        "max-size": "10m"
                        }
                    }
                }
        
        result = generate_ansible_task(parsed_data)
        
        expected_output = {
                "name": "Manage Docker container from CLI input",
                "community.docker.docker_container": {
                    "published_ports": ["80:80", "443:443"],
                    "volumes": ["/data:/app/data"],
                    "devices": ["/dev/sda"],
                    "cap_add": ["NET_ADMIN"],
                    "cap_drop": ["MKNOD"],
                    "dns_servers": ["8.8.8.8"],
                    "ulimits": ["nofile=1024:2048"],
                    "security_opts": ["no-new-privileges"],
                    "tmpfs": ["/run"],

                    # All Values
                    "name": "my-app",
                    "memory": "1g",
                    "cpus": "2",
                    "shm_size": "64m",
                    "mac_address": "92:d0:c6:0a:29:33",
                    "ip_address": "172.17.0.2",
                    "log_driver": "json-file",
                    "network_mode": "bridge",
                    "restart": "always",
                    "working_dir": "/app",
                    "hostname": "node1",
                    "user": "1000:1000",
                        
                    # All Flags
                    "detach": True,
                    "read_only": True,
                    "init": True,
                    "privileged": True,
                    "auto_remove": True,

                    # All Maps
                    "env": {
                        "ENV_VAR": "production",
                        "DEBUG": "true"
                        },
                    "extra_hosts": {
                        "myhost": "192.168.1.10"
                        },
                    "labels": {
                        "tier": "backend",
                        "stage": "production"
                        },
                    "sysctls": {
                        "net.core.somaxconn": "1024"
                        },
                    "log_options": {
                        "max-size": "10m"
                        }
                    }
                }
        
        self.assertEqual(result, expected_output)

if __name__ == "__main__":
    unittest.main()
