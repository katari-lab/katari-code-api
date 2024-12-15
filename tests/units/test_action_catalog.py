import unittest
from src.core.ActionCatalog import ActionCatalog
class TestActionCatalog(unittest.TestCase):

    def test_cubectl_get_bots(self):        
        result = ActionCatalog.from_transcript_to_action("cubectl  get  Bots")
        self.assertEqual("kubectl get pods", result)
