from stats import count_words, count_characters

def get_book_text(filepath):
    with open(filepath, "r") as f:
        data = f.read()
    return data

def main():
    frankenstein = get_book_text("books/frankenstein.txt")
    frankenstein_length = count_words(frankenstein)
    character_counts = count_characters(frankenstein)
    print(f'Found {frankenstein_length} total words')
    print(character_counts)

if __name__ == "__main__":
    main()