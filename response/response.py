import validators



def main():
    print(email_validate(input("Email: ")))


def email_validate(e):
    e = validators.email("someone@example.com")

if __name__ == "__main__":
    main()
