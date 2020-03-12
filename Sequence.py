class Sequence():
    # constructor
    def __init__(self, seqInfo: str, sequence: str):
        # sequnce information
        seqInfo = seqInfo.rstrip().split(' ')
        self.name = seqInfo[0]
        self.range = seqInfo[1].split('=')[1]           # ex. seqInfo[1] -> range=chr1:713916-714525
        self.pad_5 = seqInfo[2].split('=')[1]           # ex. seqInfo[2] -> 5'pad=0
        self.pad_3 = seqInfo[3].split('=')[1]           # ex. seqInfo[3] -> 3'pad=0
        self.strand = seqInfo[4].split('=')[1]          # ex. seqInfo[4] -> strand=+
        self.repeatMasking = seqInfo[5].split('=')[1]  # ex. seqInfo[5] -> repeatMasking=none
        
        # sequence
        self.sequence = sequence

    # printable
    def __str__(self):
        return f'Name: {self.name}\nSequence: {self.sequence}'

    def __repr__(self):
        return f'object: {self.name}\ntype: {type(self)}\naddress: {id(self)}'

    def printDetails(self):
        print(
        f"""
        Name: {self.name}
        Range: {self.range}
        5'pad: {self.pad_5}
        3'pad: {self.pad_3}
        strand: {self.strand}
        RepeatMasking: {self.repeatMasking}
        """ )
