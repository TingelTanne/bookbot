def wordcounter(whole_text):
    word_count = 0
    word_count = len(whole_text.split())
    print(word_count)

def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
    wordcounter(file_contents)
    

main()