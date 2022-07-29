# https://rosalind.info/problems/splc/

def read_fasta(fasta_file):
    # read fasta file
    # this function return a dictionary
    with open(fasta_file, 'r') as f:
        data = {}
        ind = ""
        adn = ""
        for line in f:
            if line[0] == ">":
                if len(adn) > 1 and len(ind) > 1:
                    data[ind] = adn
                ind = line.strip()
                adn = ""
            else:
                adn = adn + line.strip()
        else:
            data[ind] = adn
    return data

mapper = {'UUU' : 'F'   ,'CUU' : 'L', 'AUU' : 'I', 'GUU' : 'V',
'UUC' : 'F'   ,'CUC' : 'L', 'AUC' : 'I', 'GUC' : 'V',
'UUA' : 'L'   ,'CUA' : 'L', 'AUA' : 'I', 'GUA' : 'V',
'UUG' : 'L'   ,'CUG' : 'L', 'AUG' : 'M', 'GUG' : 'V',
'UCU' : 'S'   ,'CCU' : 'P', 'ACU' : 'T', 'GCU' : 'A',
'UCC' : 'S'   ,'CCC' : 'P', 'ACC' : 'T', 'GCC' : 'A',
'UCA' : 'S'   ,'CCA' : 'P', 'ACA' : 'T', 'GCA' : 'A',
'UCG' : 'S'   ,'CCG' : 'P', 'ACG' : 'T', 'GCG' : 'A',
'UAU' : 'Y'   ,'CAU' : 'H', 'AAU' : 'N', 'GAU' : 'D',
'UAC' : 'Y'   ,'CAC' : 'H', 'AAC' : 'N', 'GAC' : 'D',
'UAA' : 'Stop','CAA' : 'Q', 'AAA' : 'K', 'GAA' : 'E',
'UAG' : 'Stop','CAG' : 'Q', 'AAG' : 'K', 'GAG' : 'E',
'UGU' : 'C'   ,'CGU' : 'R', 'AGU' : 'S', 'GGU' : 'G',
'UGC' : 'C'   ,'CGC' : 'R', 'AGC' : 'S', 'GGC' : 'G',
'UGA' : 'Stop','CGA' : 'R', 'AGA' : 'R', 'GGA' : 'G',
'UGG' : 'W'   ,'CGG' : 'R', 'AGG' : 'R', 'GGG' : 'G',}

data = read_fasta('f.fasta')


DNA = list(data.values())[0]

introns = list(data.values())[1::]

for i in introns:
    DNA = DNA.replace(i,'')

RNA = DNA.replace('T','U')


prot = ''
i = 0
while i < len(RNA):
    try:
        if mapper[RNA[i:i+3]] == 'Stop':
            break
        else:
            prot += mapper[RNA[i:i+3]]
    except:
        pass
    i = i +3

print(prot)


