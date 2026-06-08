# EgehanMSA
Biyoinformatik Final Projesi - Çoklu Dizi Hizalaması (MSA)

Bu kütüphane, biyolojik dizilerin (DNA/Protein) çoklu hizalamasını gerçekleştirmek amacıyla **Dinamik Programlama** (Needleman-Wunsch) kullanılarak geliştirilmiştir.

## Kurulum
Terminalinize aşağıdaki komutu yazarak kütüphaneyi doğrudan bilgisayarınıza kurabilirsiniz:
```bash
pip install git+https://github.com/saikyo4/EgehanMSA.git
import egehanmsa

aligner = egehanmsa.AlignerDP()

dizi1, dizi2 = aligner.pairwise_align("ATCG", "TCCG")
print("Hizalanmış 1:", dizi1)
print("Hizalanmış 2:", dizi2)

diziler = ["ATCGT", "TGGTG", "ATCT"]
coklu_sonuc = aligner.multiple_sequence_alignment(diziler)
print("Çoklu Hizalama:", coklu_sonuc)