## Kurulum için (**Sadece Mac**)
1. Vpn ismini **MyVPN** ile değiştirilelim. (http://prntscr.com/4hmb7m)
2. Eski Vpn giriş bilgilerini boşaltalım. (http://prntscr.com/4hmli4)
3. Vpn normal şekilde bağlanmaya çalışın
4. Tüm soru ekranlarında **Save in Keychain**
5. Aşağıdaki komutları terminalden uygulayalım
```sh
sudo curl https://raw.githubusercontent.com/ahmetkapikiran/TunnelBlick-Login/master/vpnlogin.py > /usr/bin/vpnlogin
chmod +x /usr/bin/vpnlogin
vim ~/secretkey.txt içine 16 haneli secret yazılmalı.
```

## Spotlight üzerinden vpn bağlantısını kurmak için,

1. vpnlogin.zip dosyasını açın.
2. İçerisinden çıkan dosyayı Applications altına kopyalayın.
3. Applications klasörüne gidin ve vpnlogin dosyasını sağ tıklayıp open'ı tıklayın.
4. Spotlight üzerinden vpnlogin yazarak vpn bağlantısını kurabilirsiniz.

## Terminal için
```sh
vpnlogin
```