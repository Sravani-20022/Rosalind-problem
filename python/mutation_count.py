#take two variable to store the sequences
dna_seq1 = input("Enter DNA Sequence1:")
dna_seq2 = input("Enter DNA Sequence2:")
count = 0
for i in range(len(dna_seq1)):
    if dna_seq1[i] != dna_seq2[i]:
        count += 1
print(count)
    
