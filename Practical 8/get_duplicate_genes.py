import re
input_file='C:/Users/huawei/Desktop/IBI/IBI1_2023-24/IBI1_2023-24/Practical 8/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'
output_file='C:/Users/huawei/Desktop/IBI/IBI1_2023-24/IBI1_2023-24/Practical 8/duplicate_genes.fa'

def duplication(inputfile,outputfile):
    with open(inputfile,'r') as fasta_file:
        with open(outputfile,'w') as output_fasta:
            sequence=[]
            gene_written=False 
            for line in fasta_file:
                if line.startswith('>'):
                    if sequence and gene_written:
                        output_fasta.write(''.join(sequence)+'\n')
                        sequence=[]
                    gene_written=False
                    if 'duplication' in line:
                        genename_match=re.search(r'gene:(\w+)',line)
                        if genename_match:
                            output_fasta.write(f'>{genename_match.group(1)}\n')
                            gene_written=True
                else:
                    sequence.append(line.strip())

            if sequence and gene_written:
                output_fasta.write(''.join(sequence)+'\n')

duplication(input_file,output_file)
