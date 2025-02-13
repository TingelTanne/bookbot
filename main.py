def wordcounter(text):
    word_count = 0
    word_count = len(text.split())
    print(word_count)

def lettercounter(text):
    letters_counted = dict()
    text_lowered = text.lower()
    for letter in text_lowered:
        if letter not in letters_counted:
            letters_counted[str(letter)] = 1
        else:
            letters_counted[str(letter)] += 1
    print(letters_counted)

def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
    #wordcounter(file_contents)
    lettercounter(file_contents)
    

main()