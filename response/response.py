import validators



def main():
    print(email_validate(input("Email: ")))


def email_validate(e):
    if e := validators.email("someone@example.com"):
        return "Valid"
    else:
        return "Invalid"

if __name__ == "__main__":
    main()
