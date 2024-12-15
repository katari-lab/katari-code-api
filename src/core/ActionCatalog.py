import re

class ActionCatalog:
    
    catalog = {
        'kubectl': 'kubectl',
        'cubectl': 'kubectl',
        'bots': 'pods'
    }

    @staticmethod
    def normalize_whitespace(text: str) -> str:
        return re.sub(r'\s+', ' ', text).strip()  # Replace multiple spaces with one and remove leading/trailing spaces

    @staticmethod
    def from_transcript_to_action(transcript: str):
        if not transcript:
            return transcript
        transcript = transcript.lower().strip()
        transcript = ActionCatalog.normalize_whitespace(transcript)        
        words = transcript.split(' ')
        result = [ActionCatalog.catalog.get(word, word) for word in words]
        return ' '.join(result)
