# liste wird fuer die bewertung der eingabe verwendet
QualitaetsListe = ["A", "G", "C", "T", "_", " "]
# erstellung eines dictionary zur beurteilung der jeweiligen alignments bzw.
# ihrer konkatinierten strings der sequenzen an der postion [index]. Die
# jeweiligen Keys sind die letztendliche bewertung. die values sind listen
# an dessen einzelnen index positionen, die zugehoerigen Alignments bzw.
# mutationen sind. Es wird ein dictionary verwendet, damit das programm
# erweiterbar ist
QualitaetsDictionary = \
    {
        "|": ["AA", "GG", "CC", "TT"],
        ":": ["CT", "TC", "AG", "GA"],
        ".": ["CA", "AC", "CG", "GC", "TA", "AT", "TG", "GT"],
        " ": ["A_", "_A", "G_", "_G", "C_", "_C", "T_", "_T", "__"]
     }

# zur beurteilung von zwei sequenzen (seq1 und seq2), konkatiniere man hier
# die einzelnen strings an jeder position. Die Ergebnisse werden anschließend
# in einer liste gespeichert. die am Ende der Funktion ausgegeben wird, um
# sie in der alignment_bewertung() verwenden zu koennen.
# concat pair = seq1[0] + seq2[0]
# funktion konkatiniert die einzelnen positionen der strings, zu einem
# stringpaerchen, damit sie im anschluss mit der qalitaetsliste verglichen
# werden koennen
# INPUT: str1(), str2()
# OUTPUT: list
def concat_sequnces_in_string(seq1, seq2):
    string_seq1 = seq1
    string_seq2 = seq2

    ################## hier noch try except blöcke einarbeiten #############
    if len(string_seq1) != len(string_seq2):
        print("Strings sind nicht gleich lang.")
    else:
        concat_list = []
        index = 0
        concat_pair = ""
        while index < len(string_seq1) and index < len(string_seq2):
                for _ in string_seq1:
                    if string_seq1[index] in QualitaetsListe and string_seq2[index] in QualitaetsListe:
                        concat_pair = string_seq1[index] + string_seq2[index]
                        concat_list.append(concat_pair)
                        index += 1
                    else:
                        print("Wrong input. Sequence pair is removed")
                        # TODO: try except block
                        index += 1
                        continue
        # print(concat_list) ####TEST####
        return concat_list

# diese funktion vergleicht die eingespeicherten werte in der liste der
# sequenzen aus concat_sequences_in_list() mit den werten aus dem
# QualitaetsDictionary und gibt deren zugehoerigen key in einen string zurueck
# INPUT: str1(), str2()
# OUTPUT: str
def alignment_eval(seq1, seq2):
    concat_list = []

    # damit die konkatinierte liste in einer variablen gespeichert wird und
    # hier an dieser stelle einfacher verwendet werden kann
    concat_list = concat_sequnces_in_string(seq1,
                                          seq2)
    index = 0
    value = None
    evaluate_string = ""
    # erzeugt ein tuple aller items in Qualitaetsdictionary
    sorted_dict = sorted(QualitaetsDictionary.items())
    print(sorted_dict)

    for value in concat_list:
        # value speichert den jeweiligen concatinierten
        # string der seq1 und seq2, um diesen mit
        # der QulitaetsDictionary vergleichen zu koennen
            for index in range(0, len(sorted_dict), 1):
                # for-schleife iteriert ueber die gesamte laenge des sortierten
                # dictionaries
                for dict_val in sorted_dict[index][1]:
                    if value == dict_val:
                        evaluate_string += sorted_dict[index][0]
                    elif value not in sorted_dict:
                        evaluate_string += "#"
    return evaluate_string


# diese funktion druckt die einzelnen sequenzen wieder aus und fuegt die
# bewertungen zwischen jedem vorher bewerteten stringpaerchen aus
# INPUT: str1(), str2()
# OUTPUT: None
def print_alignment(seq1, seq2):
    evaluation = alignment_eval(seq1, seq2)
    # evaluation = alignment_bewertung(seq1,seq2)

    print(seq1)
    print(evaluation)
    print(seq2)

# die einzelnen sequenzen muessen hier wieder getrennt werden ODER
# sie muessen von anderen funktionen uebergeben werden


# Liste zur Kontrolle ob eine Aminosäuresequenz eingegeben wurde

if __name__ == "__main__":
    seq1 = "ATCG"
    seq2 = "AGSG"
    print_alignment(seq1, seq2)
    seq1 = "ATT"
    seq2 = "ATG"
    print_alignment(seq1, seq2)