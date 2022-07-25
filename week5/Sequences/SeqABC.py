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

