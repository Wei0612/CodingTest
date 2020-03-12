#!/usr/bin/python
"""
UCLA Coding interview
Questions:
Please write a simple program to perform the following tasks:
1. Calculate the #occurrence for a given 20-mer subsequence GCGGGGCCGGCCGCGGGAGC
2. Find the 20-mer subsequence with the highest occurrences.
"""
# read command line arguments
# command line format: python occurrencesSearch.py fastaFileDirectory
import sys, os
from FastaReader import FastaReader  
from collections import defaultdict

def main():
    fastaDir = os.path.abspath(sys.argv[1])  # file directory
    fastaReader = FastaReader()
    fastaReader.readFastaFile(fastaDir)     # read file
    
    # PROBLEM 1. (Detail Algorithm implemented in Sequence.py (subStringSearch() function))
    searchString = sys.argv[2]
    numOfSubstring = fastaReader.numberOfSubstring(searchString)
    print(f"Problem 1: String, {searchString}, appears {numOfSubstring} times in file {fastaReader.getFileName()}")

    # PROBLEM 2. (Detail Algorithm implemented in FastaReader.py ())
    lengthOfString = int(sys.argv[3])
    highestFreqString, appearTimes, subseqCounter = fastaReader.findHighestOccurrence(lengthOfString)
    print(f"Problem 2: {lengthOfString}-mer subsequence, {highestFreqString}, has highest occurrences, {appearTimes} times, in file {fastaReader.getFileName()}")
    
    # output the all substring counts in substringCount.csv
    with open(os.path.join(os.path.abspath("./"), "Output", "substringCountLarger10.csv"), 'w') as outputFile:
        # column names
        outputFile.write("Subsequence,Counts\n")

        for subseq, counter in subseqCounter.items():
            if counter >= 10:
                outputFile.write(f"{subseq},{counter}\n")

if __name__ == "__main__":
    main()