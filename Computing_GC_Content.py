# https://rosalind.info/problems/gc/


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

gc_maper = {}

for key in data.keys():
    gc_maper[key]  = (data[key].count('C') + data[key].count('G'))/len(data[key])

key = max(gc_maper,key=gc_maper.get)
gc_rate = gc_maper[key]* 100

print(key.replace('>',''))
print(f'{gc_rate:.6f}')
