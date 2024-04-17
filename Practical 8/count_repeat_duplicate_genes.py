import re
import os
repeat_sequence=input("enter one of the two repetitive sequences (GTGTGT or GTCTGT)")
if repeat_sequence not in ['GTGTGT','GTCTGT']:
    print('please enter GTGTGT or GTCTGT')
    exit()


output_directory='C:/Users/huawei/Desktop/IBI/IBI1_2023-24/IBI1_2023-24/Practical 8'
output_file=os.path.join(output_directory,f'{repeat_sequence}_duplicate_genes.fa')
input_file='C:/Users/huawei/Desktop/IBI/IBI1_2023-24/IBI1_2023-24/Practical 8/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'

def find_duplicate_genes(input_file, output_file, repeat_sequence):
    pattern=re.compile(repeat_sequence)
    with open(input_file, 'r') as fasta_file, open(output_file, 'w') as output_fasta:
        sequence_lines =[]
        gene_name_line=''

        for line in fasta_file:
            if line.startswith('>'):
                if 'duplication' in gene_name_line :
                    full_sequence=''.join(sequence_lines)
                    count_repeats=len(pattern.findall(full_sequence))
                    if count_repeats>0:
                        gene_name=re.search(r'gene:(\w+)',gene_name_line).group(1)
                        output_fasta.write(f'>{gene_name}|count of {repeat_sequence}:{count_repeats}\n')
                        output_fasta.write(full_sequence+'\n')
                gene_name_line=line
                sequence_lines=[]
            else:
                sequence_lines.append(line.strip())  
        if 'duplication' in gene_name_line:
            full_sequence=''.join(sequence_lines)
            count_repeats=len(pattern.findall(full_sequence))
            if count_repeats>0:
                gene_name = re.search(r'gene:(\w+)', gene_name_line).group(1)
                output_fasta.write(f'>{gene_name} | Count of {repeat_sequence}: {count_repeats}\n')
                output_fasta.write(full_sequence + '\n')
           
find_duplicate_genes(input_file,output_file,repeat_sequence)