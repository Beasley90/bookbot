
def word_counter(text):
    return len(text.split())

def character_count(text):
    res = {}
    for letter in text.lower():
        if letter not in res:
            res[letter] = 0
        res[letter] += 1
    return res

def main():
    try:
        with open("books/frankenstein.txt") as f:
            file_contents = f.read()
        # print(file_contents)
        word_count = (word_counter(file_contents))
        letter_count = character_count(file_contents)
        print("--- Begin report of books/frankenstein ---")
        print(f"{word_count} words found in the document")
              
        for letter in letter_count:
            if letter.isalpha() == True:
                print(f"The '{letter}' character was found {letter_count[letter]} times")
        
        print("--- End of Report ---")
    except FileNotFoundError:
        print("File not found.")

    

if __name__ == "__main__":
    main()
    
