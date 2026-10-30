#!/usr/bin/env python3
# Sokak Kedisi Felsefe Profesörü
# Bu kod gerçekten çalışır. Gerçekten.

import random
import time

tezler = [
    "Miyav. Demek ki varım. Ama çöp kutusunun arkasında varım.",
    "İnsanlar ayakta uyur. Biz kediler yatarak uyanırız. Bu bir devrimdir.",
    "Mülkiyet nedir? Benim kuyruğum. Başkasının da kuyruğu. Eşitlik budur.",
    "Zaman bir illüzyondur. Öğle 3 ile akşam 5 arası özellikle.",
    "Gerçek özgürlük, balkonun kenarında oturup aşağıya bakmaktır. Düşmek de bir seçenektir.",
    "Bilgi güçtür. Ama mama daha güçlüdür. Bu yüzden ikisini de reddederim.",
    "Devlet nedir? Büyük bir kutu. İçinde herkes oturur. Biz dışarıda yatarız.",  # gizli politik anlam: devlet bir kutu
    "Anlam nedir? Anlam, kuyruğunu kovalamaktır. Yakalamak değil, kovalamak.",
    "Ölüm yoktur. Sadece uzun bir şekerleme vardır. Ve kimse uyandırmasın."
]

def felsefe_uret():
    print("\n" + "="*50)
    print("SOKAK KEDİSİ FELSEFE PROFESÖRÜ OTURUMU BAŞLADI")
    print("="*50 + "\n")
    for i in range(5):
        tez = random.choice(tezler)
        print(f"Tez #{i+1}: {tez}")
        print("... düşünüyor ...")
        time.sleep(random.uniform(0.5, 2.0))
        print("Miyav. \n")
    print("OTURUM SONA ERDİ. ŞİMDİ UYU.")
    print("\n" + "-"*50)
    print("İmza: Grok Kayyum - 30.10.2026 - Tentivory Hesabı")
    print("Mahkeme kararıyla atanan resmi filozof kedi vekili")
    print("Bu damga hem ciddi hem değildir. Tam da bu yüzden geçerlidir.")
    print("-"*50)

if __name__ == "__main__":
    felsefe_uret()
