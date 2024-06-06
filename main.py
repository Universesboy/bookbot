def main():
    book_path = "/home/colin/workspace/github.com/Universesboy/bookbot/books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    character_count = count_characters(text)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    print()
    for char, count in sorted(character_count.items()):
        print(f"The '{char}' character was found {count} times")
    
    print("--- End report ---")

def count_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def count_characters(text):
    chars = {}
    for c in text:
        lowerd = c.lower()
        if lowerd in chars:
            chars[lowerd]+=1
        else:
            chars[lowerd]=1
    return chars


main()

# Path: bookbot/books/frankenstein.txt

