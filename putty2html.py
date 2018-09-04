#!/usr/bin/python

# Import libraries
import ConfigParser
import sys, getopt

# Configuration settings
Config = ConfigParser.ConfigParser()
Config.read('config/config.ini')

# Functions
def ConfigSectionMap(section):
    dict1 = {}
    options = Config.options(section)
    for option in options:
        try:
            dict1[option] = Config.get(section, option)
            if dict1[option] == -1:
                DebugPrint("skip: %s" % option)
        except:
            print("exception on %s!" % option)
            dict1[option] = None
    return dict1
	
# Main loop
def main(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv,
                                   "hi:o:",
                                   ["ifile=",
                                    "ofile="])
    except getopt.GetoptError:
        print 'putty2html.py -i <inputfile> -o <outputfile>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'putty2html.py -i <inputfile> -o <outputfile>'
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
    outfile = open(outputfile,'w')
    infile = file(inputfile)
    header = '<html><head></head><body>'
    footer = '</body></html>'
    outfile.write(header)
    for current_line in infile:
        if 'keyword1' in current_line:
            a = '<font color=' + ConfigSectionMap('Color')['keyword1'] + '>' + current_line + '</br>'
        elif 'keyword2' in current_line:
            a = '<font color=' + ConfigSectionMap('Color')['keyword2'] + '>' + current_line + '</br>'
        elif 'keyword3' in current_line:
            a = '<font color=' + ConfigSectionMap('Color')['keyword3'] + '>' + current_line + '</br>'
        else:
            a = '<font color=#000000>' + current_line + '</br>'
        outfile.write(a)
    outfile.write(footer)
    outfile.close()


if __name__ == "__main__":
    main(sys.argv[1:])
