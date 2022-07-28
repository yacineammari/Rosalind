# https://rosalind.info/problems/orf/

mapper = {
'UUU' : 'F'   ,'CUU' : 'L', 'AUU' : 'I', 'GUU' : 'V',
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
'UGG' : 'W'   ,'CGG' : 'R', 'AGG' : 'R', 'GGG' : 'G'}

mappers = {
    'A':'T',
    'T':'A',
    'C':'G',
    'G':'C'
    }

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


data = read_fasta('f.fasta')

DNA = data[list(data.keys())[0]]
RNA = DNA.replace('T','U')
RNA_starts = [i for i in range(len(RNA)) if RNA.startswith('AUG', i)]


RDNA = "".join(map(lambda x: mappers[x], DNA))[::-1]
RRNA = RDNA.replace('T','U')
RRNA_starts = [i for i in range(len(RRNA)) if RRNA.startswith('AUG', i)]

prot_list = []

for i in RNA_starts:
    prot = ''
    j = i
    while j < len(RNA):
        try:
            if mapper[RNA[j:j+3]] == 'Stop':
                prot_list.append(prot)
                prot = ''
                break
            else:
                prot += mapper[RNA[j:j+3]]
        except:
            pass
        j = j + 3

for i in RRNA_starts:
    prot = ''
    j = i
    while j < len(RRNA):
        try:
            if mapper[RRNA[j:j+3]] == 'Stop':
                prot_list.append(prot)
                prot = ''
                break
            else:
                prot += mapper[RRNA[j:j+3]]
        except:
            pass
        j = j + 3



prot_list = list(set(prot_list))

for p in prot_list:
    print(p)





