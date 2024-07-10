def caesar_cipher(text, shift, direction):
    result = ""
    if direction == 'decrypt': shift = -shift
    for char in text:
        if char.isalpha():
            shift_amount = 65 if char.isupper() else 97
            result += chr((ord(char) + shift - shift_amount) % 26 + shift_amount)
        else:
            result += char
    return result

def main():
    while True:
        choice = input("Encrypt/Decrypt/Exit: ").lower()
        if choice == 'exit': break
        elif choice in ['encrypt', 'decrypt']:
            text = input("Message: ")
            shift = int(input("Shift: "))
            print(f"Result: {caesar_cipher(text, shift, choice)}")
        else: print("Invalid choice.")
            
if __name__ == "__main__":
    main()
