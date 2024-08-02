def main():
    # Count words
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    num_words = get_num_words(text)

    # Create chars dict
    lower_text = text.lower()
    num_chars = count_chars(lower_text)
    print("The text has this number of chars", num_chars)

    # Final output
    print("--- Begin report of books/frankenstein.txt ---")
    print(num_words, " words found in the document\n")
    char_values = sorted_dict(num_chars)
    for i in range(len(char_values)):
        if char_values[i][0].isalpha():
            print(f"The {char_values[i][0]} character was found {char_values[i][1]} times")
    print("--- End report ---")

def sorted_dict(dict):
    sorted_items = sorted(dict.items(), key=lambda item: item[1], reverse=True)
    return sorted_items

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