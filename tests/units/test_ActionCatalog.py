import unittest
from src.core.ActionCatalog import ActionCatalog

class TestActionCatalog(unittest.TestCase):

    def test_kubectl_get_pods(self):        
        result = ActionCatalog.from_transcript_to_action("cubectl  get  Bots")
        self.assertEqual("kubectl get pods", result)

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

    def test_from_transcript_to_action_mixed_case_and_spaces(self):
        result = ActionCatalog.from_transcript_to_action("  CuBeCtL  aPpLy  bOtS  ")
        self.assertEqual(result, "kubectl apply pods")

    def test_from_transcript_to_action_no_replacements(self):
        result = ActionCatalog.from_transcript_to_action("list all services")
        self.assertEqual(result, "list all services")

    def test_from_transcript_to_action_leading_and_trailing_spaces(self):
        result = ActionCatalog.from_transcript_to_action("  list all services  ")
        self.assertEqual(result, "list all services")

    def test_from_transcript_to_action_extra_spaces_between_words(self):
        result = ActionCatalog.from_transcript_to_action("kubectl  apply  bots")
        self.assertEqual(result, "kubectl apply pods")

    def test_from_transcript_to_action_multiple_replacements(self):
        result = ActionCatalog.from_transcript_to_action("cubectl get bots and pods")
        self.assertEqual(result, "kubectl get pods and pods")

    def test_from_transcript_to_action_only_spaces(self):
        result = ActionCatalog.from_transcript_to_action("    ")
        self.assertEqual(result, "")

    def test_from_transcript_to_action_special_characters(self):
        result = ActionCatalog.from_transcript_to_action("kubectl get @bots!")
        self.assertEqual(result, "kubectl get @bots!")

    def test_from_transcript_to_action_numeric_values(self):
        result = ActionCatalog.from_transcript_to_action("kubectl get 123 bots")
        self.assertEqual(result, "kubectl get 123 pods")

    # Test scenario where the transcript contains mixed known and unknown words
    def test_from_transcript_to_action_mixed_known_and_unknown_words(self):
        result = ActionCatalog.from_transcript_to_action("kubectl unknown bots")
        self.assertEqual(result, "kubectl unknown pods")

    # Test scenario where the transcript contains only unknown words
    def test_from_transcript_to_action_only_unknown_words(self):
        result = ActionCatalog.from_transcript_to_action("unknown unknown unknown")
        self.assertEqual(result, "unknown unknown unknown")

    # Test scenario where the transcript contains repeated known words
    def test_from_transcript_to_action_repeated_known_words(self):
        result = ActionCatalog.from_transcript_to_action("bots bots bots")
        self.assertEqual(result, "pods pods pods")

    # Test scenario with a combination of known, unknown, and special characters
    def test_from_transcript_to_action_combined_known_unknown_special(self):
        result = ActionCatalog.from_transcript_to_action("kubectl unknown @bots!")
        self.assertEqual(result, "kubectl unknown @bots!")

    # Test scenario where the transcript is a single known word with extra spaces
    def test_from_transcript_to_action_single_known_word_with_spaces(self):
        result = ActionCatalog.from_transcript_to_action("  kubectl  ")
        self.assertEqual(result, "kubectl")

    # Test scenario where the transcript contains mixed known words and numeric values
    def test_from_transcript_to_action_known_words_and_numeric_values(self):
        result = ActionCatalog.from_transcript_to_action("kubectl 123 bots")
        self.assertEqual(result, "kubectl 123 pods")

if __name__ == '__main__':
    unittest.main()