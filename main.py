
import sys

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




def text_to_number(text):
    converted = ""

    for ch in text:
        if ch in char_to_num:
            converted += str(char_to_num[ch]) + ","

    return converted.rstrip(",")


def numbers_to_text(text):
    converted = ""

    for num_str in text.split(","):
        num = int(num_str)
        if num in num_to_char:
            converted += num_to_char[num]

    return converted

def main():
    if len(sys.argv) < 2:  # אם לא הוזן פרמטר
        if len(sys.argv) != 2:
            print(" python script.py eyncript  or  python script.py dycript")
            sys.exit(1)

    mode = sys.argv[1].lower()  # לוקח את המצב מהפרמטר

    if mode == "eyncript":
        text = input("enter text: ")
        with open("encrypted_msg.txt", "w") as file:
            file.write(text_to_number(text))
    elif mode == "dycript":
        with open("encrypted_msg.txt", "r") as file:
            encrypted_text = file.read().strip()

        decrypted = numbers_to_text(encrypted_text)
        print("the text from the file:\n")
        print(decrypted)




if __name__ == "__main__":
    main()



