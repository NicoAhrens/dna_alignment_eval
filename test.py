
# ~~~ Different tests for show_alignment() ~~~ #

import main

seq1 = 'AGTCAAT'
seq2 = 'AGTCAAT'
main.show_alignment(seq1, seq2)
seq1 = 'AAAAAA'
seq2 = 'AAAAAA'
main.show_alignment(seq1, seq2)
seq1 = '_AAAAA'
seq2 = 'AAAAAA'
main.show_alignment(seq1, seq2)
seq1 = 'AGTCTA'
seq2 = 'GTCGAC'
main.show_alignment(seq1, seq2)
seq1 = 'TTCGZU'
seq2 = 'TCSGTS'
main.show_alignment(seq1, seq2)
seq1 = 'ATTa'
seq2 = 'ATGA'
main.show_alignment(seq1, seq2)
seq1 = 'AT T'
seq2 = 'AT G'
main.show_alignment(seq1, seq2)
seq1 = 'AT_T__AGTC'
seq2 = 'AT_G_AATGC'
main.show_alignment(seq1, seq2)
seq1 = '___'
seq2 = '___'
main.show_alignment(seq1, seq2)
seq1 = 'ATTTTTTTTTTTTGGGGGGGGtgtgat'
seq2 = 'ATGGGGGGGGGTTTTTTTTTTg'
main.show_alignment(seq1, seq2)
seq1 = '123'
seq2 = '456'
main.show_alignment(seq1, seq2)
seq1 = '#+??ß'
seq2 = '#+??ß'
main.show_alignment(seq1, seq2)
