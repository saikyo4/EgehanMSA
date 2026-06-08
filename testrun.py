from egehanmsa.aligner import AlignerDP

def main():
    aligner = AlignerDP(match_score=1, mismatch_score=-1, gap_penalty=-2)

    print("=== İKİLİ HİZALAMA TESTİ ===")
    seq1 = "ATCGT"
    seq2 = "TGGTG"
    
    aligned_1, aligned_2 = aligner.pairwise_align(seq1, seq2)
    print(f"Orijinal Dizi 1: {seq1}")
    print(f"Orijinal Dizi 2: {seq2}")
    print(f"Hizalanmış Dizi 1: {aligned_1}")
    print(f"Hizalanmış Dizi 2: {aligned_2}\n")

    print("=== ÇOKLU HİZALAMA (MSA) TESTİ ===")
    sequences = [
        "ATCGT",
        "TGGTG",
        "ATCT",
        "TGCGT"
    ]
    
    msa_results = aligner.multiple_sequence_alignment(sequences)
    
    print("Orijinal Diziler:")
    for seq in sequences:
        print(f"- {seq}")
        
    print("\nHizalanmış Diziler:")
    for i, res in enumerate(msa_results):
        print(f"Dizi {i+1}: {res}")

if __name__ == "__main__":
    main()