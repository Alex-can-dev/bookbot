# return number of words
def count_words(file):
    words = file.split()
    count_of_words = len(words)
    return count_of_words

def main():
    path_to_file = "books/frankenstein.txt"

    with open(path_to_file) as f:
        file_contents = f.read()

    print(count_words(file_contents))

main()