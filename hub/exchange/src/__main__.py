import args

from exchange import Exchange

def main ():
    argv = args.parse()

    print(argv)

    exchange = Exchange()

    if (argv.port != None):
        exchange.port = argv.port[0]


    exchange.bind()
    print('Complete!')

if (__name__ == '__main__'):
    main()
