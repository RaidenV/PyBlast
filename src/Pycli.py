import utils
import CmdMgr
from threading import Thread

class Cli( Thread ):
    """ Provides command line interface and sanitizes input """
    def __init__( self ):
        Thread.__init__(self)
        self.__cmdmgr = CmdMgr()

        #                Command   Requires Arg
        self.__cmdDict = { 'INIT' : True,
                         'PULSE'  : True,
                         'SEND'   : True,
                         'LOAD'   : True,
                         'PLAY'   : False,
                         'STOP'   : False,
                         'HELP'   : False,
                         'Q'      : False }

    def run( self ):
        while True:
            cmd = input(">> ")
            self.__exec( cmd )

    @staticmethod
    def menu():
        print( "-----------PyBlast Menu-----------" )
        print( "INIT [IFACE] args...   Initialize an interface with the required arguments" )
        print( "   Example:" )
        print( "      init udp 192.168.168.1 1234" )
        print( "           Initializes a UDP port to 192.168.168.1 address with a target port" )
        print( "           of 1234\n" )
        print( "      init ser /dev/ttyS3 9600" )
        print( "           Initialiazes a serial port to /dev/ttyS3 with a baud rate of 9600\n" )
        print( "PULSE  [0|1]           Choose to send a command at a given rate (ms)" )
        print( "SEND   MSG             Send a message" )
        print( "LOAD   FNAME           Load a macro file" )
        print( "PLAY                   Play a macro file" )
        print( "STOP                   Stop macro file playback" )

    # Execute a given input command
    def __exec( self, cmd ):

        # split all commands on whitespace
        cmdli = cmd.split()
        if len(cmdli) < 1: return
        # first arg is the command root
        croot = cmdli[0].upper()
        # the the remaining portion (less the CLI command) may be sent as a single string
        cleaf = utils.rmhead( cmd )

        print ( "%s   %s" % ( cmdli, croot ) )

        # check if the command requires more than one argument
        try:
            if self.cmdDict[croot.upper()] and len(cmdli) < 2:
                print( "Insufficient arguments for command" )
                return
        except KeyError:
            print( "Command not available" )


        if croot == 'HELP':
            self.menu()

        if croot == 'INIT':
            if args[ 1 ].upper() == "UDP":
                if len( args ) < 4:
                    print( "UDP initialization format:" )
                    print( "    init udp ipaddr port" )
                    return

            if args[ 1 ].upper() == "SER":
                if len( args ) < 3:
                    print( "Serial initialization format:" )
                    print( "    init ser port [baud]" )
                    return

            self.__cmdmgr.init( cleaf )

        if croot == 'SEND':
            self.__cmdmgr.oneshot( cleaf )

        if croot == 'PULSE':
            print( "Pulsing at %d" % cmdli[1] )

        if croot == 'Q':
            print( "Exiting" )
            exit(0)

if __name__ == "__main__":
    c = Cli()
    c.start()