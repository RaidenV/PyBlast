from pyface import Protocol

class Player:
    def __init__( self ):
        self.__protocol = None

    def setProt( self, prot ):
        self.__protocol = prot