## Python3.5
## Matrix Shell

from os import *
from cd import _cd
from socket import gethostname

## Functions and Programs
def _exit(param):
          if len(param) == 1: exit()
          else: print("run it without any parameter")

def _get_exit_status(param):
          if len(param) == 1: print(status)
          else: print("run it without any parameter")

def _exec(param):
          if param[0] == "ls": param.append("--color=auto")

          pid = fork()
          
          if pid == 0:
                    try: execvp(param[0], param)
                    except FileNotFoundError: print("matrixsh: error: command not found:", param[0]); quit()
          elif pid < 0: print("*** Fork Error")
          else: return waitpid(pid, 0)[1]

## Builtin Programs
programlist = ({"exit": _exit, "cd": _cd, "get_exit_status": _get_exit_status})

## Exit Status Default
status = 0

while True:
          user = environ["USER"]
          host = gethostname()

          currentDirectory = getcwd()
          currentDirectory = currentDirectory.replace("/home/{}".format(user), "~")

          prompt = "\033[1;32m{}\033[1;37m@\033[1;32m{} \033[1;37m{} \033[00m$ ".format(user, host, currentDirectory)
          if status != 0: prompt = "\033[1;31m({}) {}".format(status, prompt)

          try:
                    commandLine  =  input(prompt)
                    param        =  commandLine.split()
                    
                    elem = 0
                    while elem < len(param):
                              if param[elem][0] == "$":
                                        try: param[elem] = environ[param[elem][1:]]
                                        except KeyError: param.remove(param[elem]); elem = 0
                              elem += 1
                    
                    if param != []:
                              for progs in programlist:
                                        if param[0] == progs: programlist[progs](param); break
                              else: status = _exec(param)
          except KeyboardInterrupt: print()
