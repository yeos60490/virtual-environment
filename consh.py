from optparse import OptionParser
import argparse
import os
import sys
import json

ROOT_DIR = "/root/capstone"

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
        activate(options.activate)
    elif options.deactivate != None:
        deactivate()
    else:
        print("none")




def Info():
    print("info")



def env_create(env, python_ver):
    if python_ver == "current":
        python_ver = "3.7"
    
    print(f"Environment created: {env} (python ver. {python_ver})")
    env_path = ROOT_DIR + f"/envs/{env}"
    os.system(f"mkdir {env_path}")
    os.system(f"touch {env_path}/settings.json")

    #with open(f"{env_path}/settings.json" , "r") as json_file:
    #    json_data = json.load(json_file)

    json_data = {}
    json_data['python'] = []
    json_data['python'].append({
        "version": f"{python_ver}"
    })
    json_data['packages'] = []

    with open(f"{env_path}/settings.json", 'w') as outfile:
        json.dump(json_data, outfile, indent=4)



def env_remove(env):
    check = input(f"Remove Environment: {env} ? (yes/no): ")
    if check == "yes":
        os.system(f"rm -r {ROOT_DIR}/envs/{env}")
        print(f"Environment removed : {env}")
    else:
        print("cancelled")


def env_list():
    print("Environments:")
    os.system("ls -l " + ROOT_DIR + "/envs/ | awk '/^d/{print $NF}'") 
    print()


if __name__ == '__main__':
 
    command_type = sys.argv[1] if len(sys.argv) >= 2 else "None"

    #if command_type == "activate":
    #    activate(sys.argv[2])   
        
    #elif command_type == "deactivate":
    #    deactivate()   
    
    if command_type == "env":
        if sys.argv[2] == "create":
            python_ver = sys.argv[4].split('==')[1] if len(sys.argv) >= 5 else "current"
            env_create(sys.argv[3], python_ver)

        elif sys.argv[2] == "remove":
            env_remove(sys.argv[3])

        elif sys.argv[2] == "list":
            env_list()



          
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
    #    activate("test")
    '''
