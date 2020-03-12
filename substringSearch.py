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

def main():
    fastaDir = os.path.abspath(sys.argv[1])  # file directory
    fastaReader = FastaReader()
    fastaReader.readFastaFile(fastaDir)     # read file
    
    # PROBLEM 1. (Detail Algorithm implemented in Sequence.py (subStringSearch() function))
    searchString = "GCGGGGCCGGCCGCGGGAGC"
    numOfSubstring = fastaReader.numberOfSubstring(searchString)
    print(f"String, {searchString}, appears {numOfSubstring} times in file {fastaReader.getFileName()}")

    # PROBLEM 2. (Detail Algorithm implemented in FastaReader.py ())
    highestFreqString, appearTimes = fastaReader.findHighestOccurrence(20)
    print(f"20-mer subsequence, {highestFreqString}, has highest occurrences, {appearTimes} times, in file {fastaReader.getFileName()}")


if __name__ == "__main__":
    main()