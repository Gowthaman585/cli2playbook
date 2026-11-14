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
                    
                    "values": {},
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
                    "tmpfs": ["/run"]
                    }
                }
        
        self.assertEqual(result, expected_output)

if __name__ == "__main__":
    unittest.main()
