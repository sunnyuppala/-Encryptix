import random
import string

def generate_password(password_length, password_complexity):
    if password_complexity == 'weak':
        chars = string.ascii_lowercase
    elif password_complexity == 'strong':
        chars = string.ascii_letters + string.digits + string.punctuation
    else:
        raise ValueError("Invalid complexity level. Choose 'weak' or 'strong'.")

    password = ''.join(random.choice(chars) for _ in range(password_length))
    return password

def main():
    print("Password Generator")

    while True:
        try:
            password_length = int(input("Enter the desired length of the password: "))
            if password_length < 1:
                print("Length must be at least 1.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

    while True:
        password_complexity = input("Enter the complexity level ('weak' or 'strong'): ")
        if password_complexity not in ['weak', 'strong']:
            print("Invalid complexity level. Choose 'weak' or 'strong'.")
        else:
            break

    generated_password = generate_password(password_length, password_complexity)
    print(f"Generated Password: {generated_password}")

if __name__ == "__main__":
    main()