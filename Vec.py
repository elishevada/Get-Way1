ssssssssssssssss
class Vec:
    def __init__(self):
        self.__vec = []
        
    def getVec(self):
        return self.__vec
    
    #The function clear a vector
    def clearVec(self):
        self.__vec.clear()
    
    #The function concatenate a vector to the class's vector. 
    def concatVecs(self, secVec):
        self.__vec.extend(secVec)
        
    #The function appends list with an item or adds an item at the end of the list.
    def vecAppend(self, index, val):
        self.__vec.append([index,val]) 
        
        
        
        gggggggggggggggggggggggggggggggggggggggggggggggggg
        ff
