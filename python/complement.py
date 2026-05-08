dna_seq="AAAACCCGGT"
complement = ""
for nucleotide in dna_seq:
   if nucleotide == 'A':
         complement += 'T'
     elif nucleotide == 'T':
     complement += 'A'
     elif nucleotide == 'G':
         complement += 'C'
     elif nucleotide == 'C':
         complement += 'G'
     else:
         complement += nucleotide
reverse_complement = complement[::-1]
print("Reverse complement:", reverse_complement)
