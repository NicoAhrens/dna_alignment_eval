# listen zur bewertung der sequenzen
QualitaetsListe = ["AA", "GG", "CC", "TT", "CT", "TC", "AG", "GA", "CA", "AC",
                   "CG", "GC", "TA", "AT", "TG", "GT"]
QualitaetsDictionary = {"|": ["AA", "GG", "CC", "TT"],
                        ":": ["CT", "TC", "AG", "GA"],
                        ".": ["CA", "AC", "CG", "GC", "TA", "AT", "TG", "GT"],
                        " ": ["A_", "_A", "G_", "_G", "C_", "_C", "T_", "_T",
                              "__"]}


# funktion konkatiniert die einzelnen positionen der strings, damit sie
# im anschluss mit der qalitaetsliste verglichen werden koennen
def concat_sequnces_in_list(seq1, seq2):
    string_seq1 = seq1
    string_seq2 = seq2
    concat_list = []
    index = 0
    concat_pair = ""
    while index < len(string_seq1) and len(string_seq2):
        for i in string_seq1:
            concat_pair = string_seq1[index] + string_seq2[index]
            concat_list.append(concat_pair)
            index += 1
    # print(concat_list) ####TEST####
    return concat_list


# hiermit wird die concatinierte liste der sequenzen mit den qualiteatsbe-
# wertungen verglichen
def alignment_bewertung(seq1, seq2):
    concat_list = []  # kann man vielleicht weglassen
    concat_list = concat_sequnces_in_list(seq1,
                                          seq2)
    # damit die konkatinierte # liste in einer variablen gespeichert wird und
    # hier an dieser stelle einfacher verwendet werden kann

    #print(concat_list)  ###TEST###
    index = 0
    index2 = 0
    value = None
    evaluate_list = ""
    sorted_dict = sorted(QualitaetsDictionary.items())
    # print(sorted_dict)

    for value in concat_list:
        # value speichert den jeweiligen concatinierten
        # string der seq1 und seq2, um diesen mit
        # der bewertungsliste vergleichen zu koennen
        for index in range(0, len(sorted_dict), 1):
            # for-schleife iteriert über die gesamte länge des sortierten
            # dictionaries
            for dict_val in sorted_dict[index][1]:
                #
                if value == dict_val:
                    evaluate_list += sorted_dict[index][0]

    return (evaluate_list)


# diese funktion druckt die einzelnen sequenzen wieder aus und fuegt die
# bewertungen ein
def print_alignment(seq1, seq2):
    evaluation = alignment_bewertung(seq1, seq2)
    # evaluation = alignment_bewertung(seq1,seq2)
    print(seq1)
    print(evaluation)
    print(seq2)


# die einzelnen sequenzen muessen hier wieder getrennt werden ODER
# sie muessen von anderen funktionen uebergeben werden


# Liste zur Kontrolle ob eine Aminosäuresequenz eingegeben wurde

if __name__ == "__main__":
    seq1 = "ATGC"
    seq2 = "ATCG"
    print_alignment(seq1, seq2)
    # ergebnis = alignment_bewertung(seq1,seq2)
    # print(ergebnis)
    # print_alignment(seq1,seq2)
