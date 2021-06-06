import sys
import os
import subprocess
import json

ROOT_DIR = '/root/capstone/envs/'



def activate_prompt(env):
    prompt = subprocess.check_output("echo $PS1", shell=True).decode() 

    if prompt[0] == '(':
        end = prompt.index(')') + 1
        print("activated")
        return prompt[:end]

    else:
        env_str = subprocess.check_output("ls -l " + ROOT_DIR + " | awk '/^d/{print $NF}'", shell=True).decode()
        env_list = env_str.split("\n")

        if env in env_list:
            prompt = '(' + env + ')' + prompt
            print(prompt)
            return prompt


        else:
            print("not_exist")




def activate_path(env):

    #python version 가져오기 
    with open(f"{ROOT_DIR}{env}/settings.json" , "r") as json_file:
        json_data = json.load(json_file)

    python_ver = json_data['python'][0]['version']
    print(python_ver)
   
    '''
    print(sys.path)
   
    local_path = '/usr/local/lib/python' + python_ver + '/dist-packages'
    sys.path.remove(local_path)
    sys.path.append(ROOT_DIR + env)

    print(sys.path)
    '''


def deactivate_prompt():
    prompt = subprocess.check_output("echo $PS1", shell=True).decode() 

    if prompt[0] == '(':
        end = prompt.index(')') + 1
        print(prompt[end:])
        return prompt[end:]

    else:
        print(prompt)
        return prompt



def deactivate_path():
    env = ""
    prompt = subprocess.check_output("echo $PS1", shell=True).decode()

    if prompt[0] == '(':
        end = prompt.index(')')
        env = prompt[1:end]

    #print(env)

    if env != "":
        #print(env)
        #python version 가져오기 
        with open(f"{ROOT_DIR}{env}/settings.json" , "r") as json_file:
            json_data = json.load(json_file)

        python_ver = json_data['python'][0]['version']
        print(python_ver)

        '''
        #print(sys.path)
       
        #sys.path.remove(ROOT_DIR + env)
        local_path = '/usr/local/lib/python' + python_ver + '/dist-packages'
        sys.path.append(local_path)

        #print(sys.path)
        '''

    #else:
    #    print("nothing to deactivate")



if __name__ == '__main__':
    command_type = sys.argv[1]

    if command_type == "activate":
        if sys.argv[2] == "prompt":
            activate_prompt(sys.argv[3])


    elif command_type == "deactivate":
        if sys.argv[2] == "prompt":
            deactivate_prompt()

        elif sys.argv[2] == "base":
            deactivate_path()

        #elif sys.argv[2] == "python_ver":
        #    deactivate_python_ver()

