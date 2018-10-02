from abc import ABC, abstractmethod

class Port:
    """
    Defines an abstract structure to which other types of ports should
    adhere.  Provides methods that are common and must be reimplemented.
    """

    def __init__( self ):
        pass

    @abstractmethod
    def init( self ):
        pass

    @abstractmethod
    def send( self, msg ):
        pass

    @abstractmethod
    def recv( self ):
        pass

