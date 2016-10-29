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
    parser.add_argument('--debug', nargs='?', const=True, help='Display debugging information when running')

    return parser.parse_args()
