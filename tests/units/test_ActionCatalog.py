import unittest
from src.core.ActionCatalog import ActionCatalog

class TestActionCatalog(unittest.TestCase):

    def test_kubectl_get_pods(self):        
        result = ActionCatalog.from_transcript_to_action("cubectl  get  Bots")
        self.assertEqual("kubectl get pods", result)

    # Test with an empty transcript to ensure it returns an empty string
    def test_empty_transcript(self):
        result = ActionCatalog.from_transcript_to_action("")
        self.assertEqual("", result)

    # Test with a transcript that has no matching words in the catalog
    def test_no_matching_words(self):
        result = ActionCatalog.from_transcript_to_action("hello world")
        self.assertEqual("hello world", result)

    # Test with a transcript that includes a mix of catalog and non-catalog words
    def test_mixed_catalog_and_non_catalog_words(self):
        result = ActionCatalog.from_transcript_to_action("cubectl run hello")
        self.assertEqual("kubectl run hello", result)

    # Test with a transcript that contains multiple spaces between words
    def test_multiple_spaces_between_words(self):
        result = ActionCatalog.from_transcript_to_action("kubectl   get   pods")
        self.assertEqual("kubectl get pods", result)

    # Test with a transcript that is already in the correct format
    def test_already_correct_format(self):
        result = ActionCatalog.from_transcript_to_action("kubectl get pods")
        self.assertEqual("kubectl get pods", result)

if __name__ == '__main__':
    unittest.main()