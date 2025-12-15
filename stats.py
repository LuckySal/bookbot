def count_words(text):
    return len(text.split())


def count_characters(text):
    character_counts = {}
    for c in text:
        c = c.lower()
        character_counts[c] = character_counts.setdefault(c, 0) + 1
    return character_counts


def sort_on(items):
    return items["num"]


def format_counts(counts_dict):
    counts_list = []
    for key, value in counts_dict.items():
        if key.isalpha():
            counts_list.append({"char": key, "num": value})
    counts_list.sort(reverse=True, key=sort_on)
    return counts_list
