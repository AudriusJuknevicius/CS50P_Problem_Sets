

def main():
    tweet = input("Input: ")
    tweet = shorten(tweet)
    print("Output: " + tweet)


def shorten(word):
    vowels = ["Ae", "ae", "E", "e", "I", "i", "O", "o", "U", "u"]
    for character in word:
        if character in vowels:
            word = word.replace(character,"")
    return word


if __name__ == "__main__":
    main()
