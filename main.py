def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_num_words(text)
    each_character = get_chars_dict(text)
    
    print(text, end="\n\n")
    print(f"~ * ~ * ~ Report: {book_path} ~ * ~ * ~", end="\n\n")
    print(f"This book contained {word_count} words.", end="\n\n")
    
    for char in each_character:
        print(f"The '{char}' character was found {each_character[char]} times", end="\n")
    
    
    

    
def get_book_text(path):
    with open(path) as f:
        return f.read()
    

def get_num_words(text):
    return len(text.split())
    
        
def get_chars_dict(text):
    words = text.split()
    characters = {}
    
    for char in text.lower():
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
    return characters
    
    
    
    
    
    
    
    
main()