#Normal sayıların kusüratları 17 haneye kadar hesaplanabilirken desimal sayılar 28 haneye kadar hassaslık sağlar.
import decimal #decimal kütüphanesini ekledim.
a=decimal.Decimal(22.0) #a sayısını decimal tipinde tanımladım.
b=decimal.Decimal(7.001) #b sayısını decimal tipinde tanımladım.
c=decimal.Decimal(a/b) #c sayısının hesabını decimal tipinde yaptırıp atama yaptırdım.
d=22.0/7.001 #d sayısının hesabını normal hesaplatıp atama yaptırdım.
print(c,d) #c ve d sayılarını ekrana bastırdım.

def basamak_hesabi(sayi): #basamak hesaplarını yaptırmak için basamak_hesabi adında sayi değişkenini dışarıdan alan fonksiyon oluşturdum.
    sayac=0 #basamak hesabını tutması için sayac değişkeni oluşturup 0 dan başlattım.
    sabit=int(sayi) #ondalıklı sayılarda virgülden öncesini hesaplatmak için sabit adında değişken oluşturup girilen sayının virgül solundaki kısmını aldım.
    
    if sayi>int(sayi): #sayının desimal olup olmadığını int türündeki karşılığını yaparak kontrol ettirdim.
        #eğer sayi int türündeki değerinden büyükse desimaldir. Alt satırlardaki işlemleri ona göre yaptırdım.
        
        while sayi>int(sayi): #sayı desimal olduğu sürece döngü çalışacak.
            sayac+=1 #döngüye her girdiğinde sayac değişkenini 1 arttırıyorum.
            sayi=sayi*10 #sayi değişkenini her döngüye girdiğinde 10 ile çarparak tam sayıya yaklaştırıyorum.
        
        return sayac  + desimal(sabit) #sayac değişkeninin son değeriyle desimal fonksiyonuna sayının sabit kısmını
    #yolluyorum. Böylece aşağıdaki adımlarda tam değerinin basamak uzunluğunu da hesaplıyor. (özyinelemeli fonksiyon kullandım)
    
    else: #eğer sayı desimal değilse
        while sayi>0.9: #sayi değişkenimiz desimal olana kadar aşağıdaki kod bloğunu çalıştırıyorum.
            sayi/=10 #sayi değişkenini 10'a bölerek her seferinde 1 azaltıyorum.
            sayac+=1 #sayac değişkenini her seferinde 1 arttırarak basamak hesabını hafızada tutuyorum.
        return sayac #sayac değişkenini (basamak değerini) fonksiyondan geri yolluyorum.

print ("desimalsiz bölümün uzunluğu=",basamak_hesabi(d)) #basamak hesabını sayıyı yollayarak ekrana bastırıyorum.
print ("desimal ile bölümün uzunluğu=",basamak_hesabi(c))
