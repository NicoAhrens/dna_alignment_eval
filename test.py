
### Different tests for showAlignment() ###

import main

seq1 = 'AGTCAAT'
seq2 = 'AGTCAAT'
main.showAlignment(seq1, seq2)
seq1 = 'AAAAAA'
seq2 = 'AAAAAA'
main.showAlignment(seq1, seq2)
seq1 = '_AAAAA'
seq2 = 'AAAAAA'
main.showAlignment(seq1, seq2)
seq1 = 'AGTCTA'
seq2 = 'GTCGAC'
main.showAlignment(seq1, seq2)
seq1 = 'TTCGZU'
seq2 = 'TCSGTS'
main.showAlignment(seq1, seq2)
seq1 = 'ATTa'
seq2 = 'ATGA'
main.showAlignment(seq1, seq2)
seq1 = 'AT T'
seq2 = 'AT G'
main.showAlignment(seq1, seq2)
seq1 = '___'
seq2 = '___'
main.showAlignment(seq1, seq2)
seq1 = 'ATTTTTTTTTTTTGGGGGGGGtgtgat'
seq2 = 'ATGGGGGGGGGTTTTTTTTTTg'
main.showAlignment(seq1, seq2)
seq1 = '123'
seq2 = '456'
main.showAlignment(seq1, seq2)
seq1 = '#+??ß'
seq2 = '#+??ß'
main.showAlignment(seq1, seq2)