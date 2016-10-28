import argparse
import textwrap

NAME = 'Exchange'
DESCRIPTION = textwrap.dedent('''\
    Central message exchange for the smart hub
''')

def parse ():
    parser = argparse.ArgumentParser(
        prog        = NAME,
        usage       = '%(prog)s [options]',
        description = DESCRIPTION
    )
    parser.add_argument(
        '-p', '--port', nargs = 1, type = int,
        help = 'Sets the server port for device communications'
    )

    return parser.parse_args()
