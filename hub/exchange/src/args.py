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
        help = 'Sets the server port for device communications'
    )

    return parser.parse_args()
