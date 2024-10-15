class RLE:
    def encode(self, input_string):
        encoded = []
        count = 1
        
        for i in range(len(input_string)):
            if i == len(input_string) - 1 or input_string[i] != input_string[i + 1]:
                encoded.append(f"{input_string[i]}{count}")
                count = 1
            else:
                count += 1
        
        return ''.join(encoded)

    def decode(self, input_string):
        decoded = []
        i = 0
        
        while i < len(input_string):
            ch = input_string[i]
            i += 1
            
            count_str = ''
            while i < len(input_string) and input_string[i].isdigit():
                count_str += input_string[i]
                i += 1
            
            count = int(count_str)
            decoded.append(ch * count)
        
        return ''.join(decoded)

if __name__ == "__main__":
    rle = RLE()
    input_string = input("Enter a string to encode: ")
    
    encoded = rle.encode(input_string)
    print(f"Encoded string: {encoded}")
    
    decoded = rle.decode(encoded)
    print(f"Decoded string: {decoded}")
