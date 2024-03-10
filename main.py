import random
import string

def generate_key(group_number, chars_per_group, include_special_chars, delimiter):
    key = ''
    chars = string.ascii_letters + string.digits
    if include_special_chars:
        chars += string.punctuation

    for group in range(group_number):
        group_key = ''.join(random.choice(chars) for _ in range(chars_per_group))
        key += group_key
        if group < group_number - 1:
            key += delimiter
    
    return key

if __name__ == "__main__":
    group_number = int(input("Enter the number of groups: "))
    chars_per_group = int(input("Enter the number of characters per group: "))
    include_special_chars = input("Include special characters? (yes/no): ").lower() == 'yes'
    delimiter = input("Enter the delimiter between groups: ")
    keys_to_generate = int(input("Enter the number of keys to generate: "))

    with open("key.txt", "w") as file:
        for _ in range(keys_to_generate):
            generated_key = generate_key(group_number, chars_per_group, include_special_chars, delimiter)
            file.write(generated_key + "\n")

    print(f"{keys_to_generate} keys generated and saved to 'key.txt'.")
