
from pyface import Udp
from pyface import Parser
from pymac  import Player

class CmdMgr:
    """ Handles advanced manipulation of commands and macro player """

    def __init__( self ):
        self.__player = Player.Player()
        self.__protocol = None
        self.__lastsent = ''
        self.__parser = Parser.Parser()

        # dictionary which maps initialization commands to their functions
        self.__initmap = { 'UDP': self.__initUdp,
                           'SER': self.__initSer }

    # initialize an interface
    def init( self, args ):
        cmdli = args.split()

        if len(cmdli) > 0:
            if cmdli[0] in __initmap:
                __initmap[ cmdli[0] ](args)
            else:
                print( "Invalid selection" )

    # generic callback function for the protocol
    def __printOut( self, str ):
        print( "%s" % str )

    # args must fit the format: ip xmitport [recvport]
    # receive port is optional
    def __initUdp( self, args ):
        self.__protocol = Protocol.Protocol( Udp.Udp( args[ 2 ], args[ 3 ] ), self.__parser )
        self.__protocol.add( self.__printOut )
        self.__player.setProt( self.__protocol )

    def __initSer( self, args ):
        pass

    def __oneshot( self, msg ):
        self.__lastsent = msg
        self.__protocol.send( msg )