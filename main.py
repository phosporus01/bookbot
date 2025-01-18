def main():
    book_path = "books/frankenstein.txt"
    text = get_book_txt(book_path)
    #print(text)
    words = count_words(text)
    #print(words)
    chars = count_characters(text)
    #print(chars)
    report = report_on_character(chars)
    #print(report)
    print(f"--- Begin report of {book_path} ---")
    print(f"{words} words found in the document\n")

    for item in report:
        print(f"The '{item['character']}' character was found {item['counter']} times")
    print("--- End report ---")

def get_book_txt(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    characters = text.lower()
    chars = {}
    for character in characters:
        if character in chars:
            chars[character] += 1
        else:
            chars[character] = 1
    return chars

def report_on_character(chars):
    alpha_chars = []
    def sort_on(chars):
        return chars["counter"]
    for char in chars:
        if char.isalpha() == True:
            tempchar = {"character": char, "counter": chars[char]}
            alpha_chars.append(tempchar)
    alpha_chars.sort(reverse=True, key=sort_on)
    return alpha_chars


main()
