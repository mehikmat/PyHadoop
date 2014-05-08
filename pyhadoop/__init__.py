import argparse
import sys
import os
from resources import command_map

__author__ = 'hikmat'

"""
Module docstring.
This serves as a long usage message.
"""

HADOOP_HOME = ""

def set_vars():
    global HADOOP_HOME
    HADOOP_HOME = os.getenv("HADOOP_HOME","NULL")   

def validate_vars():
	if HADOOP_HOME == "NULL":
		print("HADOOP_HOME has not been set. Please set it.")
		exit()	

def main():    
    set_vars()
    validate_vars()

    parser = argparse.ArgumentParser(description='Processes commands aganist hadoop')
    parser.add_argument("command", help='hadoop command to be executed')	
    args = parser.parse_args()
    cmd = args.command    
    cmd_exec=''

    if cmd in command_map.keys():
       cmd_exec = command_map[cmd]
    else:
       print("Oops!!! Unknown command!!!")      
       print("Valid commands are:")
       print("========================")
       print("$> hadoopy start")
       print("$> hadoopy stop")
       print("$> hadoopy cp src dest")
       print("$> hadoopy mv src dest")
       print("========================\n")
       sys.exit(1)

    cmd_exec = cmd_exec.replace("$HADOOP_HOME",HADOOP_HOME)
    
    print("Executing {} .........".format(cmd_exec))

    os.system(cmd_exec)
    	

if __name__ == '__main__':   
    sys.exit(main())