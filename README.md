# Coding interview

## Questions

**Please write a simple program to perform the following tasks:** 

1. Calculate the #occurrence for a given 20-mer subsequence GCGGGGCCGGCCGCGGGAGC
2. Find the 20-mer subsequence with the highest occurrences.



## Files Structure



**substringSearch.py** is program's entry point.

**FastaReader.py** is a class for reading fasta file and helping calculating the highest occurrences of 20-mer subsequences as well as #occurrence for a given 20-mer subsequence in the fasta file. (Problem 2 is answered in this file's `findHighestOccurrence()` function)

**Sequence.py** is a class for reading sequence information and calculating number of given subsequence in a sequence. (Problem 1 is answered in this file's `numOfSubstringSearch()` function)

## Results

## Programs

##### substringSearch.py

```python
import sys
from FastaReader import FastaReader  

def main():
    fastaDir = sys.argv[1]                  # file directory
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
```


