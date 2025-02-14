def wordcounter(text):
    word_count = 0
    word_count = len(text.split())
    return word_count

def lettercounter(text):
    all_counted = dict()
    text_lowered = text.lower()
    for letter in text_lowered:
        if letter not in all_counted:
            all_counted[str(letter)] = 1
        else:
            all_counted[str(letter)] += 1
    letters_counted = []
    for key in all_counted:
        if key.isalpha():
            letters_counted.append({"letter": key, "count": all_counted[key]})

    def sort_on(dict):
        return dict["count"]

    letters_counted.sort(reverse=True, key=sort_on)

    return letters_counted

def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
    total_words = wordcounter(file_contents)
    total_letters = lettercounter(file_contents)

    print("--- Begin report of books/frankenstein.txt ---")
    print(total_words, "words found in the document\n")
    #print()
    for letter in total_letters:
        print(f"The '{letter["letter"]}' character was found {letter["count"]} times")
    
    

main()