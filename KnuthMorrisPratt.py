class KnuthMorrisPratt:
    def createPrefixTable(self, subsequence: str):
        # implement Knuth–Morris–Pratt algorithm
        # create prefixTable
        # indicator i j
        # index  = [0 1 2 3 4 5 6 7]
        # substr = [G C G G G G C C]
        # prefix = [0 0 1 . . . . .]
        prefixTable = [0] # index 1 always is 0
        i = 0
        j = 1
        while j < len(subsequence):
            if subsequence[j] == subsequence[i]:
                i += 1
                prefixTable.append(i)
                j += 1
            elif i > 0:
                i = prefixTable[i - 1]
            else:
                prefixTable.append(0)
                j += 1

        return prefixTable

    def searchNumOfPattern(self, content: str, pattern: str) -> int:
        occurrnceSites = [] # store perfect match index
        prefixTable = self.createPrefixTable(pattern)  # create prefixTable
        j = 0   # index of pattern

        for i in range(len(content)):
            while j > 0 and content[i] != pattern[j]:
                j = prefixTable[j - 1]

            if content[i] == pattern[j]:
                j += 1

            if j == len(pattern): 
                occurrnceSites.append(i - (j - 1))
                j = prefixTable[j - 1]

        return len(occurrnceSites)