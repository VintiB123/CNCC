def crc_encode(data, generator):
 
    augmented_data = data + '0' * (len(generator) - 1)

    remainder = binary_modulo_division(augmented_data, generator)
   
    return data + remainder

def binary_modulo_division(dividend, divisor):
   
    remainder = dividend[:len(divisor)]
    for bit in dividend[len(divisor):]:
        remainder += bit
        
        if remainder[0] == '1':
            remainder = ''.join(str(int(b1) ^ int(b2)) for b1, b2 in zip(remainder, divisor))
        remainder = remainder[1:]

 
    return remainder.zfill(len(divisor) - 1)


data = "11010011101100"
generator = "1011"
encoded_data = crc_encode(data, generator)
print("Data with CRC:", encoded_data)
