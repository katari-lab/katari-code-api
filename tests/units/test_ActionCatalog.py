import unittest
from src.core.ActionCatalog import ActionCatalog

class TestActionCatalog(unittest.TestCase):

    def test_kubectl_get_pods(self):        
        result = ActionCatalog.from_transcript_to_action("cubectl  get  Bots")
        self.assertEqual("kubectl get pods", result)

if __name__ == '__main__':
    unittest.main()