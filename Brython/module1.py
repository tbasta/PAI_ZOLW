import sys
import traceback

cmd = ""

def create_command(_cmd):
    cmd = open('Brython.py').read()
    print("było: " + cmd)
    cmd = cmd.replace("_code", _cmd)
    print("jest: " + cmd)
    return cmd
    
def exec_code():
    _code = create_command("some text")
    try:
        exec(_code)
        print("finalnie: " + _code)
    except:
        try:
            traceback.print_exc()
        except:
            print("could not print traceback")

exec_code()