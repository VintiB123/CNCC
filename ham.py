def encode_hamming(data):
    m = len(data)
    r = 0
    
    
    while (2 ** r) < (m + r + 1):
        r += 1

    hamming_code = ['0'] * (m + r)

    
    j = 0
    for i in range(1, len(hamming_code) + 1):
        if (i & (i - 1)) == 0: 
            continue
        hamming_code[i - 1] = data[j]
        j += 1

    
    for i in range(r):
        parity_pos = 2 ** i
        parity_val = 0
        for j in range(1, len(hamming_code) + 1):
            if j & parity_pos: 
                parity_val ^= int(hamming_code[j - 1])  
        hamming_code[parity_pos - 1] = str(parity_val)

    return ''.join(hamming_code)

def detect_and_correct_hamming(received_code):
    n = len(received_code)
    r = 0

    while (2 ** r) < n:
        r += 1

    error_pos = 0

    
    for i in range(r):
        parity_pos = 2 ** i
        parity_val = 0
        for j in range(1, n + 1):
            if j & parity_pos:
                parity_val ^= int(received_code[j - 1])  
        if parity_val:  
            error_pos += parity_pos

    if error_pos > 0:  
        corrected_code = list(received_code)
        corrected_code[error_pos - 1] = '1' if corrected_code[error_pos - 1] == '0' else '0'  # Correct the error
        return ''.join(corrected_code), error_pos

    return received_code, 0  


data = "1011"
encoded_hamming = encode_hamming(data)
print("Encoded Hamming Code:", encoded_hamming)


received_code = encoded_hamming[:4] + '0' + encoded_hamming[5:]

corrected_code, error_pos = detect_and_correct_hamming(received_code)
print("Received Code with Error:", received_code)
if error_pos > 0:
    print(f"Error detected at position {error_pos}")
    print("Corrected Code:", corrected_code)
else:
    print("No errors detected")
