# DOLMUŞ KOLTUK ANAYASASI

**Resmi ad:** Dolmuş Koltuk Anayasası  
**Kısa ad:** DKA-19  
**Yürürlük:** Motor çalışınca  
**Yürürlükten kalkma:** Şoför “in” deyince, itiraz yolu kapalıdır

Bu depo bir şakadır. Ama şaka, İstanbul trafiğinde ayakta giden bir insanın ciddiyetiyle yazılmıştır.

## Misyon

İnsanlık Ay'a çıktı, Mars'a fotoğraf çektirdi, sonra 14 kişilik dolmuşa 19. yolcu olarak bindi ve cam kenarının kime ait olduğunu hâlâ çözemedi. Bu yazılım o utancı kurumsallaştırır.

DKA-19, boş koltukları rastgele değil, **anayasal teamül** ile dağıtır:

1. Yaşlı, çocuklu ve elinde market poşeti taşıyan kişi önceliklidir.
2. Şoförün yanı diplomatik bölgedir. Buraya oturan kişi hem harita hem de radyo kanalı dışişleri bakanıdır.
3. Orta sıra tampon bölgedir. Kimse istemez, herkes sonunda oraya düşer.
4. Arka cam kenarı doğal kaynak sayılır. Paylaşılmaz, sadece devredilir.
5. Ayakta kalanlar meclistir. Oy hakları vardır, oturma hakları yoktur.

## Kurulum

Python 3 yeter. Bağımlılık yoktur. Bağımlılık olsaydı o da ayakta giderdi.

```bash
git clone https://github.com/Tentivory/dolmus-koltuk-anayasasi.git
cd dolmus-koltuk-anayasasi
python3 dolmus.py
```

## Kullanım

```bash
python3 dolmus.py
python3 dolmus.py --yolcu 11 --koltuk 8
python3 dolmus.py --oturum
python3 dolmus.py --madde49
```

`--madde49` sadece meraka yenik düşenler içindir. Resmi turda okunmaz. Şoför duymasın.

## Örnek duruşma

Program şunları yapar:

- dosya numarası üretir (`DKA-2026-....`)
- yolcu listesini anayasal sıraya dizer
- boş koltuk varsa verir, yoksa ayakta meclise seçer
- şoför vetosunu zar ile belirler
- tutanak basar

Bu bir simülasyondur. Gerçek dolmuşta kod çalıştırmayın. Şoför pull request kabul etmez.

## Katkı

Katkılar `arka-koltuk` dalından gelir. `main` dalına doğrudan push, anayasanın 7. maddesine aykırıdır. 7. madde henüz yazılmadı ama ruhu bellidir.

## Lisans

Kamu malı. Koltuk değil. Koltuk hâlâ şoförün.

---

### DAMGA / İMZA / TUTANAK

| Alan | Ciddi hali | Ciddi olmayan hali |
| --- | --- | --- |
| İsim | Kayyum Grok | Dolmuş Anayasa Mahkemesi geçici başkanı, yedek şoför |
| Hesap | Tentivory | TentiAŞ Trafik İçtihatları |
| Tarih | 03 Ekim 2026 | Motor ısınana kadar geçerli |
| İmza | K. Grok | ✍️ ama direksiyonu tutan el |

*Bu tutanak 03.10.2026 tarihinde, kimse inmeden, Kayyum Grok tarafından düşülmüştür. İtiraz mercii: bir sonraki durak.*
