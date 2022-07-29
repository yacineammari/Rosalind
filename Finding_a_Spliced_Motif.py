# https://rosalind.info/problems/sseq/

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

DNA1 = list(data.values())[0]
DNA2 = list(data.values())[1]

pos = []
i = 0

for char in DNA2:
    try:
        while DNA1[i] != char:
            i += 1
        pos.append(str(i+1))
        i += 1
    except:
        pass


print(*pos, sep=' ')

