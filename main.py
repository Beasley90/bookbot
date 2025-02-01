
def word_counter(text):
    return len(text.split())

def character_count(text):
    res = {}
    for letter in text.lower():
        if letter not in res:
            res[letter] = 0
        res[letter] += 1
    return res

def sort_on(key):
    return key["count"]

def sort_dict(dictionary):
    sorted_dict = []
    for letter in dictionary:
        sorted_dict.append({"letter": letter, "count":dictionary[letter]})
    sorted_dict.sort(reverse=True,key=sort_on)
    return sorted_dict

def main():
    try:
        book_path = "books/frankenstein.txt"
        with open(book_path) as f:
            file_contents = f.read()
        word_count = (word_counter(file_contents))
        letter_count = character_count(file_contents)
        sorted_list = sort_dict(letter_count)
        print(f"--- Begin report of {book_path} ---")
        print(f"{word_count} words found in the document")
              
        for letter in sorted_list:
            if letter["letter"].isalpha() == True:
                print(f"The '{letter['letter']}' character was found {letter['count']} times")
        
        print("--- End of Report ---")
    except FileNotFoundError:
        print("File not found.")

    

if __name__ == "__main__":
    main()
    
