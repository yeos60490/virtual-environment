import sys
import json

ROOT_DIR = '/root/capstone/envs/'

if __name__ == '__main__':

    env = sys.argv[1]

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
