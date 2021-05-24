import sys
import os
import subprocess
import json

ROOT_DIR = '/root/capstone/envs/'


def activate_path(env):

    #python version 가져오기 
    with open(f"{ROOT_DIR}{env}/settings.json" , "r") as json_file:
        json_data = json.load(json_file)

    python_ver = json_data['python'][0]['version']
    print(python_ver)
    
    print(sys.path)
   
    local_path = '/usr/local/lib/python' + python_ver + '/dist-packages'
    sys.path.remove(local_path)
    sys.path.append(ROOT_DIR + env)

    print(sys.path)



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

    print(env)

    if env != "":
        #python version 가져오기 
        with open(f"{ROOT_DIR}{env}/settings.json" , "r") as json_file:
            json_data = json.load(json_file)

        python_ver = json_data['python'][0]['version']
        print(python_ver)
        
        print(sys.path)
       
        #sys.path.remove(ROOT_DIR + env)
        local_path = '/usr/local/lib/python' + python_ver + '/dist-packages'
        sys.path.append(local_path)

        print(sys.path)




if __name__ == '__main__':
    command_type = sys.argv[1]

    if command_type == "activate":
        activate_path(sys.argv[2])

    elif command_type == "deactivate":
        if sys.argv[2] == "prompt":
            deactivate_prompt()

        else:
            deactivate_path()

