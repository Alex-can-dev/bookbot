# return number of words
def count_words(file):
    words = file.split()
    count_of_words = len(words)
    return count_of_words

# return the number of times each character appears in the book
def count_charakters(file):
    lowered_words = file.lower()
    all_char = {}

    for char in lowered_words:
        if char.isalpha() == True:
            if char in all_char:
                all_char[char] += 1
            else:
                all_char[char] = 1

    my_keys = list(all_char.keys())
    my_keys.sort()

    sd = {i: all_char[i] for i in my_keys}

    return sd

def main():
    path_to_file = "books/frankenstein.txt"
    print("--- Begin report of " + path_to_file + " ---")

    with open(path_to_file) as f:
        file_contents = f.read()

    print(str(count_words(file_contents)) + " words found in the document\n")
    
    for key, value in count_charakters(file_contents).items():
        print(f"The '{key}' character was found {value} times")
    
    print("--- End report ---")

main()