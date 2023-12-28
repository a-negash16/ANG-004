# ANG-004

This repository contains a Python program developed for a project in a Text Analysis (CS 401) course. I investigated the influence of native language syntax on second language writing, specifically focusing on Amharic speakers writing in English. 
Amharic typically follows a subject-object-verb (SOV) order, whereas English adopts a subject-verb-object (SVO) structure. That being said, I hypothesized that Ethiopian writers, whose first language is Amharic, will exhibit traces of SOV word order in their English writings, deviating from the standard SVO order.


Methods
Data Sources
Datasets: Essays from first year writing courses by students from a small liberal arts college were obtained and categorized into two groups: L1 (Native Americans) and L2 (native Ethiopians).

Data Processing Stages
Manual Data Cleaning: Removed non-essential text elements (author, date, submission details of the paper).
Normalization: Adjusted for sentence parsing limitations by standardizing punctuation and altering “non-sentence-ending” periods.
Sentence Parsing and POS Tagging: Implemented sentence parsing and utilized NLTK package for Part-Of-Speech tagging.
Order Identification and Analysis: Developed a methodology to identify the syntactic order, focusing on noun positions to determine subject and object placements.


Key Findings
- The analysis indicates that Ethiopian writers show the influence of their native SOV language structure in their English writings, even in academic contexts.

Implications and Future Work
- This project provides a glimpse into linguistic research and the potential influences of native language syntax on second language proficiency. It underscores the importance of considering native language structures in language teaching and learning.

Limitations
Dataset Size: Limited dataset.
Logic for Order Identification

Contribution and Collaboration
I invite people to compare other texts, written by natives that are predicted to exhibit traces of SOV word order in their English writings, with native english writers. Feel free to reach out for collaboration or if you wish to contribute to this project.

