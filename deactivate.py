import sys
import os
import subprocess

ROOT_DIR = '/root/capstone/envs/'

def get_prompt(current):

    print("cc" + current)
    os.system("echo $PS1")
    if current[0] == '(':
        end = current.index(')') + 1
        return current[end:]


def get_prompt():

    prompt = subprocess.check_output("echo $PS1", shell=True).decode() 
    #print(prompt)

    if prompt[0] == '(':
        end = prompt.index(')') + 1
        return prompt[end:]

    else:
        return prompt



if __name__ == '__main__':
    command_type = sys.argv[1]

    if command_type == "prompt":
        print(get_prompt())

    else:
        print(11)
    #env = sys.argv[1]

