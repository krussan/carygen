#!/usr/local/bin/python2.7
# encoding: utf-8
'''
CaryGen -- Module for importing data from BilWeb

CaryGen is a module that scrapes the site Bilweb.se and finds a specific car and model and logs the price

@author:     krussan

@copyright:  2017. All rights reserved.

'''

import sys
import os

from argparse import ArgumentParser
from argparse import RawDescriptionHelpFormatter
from CaryGenWeb import CaryGenWeb

__all__ = []
__version__ = 0.1
__date__ = '2017-12-10'
__updated__ = '2017-12-10'

DEBUG = 1
TESTRUN = 0
PROFILE = 0

class CLIError(Exception):
    '''Generic exception to raise and log different fatal errors.'''
    def __init__(self, msg):
        super(CLIError).__init__(type(self))
        self.msg = "E: %s" % msg
    def __str__(self):
        return self.msg
    def __unicode__(self):
        return self.msg

def main(argv=None): # IGNORE:C0111
    '''Command line options.'''

    if argv is None:
        argv = sys.argv
    else:
        sys.argv.extend(argv)

    program_name = os.path.basename(sys.argv[0])
    program_version = "v%s" % __version__
    program_build_date = str(__updated__)
    program_version_message = '%%(prog)s %s (%s)' % (program_version, program_build_date)
    program_shortdesc = __import__('__main__').__doc__.split("\n")[1]
    program_license = '''%s
USAGE
''' % (program_shortdesc)

    try:
        # Setup argument parser
        print("Setting up parser")
        parser = ArgumentParser(description=program_license, formatter_class=RawDescriptionHelpFormatter)
        parser.add_argument("-b", "--brand", help="specifies the brand to search for")
        parser.add_argument("-m", "--model", help="specifies the model to search for")

        # Process arguments
        print("Parsing...")
        print(argv)
        args = parser.parse_args()
        
        if args.brand is None:
            parser.print_help()
        elif args.model is None:
            parser.print_help()
        else:
            print("Starting up...")
            w = CaryGenWeb(args.brand, args.model)
        
            print("Scraping...")
            res = w.scrape()
        
        return 0
    except KeyboardInterrupt:
        ### handle keyboard interrupt ###
        return 0
    except Exception, e:
        if DEBUG or TESTRUN:
            raise(e)
        indent = len(program_name) * " "
        sys.stderr.write(program_name + ": " + repr(e) + "\n")
        sys.stderr.write(indent + "  for help use --help")
        return 2

if __name__ == "__main__":
    if DEBUG:
        pass
    if TESTRUN:
        import doctest
        doctest.testmod()
    if PROFILE:
        import cProfile
        import pstats
        profile_filename = 'CaryGen_profile.txt'
        cProfile.run('main()', profile_filename)
        statsfile = open("profile_stats.txt", "wb")
        p = pstats.Stats(profile_filename, stream=statsfile)
        stats = p.strip_dirs().sort_stats('cumulative')
        stats.print_stats()
        statsfile.close()
        sys.exit(0)
    sys.exit(main())