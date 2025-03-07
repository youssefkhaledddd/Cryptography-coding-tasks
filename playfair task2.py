import string

def generate_playfair_matrix(keyword):
    keyword = keyword.lower().replace("j", "i")
    seen = set()
    matrix = []
    
    for char in keyword + string.ascii_lowercase:
        if char not in seen and char in string.ascii_lowercase and char != 'j':
            seen.add(char)
            matrix.append(char)
    
    return [matrix[i:i+5] for i in range(0, 25, 5)]

def find_position(matrix, letter):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == letter:
                return row, col
    return None

def process_pairs(text):
    text = text.lower().replace("j", "i").replace(" ", "")
    pairs = []
    i = 0
    while i < len(text):
        a = text[i]
        b = text[i+1] if i + 1 < len(text) else 'x'
        if a == b:
            pairs.append((a, 'x'))
            i += 1
        else:
            pairs.append((a, b))
            i += 2
    return pairs

def encrypt_playfair(plaintext, matrix):
    pairs = process_pairs(plaintext)
    ciphertext = ""
    
    for a, b in pairs:
        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)
        
        if row1 == row2:
            ciphertext += matrix[row1][(col1+1) % 5] + matrix[row2][(col2+1) % 5]
        elif col1 == col2:
            ciphertext += matrix[(row1+1) % 5][col1] + matrix[(row2+1) % 5][col2]
        else:
            ciphertext += matrix[row1][col2] + matrix[row2][col1]
    
    return ciphertext

def decrypt_playfair(ciphertext, matrix):
    pairs = process_pairs(ciphertext)
    plaintext = ""
    
    for a, b in pairs:
        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)
        
        if row1 == row2:
            plaintext += matrix[row1][(col1-1) % 5] + matrix[row2][(col2-1) % 5]
        elif col1 == col2:
            plaintext += matrix[(row1-1) % 5][col1] + matrix[(row2-1) % 5][col2]
        else:
            plaintext += matrix[row1][col2] + matrix[row2][col1]
    
    return plaintext

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(row))

def main():
    keyword = input("Enter the keyword: ")
    matrix = generate_playfair_matrix(keyword)
    print("\nGenerated Playfair Matrix:")
    print_matrix(matrix)
    
    choice = input("Do you want to Encrypt or Decrypt (Write Encrypt or Decrypt)? ").lower()
    text = input("Enter the text: ")
    
    if choice == 'encrypt':
        result = encrypt_playfair(text, matrix)
        print("Encrypted Text:", result)
    elif choice == 'decrypt':
        result = decrypt_playfair(text, matrix)
        print("Decrypted Text:", result)
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
