

def main():
    tweet = input("Input: ")
    tweet = shorten(tweet)
    print("Output: " + tweet)


def shorten(word):
    vowels = "AaEeIiOoUu"
    return ''.join([char for char in word if char not in vowels])


if __name__ == "__main__":
    main()
