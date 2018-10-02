from pyface.Port import Port
import socket

class Udp(Port):

    """
    Define an interface for UDP communication with a single entity.

    Note that this is a blocking implementation and should be run on a separate thread
    """
    LOCAL_HOST = '127.0.0.1'

    def __init__( self, targetip, targetport, listenport=0, timeout=None ):
        Port.__init__( self )
        self.__txip    = targetip
        self.__txport  = int(targetport)
        self.__rxport  = listenport
        self.__sock    = None
        self.__bufsz   = 1024   # Buffer size for receiving

    def init( self ):
        # grab the local host if txip is zero or empty
        if not self.__txip:
            self.__txip = self.LOCAL_HOST

        self.__sock = socket.socket( socket.AF_INET, socket.SOCK_DGRAM )
        try:
            self.__sock.bind( (socket.getfqdn(), self.__rxport) )

            print ( "%s" % socket.getfqdn() )
        except Exception as e:
            print( e )

    # send a message, catch and report any exceptions
    def send( self, msg ):
        try:
            self.__sock.sendto( msg.encode( 'utf-8' ), (self.__txip, self.__txport) )
        except Exception as e:
            print( e )

    # perform a block receive
    def recv( self ):
        data, server = self.__sock.recvfrom( self.__bufsz )
        if data:
            return data.decode()

if __name__ == "__main__":

    def printResponse( resp ):
        print( "Got: %s" % str( resp ) )

    udp = Udp( printResponse, "127.0.0.1", 4444 )
    udp.init()

    udp.send( "Hello server" )
    while True:
        udp.recv

