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
    
    yedek_sayi=sayi #programın sonuna kadar sayının tamamını tutacağım yedek değişken oluşturdum.
    i=0 #döngü için i değişkeni oluşturdum.
    son_sayi="" #string olarak sayıları virgülden sonra basamak basamak alacağım değişkeni oluşturdum.
    stSayi=str(sayi)+"." #string olarak tuttuğum sayıları toplu halde atacağım değişkeni oluşturdum.
    #en sonuna . koyup \0 biçiminde döngüde sayılar sonlansa dahi hata vermemesini sağladım.
    if sayi>int(sayi): #sayının desimal olup olmadığını int türündeki karşılığını yaparak kontrol ettirdim.
        #eğer sayi int türündeki değerinden büyükse desimaldir. Alt satırlardaki işlemleri ona göre yaptırdım.
        
        while stSayi[i]!=".": #string olarak tuttuğum sayı değişkeninin her hanesini . olana kadar kontrol ettirdim.
            i=i+1 #i değişkenini her seferinde 1 arttırıp döngünün devamlılığını sağladım.
        
        i=i+1 #döngü bittiğinde i değişkenini tekrar 1 arttırıp nokta işaretinden sonraki basamağa geçmesini sağladım.
        
        while stSayi[i]!=".": #string olarak tuttuğum sayı değişkenini tekrar . olana kadar kontrol ettirdim.
            #buradaki nokta en sonda bulunan nokta oluyor. İlk döngüde desimal değerin noktasını atlamıştık.
            son_sayi+=str(stSayi)[i] #son_sayi adli string değişkene stSayi değişkenindeki rakamları ardı ardına atadım.
            i=i+1 #i değişkenini tekrar döngüde 1 arttırarak sonraki basamağa geçişi sağladım.
    
        son_sayi=int(son_sayi) #string olan son_sayi değişkenini integer tipine çevirdim.
        
    while int(sayi)>0.9: #sayı .9dan büyük olduğu sürece döngü dönecek.
        sayi/=10 #sayi değişkenini 10'a bölerek her seferinde 1 basamak azaltıyorum.
        sayac+=1 #sayac değişkenini her seferinde 1 arttırarak basamak hesabını hafızada tutuyorum.
    
    if yedek_sayi>int(yedek_sayi): #yedek sayının desimal olup olmadığını kontrol ediyorum.
        #yedek_sayi değişkeninin int hali virgülden sonrasını almayacağı için daha küçük olacak.
        return sayac + basamak_hesabi(son_sayi) #sayac değişkenini (basamak değerini) ve 
    #son_sayi(virgülden sonraki sayı)yı toplatıp fonksiyondan geri döndürüyorum.
    
    else:
        return sayac #yedek_sayi değişkenimiz yani girilen sayımız desimal değilse virgül
    #sonrasını hesaplamayacağımız için sayac yani hesaplanan değeri geri döndürüyorum.



print ("desimalsiz bölümün uzunluğu=",basamak_hesabi(d)) #basamak hesabını sayıyı yollayarak ekrana bastırıyorum.
print ("desimal ile bölümün uzunluğu=",basamak_hesabi(c))
