
import args
import exchange

if (__name__ == '__main__'):
    argv = args.parse()

    print(argv)

    exchange = exchange.Exchange()

    if (argv.port != None):
        exchange.port = argv.port[0]


    exchange.bind()
    print('Complete!')
