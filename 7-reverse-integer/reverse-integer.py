class Solution:
    def reverse(self, x: int) -> int:
        step = 0 # Sayının kaç basamaklı olduğunu tutan değişken
        flag = 0 # Sayı pozitif demek
        dizi = [] # Sayının elemanlarını sırayla tutmak için liste
        result = 0
        
        # Sayıyı negatif ise pozitifleştirme
        if x < 0:
            x = x*-1 
            flag = 1 # Sayı negatif demek

        y = x # temp değişkeni

        # Sayının kaç basamaklı olduğunu sayma
        while y > 0:
            y = y//10
            step +=1
        
        step -= 1 # Basamak sayısına eşitlemek için
        
        y = x   # temp değişkeninin reseti

        # Input'un basamaklarını sırayla diziye işleme
        for i in range(step,-1,-1):
            y = (x // (10**i)) % 10
            dizi.append(y)
        
        # Dizinin sonundaki basamakları çıkartma döngüsü
        for i in range(len(dizi)-1,-1,-1):
            if dizi[i] != 0:
                break
            else:
                del dizi[i]
        
        if len(dizi) > 10:      # Eğer eleman sayısı 10'dan fazlaysa (kesinlikle 32-bit'ten fazladır) 0 döndür.
            return 0
        elif len(dizi) < 10:    # Eğer eleman sayısı 10'dan az ise(kesinlikle 32-bit sınırı içerisindedir) sayıyı döndür.
            # Dizideki elemanları basamaklarına göre tersten toplama işlemi.
            for i in range(len(dizi)-1,-1,-1):
                result += dizi[i]*(10**i)
            
            return result if flag == 0 else result*-1
        else:   # Eğer sayı 10 basamaklı ise
            if flag == 0:   # Pozitif sayılar için
                for i in range(len(dizi)-1,-1,-1):
                    # 32-bit sınır kontrolü
                    if result > (2**31 - 1) - (dizi[i] * (10**i)):
                        return 0
                    result += dizi[i]*(10**i)
            else:
                for i in range(len(dizi)-1,-1,-1):
                    # 32-bit sınır kontrolü
                    if result > (2**31) - (dizi[i] * (10**i)):
                        return 0
                    result += dizi[i]*(10**i)
            
            return result if flag == 0 else result*-1