import random
import string

def generate_password(length, use_uppercase, use_digits, use_special_chars):
    
    lower_chars = string.ascii_lowercase
    upper_chars = string.ascii_uppercase if use_uppercase else ''
    digits = string.digits if use_digits else ''
    special_chars = string.punctuation if use_special_chars else ''
    
    all_chars = lower_chars + upper_chars + digits + special_chars
    
    if not all_chars:
        raise ValueError("At least one character type must be selected.")
    
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

def main():
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length <= 0:
                raise ValueError("Password length must be a positive integer.")
            break
        except ValueError as e:
            print(e)
            continue

    use_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower() == 'yes'
    use_digits = input("Include digits? (yes/no): ").strip().lower() == 'yes'
    use_special_chars = input("Include special characters? (yes/no): ").strip().lower() == 'yes'
    
    try:
        password = generate_password(length, use_uppercase, use_digits, use_special_chars)
        print(f"Generated password: {password}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
