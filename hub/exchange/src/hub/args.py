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
    parser.add_argument('-d', '--daemonize', nargs='?', const=True, help='Fork this process into the background')
    parser.add_argument('-f', '--file',type=str, help='Log to output file specified')
    return parser.parse_args()
