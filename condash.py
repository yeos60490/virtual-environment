from optparse import OptionParser
import argparse
import os
import sys

def Options():
    parser = OptionParser()
    parser.add_option("-i", "--info", 
                        action = "store_true", 
                        dest="info",
                        help="print info")

    parser.add_option("--activate", 
                        #action = "store_true", 
                        dest="activate",
                        help="activate envs")

    parser.add_option("--deactivate", 
                        action = "store_true", 
                        dest="deactivate",
                        help="deactivate envs")

    (options, args) = parser.parse_args()

    if options.info != None:
        Info()
    elif options.activate != None:
        Activate(options.activate)
    elif options.deactivate != None:
        Deactivate()
    else:
        print("none")




def Info():
    print("info")


def Activate(env):
    print("activate")
    os.system("export PS1='(test)'$PS1")
    os.system("echo $PS1")
    #os.system("ls -al")
    #print(env)


def Deactivate():
    print("deactivate")



if __name__ == '__main__':
 
    command_type = sys.argv[1] if len(sys.argv) >= 2 else "None"

    if command_type == "activate":
        Activate(sys.argv[2])   
        
    elif command_type == "deactivate":
        Deactivate()   

          
    #Options()
    '''
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--info",
        action = "store_true",
        help="info"
    )

    parser.add_argument(
        "activate",
        action = "store_true",
        #required=False,
        #default = "base",
        #type = str,
        help="activate environment"
    )

    args = parser.parse_args()
    #print(args)


    #if args.activate:
    #    Activate("test")
    '''
