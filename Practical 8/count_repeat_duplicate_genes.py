import re
import os
repeat_sequence=input("enter one of the two repetitive sequences (GTGTGT or GTCTGT)")
if repeat_sequence not in ['GTGTGT','GTCTGT']:
    print('please enter GTGTGT or GTCTGT')
    exit()

output_file=f'{repeat_sequence}_duplicate_genes.fa'
output_directory='C:/Users/huawei/Desktop/IBI/IBI1_2023-24/IBI1_2023-24/Practical 8'
output_file=os.path.join(output_directory,f'{repeat_sequence}_duplicate_genes.fa')

input_file='C:/Users/huawei/Desktop/IBI/IBI1_2023-24/IBI1_2023-24/Practical 8/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'

def find_duplicate_genes(input_file, output_file, repeat_sequence):
    with open(input_file, 'r') as fasta_file, open(output_file, 'w') as output_fasta:
        sequence_lines =[]
        gene_name_line=''

        for line in fasta_file:
            if line.startswith('>'):
                if 'duplication' in gene_name_line and any(repeat_sequence in seq for seq in sequence_lines):
                    output_fasta.write(gene_name_line)
                    output_fasta.write(''.join(sequence_lines)+'\n')
                gene_name_line=line
                sequence_lines=[]
            else:
                sequence_lines.append(line.strip())  
        if 'duplication' in gene_name_line and any(repeat_sequence in seq for seq in sequence_lines):
            output_fasta.write(gene_name_line)
            output_fasta.write(''.join(sequence_lines)+'\n')
           
find_duplicate_genes(input_file,output_file,repeat_sequence)