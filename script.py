import sys
import logging
import os

# Logging configuration
logging.basicConfig(
    filename='log.txt',
    level=logging.INFO,
    format='[%(levelname)s] %(asctime)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# Character to number mapping
char_to_num = {
    '.': 100, "'": 101, '!': 102,
    '-': 103, ' ': 98, ',': 99,
    'A': 56, 'B': 57, 'C': 58, 'D': 59, 'E': 40, 'F': 41, 'G': 42, 'H': 43, 'I': 44,
    'J': 45, 'K': 46, 'L': 47, 'M': 48, 'N': 49, 'O': 60, 'P': 61, 'Q': 62, 'R': 63, 'S': 64, 'T': 65, 'U': 66, 'V': 67,
    'W': 68, 'X': 69, 'Y': 10, 'Z': 11,
    'a': 12, 'b': 13, 'c': 14, 'd': 15, 'e': 16, 'f': 17, 'g': 18, 'h': 19, 'i': 30, 'j': 31, 'k': 32, 'l': 33, 'm': 34,
    'n': 35, 'o': 36, 'p': 37, 'q': 38,
    'r': 39, 's': 90, 't': 91, 'u': 92, 'v': 93, 'w': 94, 'x': 95, 'y': 96, 'z': 97
}

num_to_char = {v: k for k, v in char_to_num.items()}


def text_to_number():
    """
    Convert user input text into a string of numbers separated by commas based on a predefined mapping.

    Prompts the user to enter text until all characters are valid. Logs each conversion step and the final result.

    Returns:
        str: Comma-separated string of numbers representing the input text.
    """
    logging.info("Starting text to number conversion")
    while True:
        text = input("enter text: ")
        converted = ""

        try:
            for ch in text:
                if ch not in char_to_num:
                    raise ValueError(f"Invalid character in input: '{ch}'")

                number = char_to_num[ch]
                logging.info(f"Converting character '{ch}' -> number {number}")
                converted += str(number) + ","

            logging.info(f"Conversion complete. Result: {converted.rstrip(',')}")
            return converted.rstrip(",")

        except ValueError as e:
            logging.error(e)
            print(f"Error: {e}. Please try again.\n")


def numbers_to_text(text):
    """
    Convert a string of numbers back to text using the predefined mapping.

    Checks if the encrypted file exists; logs and exits if it doesn't. Each number is converted back to its corresponding character.

        text (str): Comma-separated string of numbers representing encrypted text.

    Returns:
        str: The decrypted text.
    """
    if not os.path.exists('encrypted_msg.txt'):
        print(f"[ERROR] File '{'encrypted_msg.txt'}' not found!")  # this will show on screen
        logging.error(f"File '{'encrypted_msg.txt'}' not found!") # this will go to log.txt
        sys.exit(1)

    logging.info("Starting number to text conversion")
    for ch in text:
        assert ch.isdigit() or ch == ",", "Invalid character in encrypted file"

    if not text.strip():
        logging.info("Input text is empty")
        return ""

    converted = ""
    for num_str in text.split(","):
        num = int(num_str)
        if num in num_to_char:
            char = num_to_char[num]
            logging.info(f"Converting number {num} -> character '{char}'")
            converted += char

    logging.info(f"Conversion complete. Result: {converted}")
    return converted


def main():
    """
    Main function to handle encryption or decryption based on command-line argument.

    Usage:
        python script.py encrypt
        python script.py decrypt

    Encrypts user input text to numbers or decrypts the contents of 'encrypted_msg.txt' and prints the result.
    Logs all major actions and errors.
    """
    logging.info("Program started")

    if len(sys.argv) != 2:
        logging.error("Usage: python script.py encrypt OR python script.py decrypt")
        sys.exit(1)

    mode = sys.argv[1].lower()
    logging.info(f"Mode selected: {mode}")

    if mode == "encrypt":
        encrypted = text_to_number()
        logging.info("Writing encrypted text to 'encrypted_msg.txt'")
        with open("encrypted_msg.txt", "w") as file:
            file.write(encrypted)
        logging.info("Encryption complete! Saved to 'encrypted_msg.txt'")

    elif mode == "decrypt":
        logging.info("Reading encrypted text from 'encrypted_msg.txt'")
        try:
            with open("encrypted_msg.txt", "r") as file:
                encrypted_text = file.read().strip()
        except FileNotFoundError:
            assert "File 'encrypted_msg.txt' not found!"
            logging.error(AssertionError)
            sys.exit(1)

        decrypted = numbers_to_text(encrypted_text)
        logging.info("Decryption complete!")
        print("\nDecrypted text from the file:\n")
        print(decrypted)

    logging.info("Program finished")


if __name__ == "__main__":
    main()
