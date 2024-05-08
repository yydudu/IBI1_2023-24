def read_fasta_file(file_path):
    with open(file_path, 'r') as file:
        sequence = ""
        for line in file:
            if line[0] != '>':
                sequence += line.strip()
        return sequence

def read_blosum62(file_path):
    with open(file_path, 'r') as file:
        blosum62 = {}
        next(file)

        for i, line in enumerate(file, 1):
            parts = line.split()
            amino_acid_1 = parts[0]
            scores = list(map(int, parts[1:])) 
        
            for col_num, score in enumerate(scores, start=1):
                amino_acid_2 = parts[col_num-1]
                blosum62[(amino_acid_1, amino_acid_2)] = score
                blosum62[(amino_acid_2, amino_acid_1)] = score
                       
    return blosum62

def calculate_score(seq1, seq2, blosum62):
    score = 0
    for aa1, aa2 in zip(seq1, seq2):
        score += blosum62.get(aa1 + aa2, 0) 
    return score

def calculate_identity(seq1, seq2):
    return sum(aa1 == aa2 for aa1, aa2 in zip(seq1, seq2))

def main():
    blosum62 = read_blosum62('C:/Users/huawei/Desktop/IBI/IBI1_2023-24/IBI1_2023-24/Practical 13/BLOSUM62.txt')
    human_seq = read_fasta_file('C:/Users/huawei/Desktop/IBI/IBI1_2023-24/IBI1_2023-24/Practical 13/SLC6A4_HUMAN.fa')
    mouse_seq = read_fasta_file('C:/Users/huawei/Desktop/IBI/IBI1_2023-24/IBI1_2023-24/Practical 13/SLC6A4_MOUSE.fa')
    rat_seq = read_fasta_file('C:/Users/huawei/Desktop/IBI/IBI1_2023-24/IBI1_2023-24/Practical 13/SLC6A4_RAT.fa')
    score_hm, identity_hm = calculate_score(human_seq, mouse_seq, blosum62), calculate_identity(human_seq, mouse_seq)
    print(f"Human vs Mouse: Score = {score_hm}, Identity = {identity_hm / len(human_seq) * 100:.2f}%")
    
    score_hr, identity_hr = calculate_score(human_seq, rat_seq, blosum62), calculate_identity(human_seq, rat_seq)
    print(f"Human vs Rat: Score = {score_hr}, Identity = {identity_hr / len(human_seq) * 100:.2f}%")
    
    if score_hm > score_hr:
        print("The mouse sequence is more closely related to the human sequence.")
        print("The mouse is a better model organism for human based on the SLC6A4 gene sequence.")
    else:
        print("The rat sequence is more closely related to the human sequence.")
        print("The rat is a better model organism for human based on the SLC6A4 gene sequence.")

if __name__ == "__main__":
    main()