def checkIndex(key):
    if not isinstance(key,(int,long)):
        raise TypeError
    if key < 0:
        raise IndexError

class ArithSequence:
    def __init__(self, start = 0, step = 1):
        self.start = start
        self.step = step
        self.changed = {}
    
    def __getitem__(self, key):
        checkIndex(key)
        try:
            return self.changed[key]
        except KeyError:
            return self.start + self.step*key

    def __setitem__(self, key, value):
        checkIndex(key)
        
        self.changed[key] = value

if __name__ == '__main__':
    A = ArithSequence(1,2)
    print A[4]
    A[4] = 2
    print A[4]
    print A[5]
