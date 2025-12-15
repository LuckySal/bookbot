import sys
from stats import count_words, count_characters, format_counts

def get_book_text(filepath):
    with open(filepath, "r") as f:
        data = f.read()
    return data

def main():
    if len(sys.argv) != 2:
        print('Usage: python3 main.py <path_to_book>')
    else:
        report = (
                    '============ BOOKBOT ============\n'
                    'Analyzing book found at {filepath}\n'
                    '----------- Word Count ----------\n'
                    'Found {wordcount} total words\n'
                    '--------- Character Count -------'
                )
        filepath = sys.argv[1]

        text = get_book_text(filepath)
        book_length = count_words(text)
        character_counts = format_counts(count_characters(text))

        print(report.format(filepath=filepath, wordcount=book_length))
        for character in character_counts:
            print(f'{character['char']}: {character['num']}')
        print('============= END ===============')

if __name__ == "__main__":
    main()