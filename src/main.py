# Project py-learn-class Main file

def main():
    print("START OF PROGRAM")
    word_pair_file = open("resources/pairs.txt")
    word_list_file = open("resources/words.txt")
    word_list = set(word_list_file.read().split())

    for line in word_pair_file:
        start, end = line.split()
        print("start:end = " + start + ":"  + end)

    word_pair_file.close()
    word_list_file.close();

    print("\nEND OF PROGRAM")

if __name__ == "__main__":
    main()
