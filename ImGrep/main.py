
import sys
import getopt

#The goal is to implement grep
#will be used only to .txt files
#Main will just be there to take input from console commands

#==========================================================

class Grep():

    def Finder(self):
        if (arg):
            print "lUl"
        else:
            print "Naa"

    @staticmethod
    def Main(argv):
        inputfile = ""
        outputfile = ""
        global arg
        try:
            opts, args = getopt.getopt(argv, "hi:o:",["ifile=", "ofile="])
        except getopt.GetoptError:
            print "test.py -i <inputfile>"
            sys.exit(2)
        for opt, arg in opts:
            if opt == '-h':
                print "test.py -i <filetype>"
                sys.exit()
            elif opt in ("-i", "--ifile"):
                inputfile = arg
            elif opt in ("-o", "--ofile"):
                outputfile = arg
        print "Listing files", inputfile

#==========================================================

#Running the goddamn ting

if __name__ == "__main__":
    Grep.Main(sys.argv[1:])
    aja = Grep()
    aja.Finder()
