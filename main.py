def main():
    # Count words
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    num_words = get_num_words(text)
    print("The text has", num_words, "words.")

    # Create chars dict
    lower_text = text.lower()
    num_chars = count_chars(lower_text)
    print("The text has this number of chars", num_chars)

def count_chars(text):
    chars_dict = {}
    for char in text:
        chars_dict[char] = chars_dict.get(char, 0) + 1
    return chars_dict

def get_num_words(text):
    words = text.split()
    return len(words)

def get_text(path):
    with open(path) as f:
        return f.read()

main()