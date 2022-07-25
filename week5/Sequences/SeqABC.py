from abc import ABC, abstractmethod

class SeqABC(ABC):
    #This will define how sequences should behave

    """ You can pass an array to init the sequence with """
    @abstractmethod
    def __init__(self, seqArray, function):
        """ Assign the passed variables to their insance var """
        pass


    """ Add the passed var to the end of the sequence """
    @abstractmethod
    def addToSeq(self, toAdd):
        pass


    """ count the length of the sequence array """
    @abstractmethod
    def length(self):
        pass

    """ Get the sequence item by it's index """
    @abstractmethod
    def get(self, index):
        pass

    """ Iterate over the sequence to determine if it is increasing
        or decreasing. If two indexes are equal, then it can be neither
        increasing or decreasing (by definition)
    """
    @abstractmethod
    def IncrOrDecr(self):
        pass

    """ Call IncrOrDecr at the start of this method. This will determine
        which conditionals need to be tested. If it is increasing, then it is
        non-decreasing by definition. The opposite holds true for a decreasing
        sequence. If it is neither decreasing or increasing, then you must
        iterate over the sequence.
        CAREFUL: a trend of non-decreasing/increasing must be true for the 
                entire sequence. This means iterating over the whole array
                is a requirement.
    """
    @abstractmethod
    def nonDecrOrnonIncr(self)
        pass
