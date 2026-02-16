def extract_city(text):
    text = text.lower()

    # Common filler words to ignore
    ignore = [
        "what","is","the","weather","in","today","temperature",
        "of","will","it","rain","whats","what's","show","tell","me"
    ]

    words = text.split()

    # Return last meaningful word (usually city)
    for w in reversed(words):
        if w not in ignore:
            return w.capitalize()

    return None
