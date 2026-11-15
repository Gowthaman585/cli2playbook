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
                    "flags": {},
                    "maps": {}
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
                    "user": "1000:1000"

                    }
                }
        
        self.assertEqual(result, expected_output)

if __name__ == "__main__":
    unittest.main()
