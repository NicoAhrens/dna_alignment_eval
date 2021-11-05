
### Program for the evaluation of the alignment of two dna sequences ####
# This program gets two sequences as an input and calculates the alignment of
# the two corresponding nucleotides at the given position. In the end
# it prints out the two sequences and in between the line of evaluations
# of every pair.

# Evaluations of nucleotide pairing and there meaning:
# "|" -> exact match
# ":" -> a good match
# "." -> a bad match
# " " -> nucleotide with gap aligned

# Creates a dictionary for the evaluation of the match of two dna sequences.
# The keys are the evaluation of the matching pairs of the two dna sequences.
# the corresponding values lists into which the corresponding pairs for the
# evaluation are written. So the string "AA" has the corresponding key
# "|". The dictionary is saved in a global valuable, because then it does not
# need to be created every time a combination of sequences needs to be
# evaluated.
QualityDictionary = \
    {
        "|": ["AA", "GG", "CC", "TT"],
        ":": ["CT", "TC", "AG", "GA"],
        ".": ["CA", "AC", "CG", "GC", "TA", "AT", "TG", "GT"],
        " ": ["A_", "_A", "G_", "_G", "C_", "_C", "T_", "_T", "__", "  "]
     }


# This function concatenates every character in the string from one sequence
# with the corresponding (same position, index) of the other sequence.
# these pairs are saved in a list. The function returns the whole list to
# use it in the other functions.
# INPUT: str seq1, str seq2
# OUTPUT: list
def concat_sequnces_in_string(seq1, seq2):
    ###print('This is sequence 1:', seq1)
    ###print('This is the class of sequence 1:', type(seq1))
    string_seq1 = seq1.upper()
    string_seq2 = seq2.upper()
    concat_list = []
    index = 0
    concat_pair = ''

    # The try and except blocks are for the case, when a string is longer
    # then the other. Normally an IndexError would occur, when it does
    # the function just prints out that the two strings do not have the same
    # length and then continues to concatenate other input sequences. It also
    # concatenates to the point when the IndexError is raised. The assumption
    # is that when the user puts in the two sequences, he maybe types in a
    # wrong character at the end or did not copy the whole sequence.
    try:
        while index < len(string_seq1) and index < len(string_seq2):

            for nucleotide in string_seq1:
                concat_pair = string_seq1[index] + string_seq2[index]
                concat_list.append(concat_pair)
                index += 1

    except IndexError:
        print(string_seq1, ' and')
        print(string_seq2, ' :')
    return concat_list

# This function takes the actual string pairs from concat_sequences_in_string()
# and saves it into a variable (concat_list). It then compares every pair of
# string in the concat_list with the pairs in the dictionary QualityDictionary.
# It saves the wrong inputs in a list, to print them out later and point out
# where the positions of the wrong inputs are.
# When the input is correct it then saves the evaluation of the string pair in
# a string and returns this string of only evaluations.
# INPUT: str seq1, str seq2
# OUTPUT: str
def alignmentEval(seq1, seq2):
    concat_list = []

    concat_list = concat_sequnces_in_string(seq1, seq2)
    index = 0
    evaluate_string = ''

    # creates tuple of all items in QualityDictionary in reverse order, for
    # the later iteration

    sorted_dict = sorted(QualityDictionary.items(), reverse = True)
    #print(sorted_dict)
    wrong_inputs = []
    merged_dictionary_values = \
        [
         'AA', 'GG', 'CC', 'TT', 'CT', 'TC', 'AG', 'GA','CA', 'AC', 'CG', 'GC',
         'TA', 'AT', 'TG', 'GT', 'A_', '_A', 'G_', '_G', 'C_', '_C', 'T_',
         '_T', '__', '  '
         ]
    # seq1_seq2_pair is the variable to iterate over in the loop.
    # it uses each concatenated pair from the concat_list to iterate
    # over

    for seq1_seq2_pair in concat_list:
        ###print('Pair: ', seq1_seq2_pair)

        # this if-query creates a list of wrong inputs, when
        # the seq1_seq2_pair is not in the merged_dictionary_values and
        # puts a # on this position to track the wrong input

        if seq1_seq2_pair not in merged_dictionary_values:
            ###print('Pair: ', seq1_seq2_pair)
            ####print('QualityValue: ', merged_dictionary_values)
            evaluate_string += '#'
            wrong_inputs.append('Character combination {}is not allowed. '\
                                'Printed out "#" as placeholder.'\
                                .format(seq1_seq2_pair))
        else:

            # This for-loop is for the iteration over the QualityDictionary
            # which was sorted for easier iteration over it.

            for index in range(0, len(sorted_dict), 1):
                #print(sorted_dict[index][1])

                # This for-loop appends the different evaluations for each
                # concat pair of nucleotides into a string. This string
                # is returned in the end to use in it in showAlignment
                for dict_val in sorted_dict[index][1]:
                    if seq1_seq2_pair == dict_val:
                        evaluate_string += sorted_dict[index][0]

    for index in wrong_inputs:
        print([index][0])

    return evaluate_string
# This function prints out each dna sequence and in between it prints out
# the match evaluation. If the sequences do not have the same length it prints
# out this information for the user.
# INPUT: str seq1, str seq2
# OUTPUT: None
def showAlignment(seq1, seq2):
    evaluation = alignmentEval(seq1, seq2)
    if len(seq1) == len(seq2):
        print('Alignment Evaluation:')
        print(len(seq1)* '~')
        print(seq1)
        print(evaluation)
        print(seq2)
        print(len(seq1) * '~')
    else:
        print('Did not align sequences, because they are not the same length')

if __name__ == '__main__':
