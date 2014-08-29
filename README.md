## Kurulum için (**Sadece Mac**)
1. Vpn ismini **MyVPN** ile değiştirilelim. (http://prntscr.com/4hmb7m)
2. Eski Vpn giriş bilgilerini boşaltalım. (http://prntscr.com/4hmli4)
3. Vpn normal şekilde bağlanmaya çalışın
4. Tüm soru ekranlarında **Save in Keychain**
5. Aşağıdaki komutları terminalden uygulayalım
```sh
sudo curl https://raw.githubusercontent.com/ahmetkapikiran/TunnelBlick-Login/master/vpnlogin.py > /usr/bin/vpnlogin
chmod +x /usr/bin/vpnlogin
vim ~/secretkey.txt içine secret yazılmalı.
```

## Otomatik login olmak için terminale
```sh
vpnlogin
```