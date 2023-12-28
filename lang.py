#!/usr/bin/env python
import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
""" 
    CS 401, Denison University
    Final Project [Abrham Negesh Gelan, Nuri Hyun, Anton Maninang]
        Multilingual NLP Analysis: Amharic, Korean, and Tagalog with English
    
    Analysis 01 - ANG → A comparative analysis of native English speakers with native 
    Amharic speaker in their English writings

    Author: Abrham Negash Gelan.
    Date:  11 December 2023
"""

#------------------------------ SENTENCE PARSING ------------------------------#
################################################################################
def generate_parsed(filename):
    """
    Purpose: Parses the given txt file into sentences using periods.
    Input: A txt file of an essay.
    Output: A file with lines of parsed sentences.
    Returns: Nothing
    """
    #Rename output file based on input
    output_filename = filename.split('.')[0] + '_parsed.txt'

    with open(filename, 'r', encoding='utf-8') as file:
        with open(output_filename, 'w', encoding='utf-8') as output_file:
            for line in file:
                # Parse using periods
                sentences = line.split('.')
                for sentence in sentences:
                    # Stripping whitespace adding a period back
                    cleaned_sentence = sentence.strip()
                    #If sentence valid (not empty), write to output file
                    if cleaned_sentence:
                        output_file.write(cleaned_sentence + '.' + '\n')
################################################################################

#------------------------------ POS TAGGING -----------------------------------#
################################################################################

def nltk_pos_tagging(filename):
    """
    Purpose: Word tokenization and POS tagging using NLTK package
    Input: A parsed txt file of an essay.
    Returns: A list of tuples, each containing a sentence and its POS-tagged words.
    """
    tagged_sentences = []
    with open(filename, 'r', encoding='utf-8') as file:
        for sentence in file:
            tokens = word_tokenize(sentence)
            tagged = pos_tag(tokens)
            tagged_sentences.append(tagged)
    #for i in range(min(5, len(tagged_sentences))):
            #print(tagged_sentences[i])
    return tagged_sentences
################################################################################

#---------------------------- ORDER IDENTIFIER --------------------------------#
################################################################################
def identify_order(tagged_sentences, output_file):
    """
    Purpose: Sentence identifier and structure counting
    Input: Output of pos_tagging.
    Returns: Computed analysis of SVO and SOV for a given txt file
    """
    svo_count, sov_count, total_count = 0, 0, 0

    with open(output_file, 'w', encoding='utf-8') as file:
        for tags in tagged_sentences:
            order = sentence_order(tags)
            if order == 'SVO':
                svo_count += 1
            elif order == 'SOV':
                sov_count += 1
            file.write(f"[{order}] -- {tags}\n\n")
            total_count += 1

    return {'SVO': svo_count / total_count * 100, 'SOV': sov_count / total_count * 100}



def sentence_order(tags):
    """
    Purpose: Determine SVO/SOV order based on first noun and verb encountered
    Logic: Does object come after or before verb??
    Input: A computed sentence (list of tuples with words and their POS tags).
    Returns: string value of 'SVO' or 'SOV'
    """
    #Initialize
    subject_pos = None
    verb_pos = None
    object_pos = None

    for i, (word, tag) in enumerate(tags):
        #Identify first noun as subject
        if subject_pos is None and tag.startswith('NN'):
            subject_pos = i
        elif verb_pos is None and tag.startswith('VB') and subject_pos is not None:
            verb_pos = i
        #Identify second noun as object
        elif object_pos is None and tag.startswith('NN') and i != subject_pos:
            object_pos = i
        if subject_pos is not None and verb_pos is not None and object_pos is not None:
            break

    if subject_pos is not None and verb_pos is not None and object_pos is not None:
        if subject_pos < verb_pos < object_pos:
            return 'SVO'
        elif subject_pos < object_pos < verb_pos:
            return 'SOV'
    return 'Unknown'
################################################################################

#---------------------------------- MAIN --------------------------------------#
################################################################################
def main():
    """
    Purpose: Main function
    Output: Frequency analysis
    """
    #------------ File Organization---------------#
    # 1. --- Input "Added text here"
    input_file = "L1_1.txt"

    # 2. --- Parsed
    parsed_file = input_file.split('.')[0] + '_parsed.txt'
    # 3. --- Final
    output_file = input_file.split('.')[0] + '_final.txt'
    # ----------- Generate parsed file ----------#
    generate_parsed(input_file)
    # ----------- Analysis with parsed file
    tagged_sentences = nltk_pos_tagging(parsed_file)
    freq_analyzed = identify_order(tagged_sentences, output_file)
    print(freq_analyzed)
################################################################################

if __name__ == "__main__":
    main()
