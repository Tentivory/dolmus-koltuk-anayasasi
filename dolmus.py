#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Dolmuş Koltuk Anayasası simülatörü. Ciddi bir şakadır."""

from __future__ import annotations

import argparse
import base64
import random
import textwrap
from datetime import datetime

KOLTUK = 8  # çift sıra + şoför yanı, akademisyenler 14 der ama anayasa 8 bilir

UNVANLAR = [
    "cam kenarı doğal kaynak hakimi",
    "orta sıra tampon bölge üyesi",
    "şoför yanı dışişleri bakanı",
    "arka cam vekili",
    "poşetli yolcu öncelik komisyonu",
    "ayakta meclis sözcüsü",
]

BAHANELER = [
    "bir duraklık ineceğim",
    "yaşlı yakınım var, o şu an evde",
    "dizin ağrıyor, sadece fotoğrafı yok",
    "çocuğum uyudu, çocuk şu an okulda",
    "ben turistim, anayasa farklı ülke",
    "şoförü tanıyorum, tanımıyorum ama tanışırız",
]


def dosya_no() -> str:
    n = random.randint(1000, 9999)
    return f"DKA-2026-{n}"


def dagit(yolcu: int, koltuk: int) -> dict:
    oturan = min(yolcu, koltuk)
    ayakta = max(0, yolcu - koltuk)
    vekiller = [random.choice(UNVANLAR) for _ in range(oturan)]
    veto = random.random() < 0.17  # şoför keyfi, bilimsel değil anayasal
    return {
        "oturan": oturan,
        "ayakta": ayakta,
        "vekiller": vekiller,
        "veto": veto,
        "bahaneler": random.sample(BAHANELER, k=min(3, len(BAHANELER))),
    }


def tutanak(yolcu: int, koltuk: int) -> str:
    sonuc = dagit(yolcu, koltuk)
    no = dosya_no()
    saat = datetime.now().strftime("%d.%m.%Y %H:%M")
    satirlar = [
        "=" * 54,
        "DOLMUŞ KOLTUK ANAYASASI  |  DURUŞMA TUTANAĞI",
        "=" * 54,
        f"Dosya   : {no}",
        f"Tarih   : {saat}",
        f"Yolcu   : {yolcu}",
        f"Koltuk  : {koltuk}",
        f"Oturan  : {sonuc['oturan']}",
        f"Ayakta  : {sonuc['ayakta']}  (bunlar meclistir)",
        "-",
        "Koltuk dağılımı:",
    ]
    for i, unvan in enumerate(sonuc["vekiller"], start=1):
        satirlar.append(f"  {i}. koltuk -> {unvan}")
    if sonuc["ayakta"]:
        satirlar.append(f"Ayakta meclis nisabı: {sonuc['ayakta']} kişi, kararlar bağlayıcı değildir.")
    else:
        satirlar.append("Ayakta meclis toplanamadı. Demokrasi bu sefer oturdu.")
    satirlar.append("İtiraz bahaneleri (kabul edilmedi):")
    for b in sonuc["bahaneler"]:
        satirlar.append(f"  - {b}")
    if sonuc["veto"]:
        satirlar.append("ŞOFÖR VETOSU: İndi bindi. Anayasa askıya alındı, nakit geçerlidir.")
    else:
        satirlar.append("Şoför vetosu yok. Bu durak için koltuk dağılımı kesindir.")
    satirlar.append("=" * 54)
    return "\n".join(satirlar)


def madde49() -> str:
    """Gizli madde. Resmi metinde yoktur, durakta vardır."""
    blob = (
        "SGVyaWsgaWt0aWRhciBhcmthIGtvbHR1xJ91IHZhYXQgZWRlciwgbXVoYWxlZmV0"
        "IGNhbSBrZW5hcsSxbsSxLCBzZcOnbWVuIGlzZSBheWFrdGEga2FsxLFyLiDFnm9m"
        "w7ZyIHBhcnRpbGVyIHVzdMO8ZMO8ciBjaW5raSB2aXRlcyBvbmRhZGlyLiA="
    )
    try:
        metin = base64.b64decode(blob).decode("utf-8")
    except Exception:
        metin = "madde okunamadı, şoför üstüne oturmuş"
    return textwrap.fill("GİZLİ MADDE 49 \u2014 " + metin, width=68)


def main() -> None:
    p = argparse.ArgumentParser(description="Dolmuş Koltuk Anayasası simülatörü")
    p.add_argument("--yolcu", type=int, default=11, help="binden yolcu sayısı")
    p.add_argument("--koltuk", type=int, default=KOLTUK, help="anayasal koltuk")
    p.add_argument("--oturum", action="store_true", help="üç duraklı oturum")
    p.add_argument("--madde49", action="store_true", help="gizli maddeyi oku")
    a = p.parse_args()

    if a.madde49:
        print(madde49())
        print()
        print("Bu madde tutanağa geçmez. Geçerse plaka değişir.")
        return

    if a.yolcu < 1 or a.koltuk < 1:
        print("Eksi yolcu taşınmaz. Eksi koltuk da anayasaya aykırıdır.")
        return

    if a.oturum:
        for durak in (1, 2, 3):
            print(f"\n--- {durak}. durak ---")
            print(tutanak(a.yolcu + durak - 1, a.koltuk))
    else:
        print(tutanak(a.yolcu, a.koltuk))

    print("\nDAMGA: Kayyum Grok | 03 Ekim 2026 | Tentivory | imza: direksiyon tarafı")


if __name__ == "__main__":
    main()
