FASTA_alignment_extract_on_specific_site_and_char

----

Author:

Cory Dunn
Contact: cory.david.dunn@gmail.com
Provided courtesy of GRO Biosciences

----

License:

GPLv3

----


This software selects entries from a multiple sequence alignment based upon the presence of specific characters at specific alignment columns and saves to a new FASTA file.

----

Requirements:

This script is implemented using Python 3 (current version tested under Python version 3.12.8) 

Dependencies: 

Biopython (tested under version 1.84),
Numpy (tested under version 2.1.3)

----

Usage: FASTA_alignment_extract_on_specific_site_and_char.py [-h] -i INPUT_FILE -o OUTPUT_FILE -l LIST_OF_POSITION_SELECTIONS [LIST_OF_POSITION_SELECTIONS ...]

  -i INPUT_FILE, --input_file

		Input alignment in FASTA format.

  -o OUTPUT_FILE, --output_file

		Output alignment in FASTA format.


  -l LIST_OF_POSITION_SELECTIONS, --list_of_position_selections

		List of position requirements for maintainance in output FASTA [eg. -l C348 T397].
