from validator_collection import validators



def main():
    print(email_validate(input("Email: ")))


def email_validate(e):
    e = validators.email

if __name__ == "__main__":
    main()
