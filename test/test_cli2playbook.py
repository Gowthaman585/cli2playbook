import unittest
from cli2playbook.parser import parse_lists_only

class TestParserLists(unittest.TestCase):
    
    def test_parse_ports_list(self):
        # Simulate command line arguments
        args = ["-p", "80:80", "-p", "443:443"]
        
        # Call your function
        result = parse_lists_only(args)
        
        # Verify the lists box captured the ports correctly
        expected_output = {
            "lists": {
                "ports": ["80:80", "443:443"]
            }
        }
        
        self.assertEqual(result, expected_output)

if __name__ == "__main__":
    unittest.main()
