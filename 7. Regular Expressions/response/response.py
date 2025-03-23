import validators



def main():
    print(email_validate(input("Email: ")))


def email_validate(e):
    if e := validators.email(e):
        return "Valid"
    else:
        return "Invalid"


if __name__ == "__main__":
    main()


