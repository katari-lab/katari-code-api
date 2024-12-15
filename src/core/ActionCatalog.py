class ActionCatalog:
    
    catalog = {
        'kubectl': 'kubectl',
        'cubectl': 'kubectl'
    }
        

    @staticmethod
    def from_transcript_to_action(transcript: str):
        transcript = transcript.lower()
        transcript = transcript.strip()
        transcript = transcript.replace("  ", " ")
        words = transcript.split(' ')
        result = []
        for w in words:
            result.append(ActionCatalog.catalog.get(w, w))                    
        return ' '.join(result)


