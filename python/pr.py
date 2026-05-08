# Simple RNA to Protein conversion

# Minimal codon table
codon_table = {
    'AUG': 'M',
    'UUU': 'F', 'UUC': 'F',
    'UAA': 'STOP', 'UAG': 'STOP', 'UGA': 'STOP'
}

rna = input("Enter RNA sequence: ").upper()

# Split into codons
codons = [rna[i:i+3] for i in range(0, len(rna), 3)]

protein = ""

for codon in codons:
    if len(codon) < 3:
        break
    amino = codon_table.get(codon, '?')
    if amino == 'STOP':
        break
    protein += amino

print("Protein:", protein)
