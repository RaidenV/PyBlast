import sys
import re

def rmhead( s ):
    """ Removes the first word from a string """
    ver   = sys.version_info[0] == 3
    isStr = ( isinstance( s, basicstring ), isinstance( s, str ) )[ver]

    if not isStr:
        return

    return re.sub(r'^\W*\w+\W*', '', string )