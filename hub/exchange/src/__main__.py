import args
import hub

def main ():
    hub.Hub(args.parse()).start()

if (__name__ == '__main__'):
    main()
