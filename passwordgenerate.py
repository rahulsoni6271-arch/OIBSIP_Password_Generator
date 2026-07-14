import random
import string

def generate_password():
    print("=" * 40)
    print("      RANDOM PASSWORD GENERATOR")
    print("=" * 40)

    # Password length
    while True:
        try:
            length = int(input("Enter password length (8-64): "))
            if length < 8 or length > 64:
                print("Please enter a number between 8 and 64.")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    # Character type selection
    print("\nSelect character types:")
    use_letters = input("Include Letters (A-Z, a-z)? (y/n): ").strip().lower() == "y"
    use_numbers = input("Include Numbers (0-9)? (y/n): ").strip().lower() == "y"
    use_symbols = input("Include Symbols (!@#$%^&*)? (y/n): ").strip().lower() == "y"

    # Character pool
    char_pool = ""

    if use_letters:
        char_pool += string.ascii_letters

    if use_numbers:
        char_pool += string.digits

    if use_symbols:
        char_pool += string.punctuation

    # Validation
    if not char_pool:
        print("\nError: You must select at least one character type!")
        return

    # Generate password
    password = "".join(random.choice(char_pool) for _ in range(length))

    # Output
    print("\n" + "=" * 40)
    print("       YOUR GENERATED PASSWORD")
    print("=" * 40)
    print(password)
    print("=" * 40)


if __name__ == "__main__":
    generate_password()