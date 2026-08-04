class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1 or numRows >= len(s):
            return s

        matris = [["" for j in range(len(s))] for i in range(numRows)] # kelime uzunluğu kadar sütunlu numRows kadar satırlı matris (kelimenin kaplayabileceği maksimum alan)
        cursor = 0
        column = 0

        while cursor < len(s):              # Bütün harfleri dolaşma
            for row in range(numRows):
                if cursor < len(s):
                    matris[row][column] = s[cursor]
                else:
                    return self.mr(matris, numRows, s)
                cursor += 1
            
            for row in range(numRows - 2, 0, -1):
                column += 1
                if cursor < len(s):
                    matris[row][column] = s[cursor]
                else: 
                    return self.mr(matris, numRows, s)
                cursor += 1
            
            column += 1
    
        return self.mr(matris, numRows, s)
    
    # Matrisi sırayla okuma fonksiyonu
    def mr(self, matris, numRows, s):
        text = ""
        for i in range(numRows): # Matrisi sırayla kelimeye dökme
            for j in range(len(s)):
                text += matris[i][j]
        
        return text