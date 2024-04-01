import re
input_file='C:/Users/huawei/Desktop/IBI/IBI1_2023-24/IBI1_2023-24/Practical 8/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'
output_file='C:/Users/huawei/Desktop/IBI/IBI1_2023-24/IBI1_2023-24/Practical 8/duplicate_genes.fa'

def duplication(inputfile,outputfile):
    with open(inputfile,'r') as fasta_file:
        with open(outputfile,'w') as output_fasta:
            sequence=[]
            genename=None
            for line in fasta_file:
                if line.startswith('>'):
                    if sequence and genename:
                        output_fasta.write(''.join(sequence)+'\n')
                        sequence=[]
                    if 'duplication' in line:
                        genename_match=re.search(r'>(\S+)',line)
                        if genename_match:
                            genename=genename_match.group(1)
                            output_fasta.write(f'>{genename}\n')
                    else:
                        genename=None
                elif genename:
                    sequence.append(line.strip())

            if sequence and genename:
                output_fasta.write(''.join(sequence)+'\n')

duplication(input_file,output_file)
