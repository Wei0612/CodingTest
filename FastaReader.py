import os
from Sequence import Sequence
from collections import defaultdict
from KnuthMorrisPratt import KnuthMorrisPratt

class FastaReader():
    def __init__(self):
        self.dir = ""
        self.fileDir = ""
        self.fileName = ""
        self.seqs = []  # save sequence information and sequences
        self.numOfSeqs = 0

    # getter
    def getFileName(self):
        return self.fileName

    # load fasta file
    def readFastaFile(self, fileDir) -> None:
        self.fileDir = fileDir
        self.dir = os.path.dirname(fileDir)
        self.fileName = os.path.basename(fileDir)

        # read file
        with open(self.fileDir, 'r') as inputFile:
            content = inputFile.read()
            splitedContent = content.split('>')  # split sequences by '>'
            splitedContent.pop(0) # remove first element "" at index 0

            for seqContent in splitedContent:
                # remove whitespace and newline and then split string by newline
                seqContent = seqContent.rstrip().split("\n")

                # save sequence info and sequence
                seqInfo = seqContent[0]
                sequence = "".join(seqContent[1:])

                # create Sequence object
                sequence = Sequence(seqInfo, sequence)

                # store sequence into list
                self.seqs.append(sequence)
                self.numOfSeqs += 1
                
        # report how many reads loaded
        self.numberOfSequences()

    #print amout of sequnces in fasta file
    def numberOfSequences(self) -> None:
        print(f'There are {self.numOfSeqs} seuqneces in {self.fileName}')

    # print element by index
    def printSeqInfoByIndex(self, index: int) -> None:
        if index >= len(self.seqs):
            print(f"index {index} is out of range of list! There are only {self.numOfSeqs} elements in {self.fileName}")
        else:
            print(self.seqs[index])

    # problem 1. Calculate the #occurrence for a given 20-mer subsequence GCGGGGCCGGCCGCGGGAGC
    def numberOfSubstring(self, substring: str) -> None:
        allOccurrence = 0
        kmp = KnuthMorrisPratt()
        
        for seq in self.seqs:
            sequence = seq.sequence
            allOccurrence += kmp.searchNumOfPattern(sequence, substring)
        
        return allOccurrence

    
    # problem 2. Find the 20-mer subsequence with the highest occurrences
    def findHighestOccurrence(self, lengthOfString: int) -> str:
        highestFreqString = ""
        appearTimes = 0
        subseqCounter = defaultdict(int)

        # Owing to dictionary is implemented by hashTable,
        # I assume that the complexity of using key to get value is O(1)
        # iterate the seqs list to gather single sequence
        for seq in self.seqs:
            sequence = seq.sequence

            # if sequence length is 51 and length of string is 20-mer,
            # total substring is 51-20+1=32
            for i in range(0, len(sequence) - lengthOfString + 1, 1):
                subsequence = sequence[i: i + lengthOfString]
                subseqCounter[subsequence] += 1

                if subseqCounter[subsequence] > appearTimes:
                    highestFreqString = subsequence
                    appearTimes = subseqCounter[subsequence]

        return [highestFreqString, appearTimes, subseqCounter]
