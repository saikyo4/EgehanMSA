import numpy as np

class AlignerDP:
    def __init__(self, match_score=1, mismatch_score=-1, gap_penalty=-2):
        self.match = match_score
        self.mismatch = mismatch_score
        self.gap = gap_penalty

    def pairwise_align(self, seq1, seq2):
        # 1. Matrisleri Oluşturma
        m, n = len(seq1), len(seq2)
        score_matrix = np.zeros((m + 1, n + 1))
        
        for i in range(m + 1):
            score_matrix[i][0] = self.gap * i
        for j in range(n + 1):
            score_matrix[0][j] = self.gap * j

        # 2. Matrisi Doldurma
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                match = score_matrix[i - 1][j - 1] + (self.match if seq1[i - 1] == seq2[j - 1] else self.mismatch)
                delete = score_matrix[i - 1][j] + self.gap
                insert = score_matrix[i][j - 1] + self.gap
                score_matrix[i][j] = max(match, delete, insert)

        # 3. Hizalama bulma
        aligned_seq1, aligned_seq2 = "", ""
        i, j = m, n
        while i > 0 and j > 0:
            current_score = score_matrix[i][j]
            diagonal_score = score_matrix[i - 1][j - 1]
            up_score = score_matrix[i - 1][j]
            left_score = score_matrix[i][j - 1]

            if current_score == diagonal_score + (self.match if seq1[i - 1] == seq2[j - 1] else self.mismatch):
                aligned_seq1 += seq1[i - 1]
                aligned_seq2 += seq2[j - 1]
                i -= 1
                j -= 1
            elif current_score == up_score + self.gap:
                aligned_seq1 += seq1[i - 1]
                aligned_seq2 += "-"
                i -= 1
            else:
                aligned_seq1 += "-"
                aligned_seq2 += seq2[j - 1]
                j -= 1

        while i > 0:
            aligned_seq1 += seq1[i - 1]
            aligned_seq2 += "-"
            i -= 1
        while j > 0:
            aligned_seq1 += "-"
            aligned_seq2 += seq2[j - 1]
            j -= 1

        return aligned_seq1[::-1], aligned_seq2[::-1]

    def multiple_sequence_alignment(self, sequences):
        # Dizileri birleştirme
        if not sequences:
            return []
        
        base_seq = sequences[0]
        aligned_results = [base_seq]

        for i in range(1, len(sequences)):
            base_seq, new_aligned = self.pairwise_align(base_seq.replace("-", ""), sequences[i])
            aligned_results.append(new_aligned)
            
            # Güncelleme
            for j in range(len(aligned_results) - 1):
                updated_seq = ""
                idx = 0
                for char in base_seq:
                    if char == "-":
                        updated_seq += "-"
                    else:
                        updated_seq += aligned_results[j][idx] if idx < len(aligned_results[j]) else "-"
                        idx += 1
                aligned_results[j] = updated_seq

        aligned_results[-1] = base_seq
        return aligned_results