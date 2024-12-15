
class ActionCatalog:
    
    catalog = {
        'kubectl': 'kubectl',
        'cubectl': 'kubectl',
        'bots': 'pods'
    }
        
    @staticmethod
    def from_transcript_to_action(transcript: str):
        if not transcript:
            return transcript
        transcript = transcript.lower().strip().replace("  ", " ")
        words = transcript.split(' ')
        result = [ActionCatalog.catalog.get(word, word) for word in words]
        return ' '.join(result)
