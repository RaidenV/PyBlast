# Generic class for importing various parsers and ports (serial, udp, etc...)
# and running blocking receive threads

from threading import Thread

class Protocol(Thread):
    "Defines a generic protocol class for inserting various parsers and ports"

    def __init__( self, port, parser):
        Thread.__init__(self)
        self.__parser = parser
        self.__port = port
        # Callback should always be to the parsers parse function
        self.__callback = []
        self.__port.init()

        self.start()

    def setParser( self, parser ):
        self.__parser = parser

    def setPort( self, port ):
        self.__port = port

    # Allows user to specify function to call whenever data is received
    def addCallback( self, callback ):
        # ensure that the function set by the user is callable
        if hasattr( callback, '__call__' ):
            self.__callback.append(callback)
        else
            raise AttributeError( "Cannot set uncallable object as a callback function" )

    def run( self ):
        while True:
            output = self.__port.recv()
            for cb in self.__callback:
                cb( self.__parser.parse( output ) )

    def send( self, msg ):
            self.__port.send( msg )