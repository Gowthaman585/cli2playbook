import unittest
from cli2playbook.parser import parse_cli_args

class TestParser(unittest.TestCase):
    
    def test_LISTS_VALUES_FLAGS_MAP_container_parsing(self):
        args = [
                # 1. VALUE options
                "--name", "my-app",
                "--memory", "1g",
                "--cpus", "2",
                "--shm-size", "64m",
                "--mac-address", "92:d0:c6:0a:29:33",
                "--ip", "172.17.0.2",
                "--log-driver", "json-file",
                "--net", "bridge",
                "--restart", "always",
                "--workdir", "/app",
                "--hostname", "node1",
                "--user", "1000:1000",
            
                # 2. LIST options
                "-p", "80:80",
                "-p", "443:443",
                "--volume", "/data:/app/data",
                "--device", "/dev/sda",
                "--cap-add", "NET_ADMIN",
                "--cap-drop", "MKNOD",
                "--dns", "8.8.8.8",
                "--ulimit", "nofile=1024:2048",
                "--security-opt", "no-new-privileges",
                "--tmpfs", "/run",

                # 3. FLAG options
                "--detach",
                "--read-only",
                "--init",
                "--privileged",
                "--rm",

                # 4. MAP options
                "-e", "ENV_VAR=production",
                "-e", "DEBUG=true",
                "--add-host", "myhost:192.168.1.10",
                "-l", "tier=backend" ,
                "-l" , "stage=production",
                ]
        
        result = parse_cli_args(args)

        expected_output = {

                "lists": {
                    "ports": ["80:80", "443:443"],
                    "volumes": ["/data:/app/data"],
                    "devices": ["/dev/sda"],
                    "cap_adds": ["NET_ADMIN"],
                    "cap_drops": ["MKNOD"],
                    "dns_servers": ["8.8.8.8"],
                    "ulimits": ["nofile=1024:2048"],
                    "security_opts": ["no-new-privileges"],
                    "tmpfs_mounts": ["/run"]
                    },
                
                "values": {
                    "container_name": "my-app",
                    "memory_limit": "1g",
                    "cpus_limit": "2",
                    "shm_size": "64m",
                    "mac_address": "92:d0:c6:0a:29:33",
                    "ip_address": "172.17.0.2",
                    "log_driver": "json-file",
                    "network_mode": "bridge",
                    "restart_policy": "always",
                    "workdir": "/app",
                    "host_name": "node1",
                    "user": "1000:1000"
                    },

                "flags": {
                    "detach_mode": True,
                    "read_only_mode": True,
                    "init_mode": True,
                    "priv_mode": True,
                    "auto_remove": True
                    },

                "maps": {
                    "envs": {
                        "ENV_VAR": "production",
                        "DEBUG": "true"
                        },
                    "extra_hosts": {
                        "myhost": "192.168.1.10"
                        },
                    "labels": {
                        "tier": "backend",
                        "stage": "production"
                        }
                    }
                }
   
        self.assertEqual(result, expected_output)

if __name__ == "__main__":
    unittest.main()
