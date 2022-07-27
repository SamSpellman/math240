from SeqABC import SeqABC

""" This class will implement SeqABC """
class Sequence(SeqABC):
    
    """ Instantiates the sequence object and initializes
        variables to passed parameters.
        seqArray: an array of numbers
        function: an explicit function as a string
        
        Checks types and attempts to set vars to the params.
    """
    def __init__(self, seqArray, function):
        # check seqArray with isinstance()
        if(isinstance(seqArray, list)):
            # Correct variable type 
            self.seqArray = seqArray
        else:
            # insantiate seqArray to an empty list
            self.seqArray = []

        # assign function to the function param(not used at this point)
        self.function = function

    """ Add the passed value to the sequence """
    def addToSeq(self, toAdd):
        # only need to append the value to seqArray
        if(isinstance(toAdd, int)):
            self.seqArray.append(toAdd)
        # it will not append a non integer value

    """ Return the length of the sequence array """
    def length(self):
        # There is a built in python function for length
        return len(self.seqArray)

    """ Return the sequence value at specified index.
        CASE(invalid index): return -1
    """
    def get(self, index):
        # verify that index is an int
        if(isinstance(index, int) != True):
            return -1
        else:
            return 1

    """ Compare two numbers to determine which is greater.
        This is a helper method.

        CASE greater: return 1
        CASE lesser: return -1
        CASE equal: return 0
    """
    def getTrend(x, y):
        if(x > y):
            return 1
        elif(x < y):
            return -1
        else:
            return 0

    """ Categorize seqArray as increasing, decreasing, or neither. 
        
        CASE increasing: return 1
        CASE decreasing: return -1
        CASE neither: return 0
    """
    def IncrOrDecr(self):
        # Iterate over the entire sequence to validate any trend
        trend = 0
        passed = None
        for element in seqArray:
            # validate a trend across the whole array
            if(trend == 0 and passed == None):
                # still need to figure out a trend
                passed = element
                # the continue sttmnt will go to next for loop iteration
                continue
            elif(trend == 0):
                match getTrend(element, passed):
                    case 1:
                        # INCREASING
                        trend = 1
                        passed = element
                    case -1:
                        # DECREASING
                        trend = -1
                        passed = element
                    case 0:
                        # NEITHER: end loop
                        trend = 0
                        break
            else:
                # the trend is set
                if(getTrend(element, passed) != trend):
                    # TREND BROKEN: break loop
                    trend = 0
                    break

        return trend

    def nonDecrOrnonIncr(self):
        return None

    """ Return the sequence as a formatted string """
    def displaySeqElements(self):
        # Iterate over the sequence, appending them to this string
        toPrint = "Sequence = "
        for i in range(len(self.seqArray)):
            toPrint += ("seqArray(" + str(i) + "):" + str(self.seqArray[i]) + ", ")
        return toPrint

    """ This will print data about the sequence, formatted to be 
        descriptive. This will assume the sequence begins at index 0.
        There will be no return, as display will print the data in place.
    """
    def toString(self):
        # Seperate print statements by line
        print("This is your finite sequence: \n")
        print(self.displaySeqElements())
