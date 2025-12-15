def count_words(text):
    return len(text.split())

def count_characters(text):
    character_counts = {}
    for c in text:
        c = c.lower()
        character_counts[c] = character_counts.setdefault(c, 0) + 1
    return character_counts