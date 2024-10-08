class Rowcol:
    def __init__(self, numCols):
        self.numCols = numCols

    def encrypt(self, message):
        return ''.join([message[i::self.numCols] for i in range(self.numCols)])

    def decrypt(self, encryptedMessage):
        
        numRows = (len(encryptedMessage) + self.numCols - 1) // self.numCols
       
        fullCols = len(encryptedMessage) % self.numCols
        
        
        colLengths = [numRows] * self.numCols
        for i in range(fullCols, self.numCols):
            colLengths[i] -= 1

       
        rows = [''] * numRows
        index = 0
        for col in range(self.numCols):
            for row in range(colLengths[col]):
                rows[row] += encryptedMessage[index]
                index += 1

        return ''.join(rows)


message = input('Enter a text: ')
numCols = 4

cipher = Rowcol(numCols)

encryptedMessage = cipher.encrypt(message)
print(f"encrypt: '{message}': {encryptedMessage}")

decryptedMessage = cipher.decrypt(encryptedMessage)
print(f"decrypt: {decryptedMessage}")