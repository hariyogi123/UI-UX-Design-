import random
import string

# Function to generate a random password
def generate_password(length, use_uppercase, use_digits, use_special):
    # Define character pools based on user preferences
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase if use_uppercase else ""
    digits = string.digits if use_digits else ""
    special = string.punctuation if use_special else ""

    # Ensure there's at least one character from each selected category
    mandatory = (
        random.choice(lower) +
        (random.choice(upper) if upper else "") +
        (random.choice(digits) if digits else "") +
        (random.choice(special) if special else "")
    )

    # Combine all selected characters
    all_characters = lower + upper + digits + special
    if len(all_characters) < length:
        remaining = ''.join(random.choices(all_characters, k=length - len(mandatory)))
        password = mandatory + remaining
    else:
        password = ''.join(random.choices(all_characters, k=length))

    # Shuffle the password to ensure randomness
    return ''.join(random.sample(password, len(password)))

# Main program
def main():
    print("Welcome to the Enhanced Password Generator!")
    try:
        # Get password length from the user
        length = int(input("Enter the desired length of the password: "))
        if length < 6:
            print("Password length should be at least 6 characters for security reasons.")
            return

        # Get user preferences for password components
        use_uppercase = input("Include uppercase letters? (y/n): ").strip().lower() == "y"
        use_digits = input("Include digits? (y/n): ").strip().lower() == "y"
        use_special = input("Include special characters? (y/n): ").strip().lower() == "y"

        # Ensure at least one category is selected
        if not (use_uppercase or use_digits or use_special):
            print("You must include at least one of uppercase letters, digits, or special characters.")
            return

        # Generate the password
        password = generate_password(length, use_uppercase, use_digits, use_special)

        # Display the generated password
        print(f"\nGenerated Password: {password}")
    except ValueError:
        print("Please enter a valid number for the password length.")

# Run the program
if __name__ == "__main__":
    main()
