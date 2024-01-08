from pprint import pprint

protein_types = [
    'Methionine',
    'Phenylalanine',
    'Leucine',
    'Serine',
    'Tyrosine',
    'Cysteine',
    'Tryptophan',
    'STOP',]

codons = [
    'AUG',
    'UUU, UUC',
    'UUA, UUG',
    'UCU, UCC, UCA, UCG',
    'UAU, UAC',
    'UGU, UGC',
    'UGG',
    'UAA, UAG, UGA',]

def construct_protein_codon_pairs():
    protein_codon_pairs = {}
    for codon, protein in zip(codons, protein_types):
        split_codons = codon.split(',')
        for split_codon in split_codons:
            protein_codon_pairs[split_codon.strip()] = protein
    return protein_codon_pairs

def proteins(strand):
    pairs = construct_protein_codon_pairs()
    proteins = []
    for codon_idx in range(0, len(strand), 3):
        current = pairs[strand[codon_idx:codon_idx+3]]
        if current == 'STOP':
            break
        proteins.append(current)
    return proteins

if __name__ == '__main__':
    value = "UGGUGUUAUUAAUGGUUU"
    expected = ["Tryptophan", "Cysteine", "Tyrosine"]
    print(proteins(value))
    print(expected)