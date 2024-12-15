import unittest
from src.core.ActionCatalog import ActionCatalog

class TestActionCatalog(unittest.TestCase):

    def test_from_transcript_to_action_empty(self):
        result = ActionCatalog.from_transcript_to_action("")
        self.assertEqual(result, "")

    def test_from_transcript_to_action_single_word(self):
        result = ActionCatalog.from_transcript_to_action("kubectl")
        self.assertEqual(result, "kubectl")
        
        result = ActionCatalog.from_transcript_to_action("cubectl")
        self.assertEqual(result, "kubectl")
        
        result = ActionCatalog.from_transcript_to_action("bots")
        self.assertEqual(result, "pods")
        
        result = ActionCatalog.from_transcript_to_action("unknown")
        self.assertEqual(result, "unknown")

    def test_from_transcript_to_action_multiple_words(self):
        result = ActionCatalog.from_transcript_to_action("kubectl apply bots")
        self.assertEqual(result, "kubectl apply pods")
        
        result = ActionCatalog.from_transcript_to_action("cubectl get pods")
        self.assertEqual(result, "kubectl get pods")
        
        result = ActionCatalog.from_transcript_to_action("unknown command")
        self.assertEqual(result, "unknown command")

    def test_from_transcript_to_action_case_insensitivity(self):
        result = ActionCatalog.from_transcript_to_action("KUBECTL")
        self.assertEqual(result, "kubectl")
        
        result = ActionCatalog.from_transcript_to_action("BoTs")
        self.assertEqual(result, "pods")

    def test_from_transcript_to_action_strip_and_replace_spaces(self):
        result = ActionCatalog.from_transcript_to_action("  kubectl  apply  ")
        self.assertEqual(result, "kubectl apply")

if __name__ == '__main__':
    unittest.main()
