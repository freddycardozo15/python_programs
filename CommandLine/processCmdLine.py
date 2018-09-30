# This python program processes the command line arguments using a json file.
# The command parameters are defined in the json file commandLine.json 

__author__ = 'Freddy Cardozo'

from pdb    import set_trace as st
from pprint import pprint 

from common import readJsonFile
from common import processCommandLineArgs

try:
    # Read the command line argument fields from the json file 'commandLineArguments.json'
    cmd_line_hash = readJsonFile('commandLineArguments.json')
    pprint(cmd_line_hash)
    cmd_line_obj  = processCommandLineArgs(cmd_line_hash)
except StopIteration as e:
    print("Stop Iteration  occured")
except:
    print("Error Ocured")
