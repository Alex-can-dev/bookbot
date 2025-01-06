# return number of words
def count_words(file):
    words = file.split()
    count_of_words = len(words)
    return count_of_words

# return the number of times each character appears in the book
def count_charakters(file):
    lowered_words = file.lower()
    list = {}

    for char in lowered_words:
        if char.isalpha() == True:
            if char in list:
                list[char] += 1
            else:
                list[char] = 1

    return list

def main():
    path_to_file = "books/frankenstein.txt"

    with open(path_to_file) as f:
        file_contents = f.read()

    print(count_words(file_contents))
    print(count_charakters(file_contents))

main()