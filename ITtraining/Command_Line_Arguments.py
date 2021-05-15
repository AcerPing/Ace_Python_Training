import sys, getopt

def main(argv):
    inputfile = ""
    outputfile = ""

    try:
        opts, args = getopt.getopt(argv, "EAWlbp")
        print('opts:', opts)
        print('args:', args)

    except getopt.GetoptError:
        print('Commmand_Line_Arguments.py -[EAW][lbp]')
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print('Commmand_Line_Arguments.py -i <inputfile> -o <outputfile>')
            sys.exit()

        elif opt == '-E':
            print('-E')

        elif opt == "-A":
            print("-A")

if __name__ == '__main__':
    main(sys.argv[1:])

