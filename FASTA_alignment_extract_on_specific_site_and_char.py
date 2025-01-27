#!/usr/bin/env python
# coding: utf-8

# Author: Cory Dunn
# Contact : cory.david.dunn@gmail.com
# Provided courtesy of GRO Biosciences

import numpy as np
from Bio import SeqIO
import argparse

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--input_file', required = True, type = str, help = 'Input alignment in FASTA format.\n')
ap.add_argument('-o', '--output_file', required = True, type = str, help = 'Output alignment in FASTA format.\n')
ap.add_argument('-l','--list_of_position_selections', nargs='+', type=str, help='List of position requirements for maintainance in output FASTA [eg. -l C348 T397].\n', required=True)

args = vars(ap.parse_args())

alignfile = args['input_file']
output_file = args['output_file']
selected_ID_list = args['list_of_position_selections']

ofile = open(output_file, 'w')

for record in SeqIO.parse(alignfile, 'fasta'):

    accession_name = str(record.name)
    accession_name_underscore = accession_name.replace(' ', '_')
    accession_sequence = list(record.seq)
    accession_sequence_NP = np.array(accession_sequence, dtype = 'str')
    write_flag = 1
    
    for amino_acid in selected_ID_list:
        character = amino_acid[0]
        site = int(amino_acid[1:])
        if accession_sequence_NP[int(site)-1] != character: 
            write_flag = 0
    
    if write_flag == 1:
        
        accession_sequence_back_to_str = accession_sequence_NP.astype('|S1').tobytes().decode('utf-8')
        ofile.write('>' + accession_name_underscore + '\n' + accession_sequence_back_to_str + '\n')
        
ofile.close()
