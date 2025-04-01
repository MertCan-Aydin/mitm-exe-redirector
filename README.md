
# 📜 Proje Açıklaması: Phthon ile Otomatikleştirilmiş MITM Sarlırısı

## 🔍 **Projenin Amacı**
Bu araç, **siber güvenlik uzmanlarına** ve **etik hacker'lara** yönelik geliştirilmiş bir eğitim simülasyonudur. Temel işlevleri:
- Ağ trafiğini manipüle ederek `.exe` indirmeleri yönlendirme
- ARP spoofing ile tam trafik denetimi
- Gerçekçi penetrasyon test senaryoları oluşturma

## 🛠️ **Nasıl Çalışır?**
1. **Ağ Dinleme**: 
   - Bettercap ile yerel ağdaki cihazlar tespit edilir
     
2. **ARP Manipülasyonu**:
   - Hedef cihazın trafiği sizin üzerinize yönlendirilir

3. **Backdoor Yerleştirme**:
   - Msfvenom ile oluşturulan özel backdoor

4. **Yönlendirme Mekanizması**:
   - Mitmproxy, `.exe` isteklerini otomatik olarak backdoor'a yönlendirir

## 🌟 **Öne Çıkan Özellikler**
| Özellik | Açıklama |
|---------|----------|
| **Görünmez Yönlendirme** | Kullanıcılar orijinal dosyayı indirdiğini sanar |
| **SSL Bypass** | Mitm.it sertifikasıyla şifreli trafik çözülür |
| **Çoklu Hedef** | Tüm ağ veya tek cihaz seçilebilir |

## ⚠️ **Yasal Uyarı**
Bu araç **sadece**:
- Yetkili güvenlik testlerinde
- Kendi ağınızda
- Yazılı izinle kullanılabilir

**Örnek Kullanım Senaryoları**:
- Kurumsal ağ güvenlik testleri
- Siber güvenlik eğitimleri
- Zararlı yazılım davranış analizleri

## 💡 **Neden Önemli?**
- Şirketlerin **indirme güvenliği** zafiyetlerini test eder
- **Sosyal mühendislik** saldırılarının teknik ayağını simüle eder
- Güvenlik uzmanlarının **savunma mekanizmaları** geliştirmesine yardımcı olur

---

### 📌 **Son Not**
Bu proje **Kali Linux** ve **Python 3** ortamında geliştirilmiştir. Tüm testler kontrollü laboratuvar ortamında yapılmıştır. Lütfen **sorumlu kullanım** ilkelerine uyunuz.

> "Bilgi güvenliği, savunma ve saldırı dinamiklerini anlamakla başlar." - Siber Güvenlik Manifestosu

---
