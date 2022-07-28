# https://rosalind.info/problems/revp/
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


mapper = {
    'A':'T',
    'T':'A',
    'C':'G',
    'G':'C'
    }

data = read_fasta('f.fasta')
DNA = data[list(data.keys())[0]]


RDNA = "".join(map(lambda x: mapper[x], DNA))


for j in range(len(DNA)):
    for i in range(12,3,-1):
        if DNA[j:j+i][::-1] in RDNA[j:j+i] and len(DNA[j:j+i][::-1]) == i:
            print(j+1, i,sep="\t")
            break

