#!/usr/bin/env python3.5
## Python3.5
## Matrix Shell

version = "1.0"

from os import *
from cd import _cd
from socket import gethostname

## Functions and Programs
def _exit_(ignore):
          exit(0)

def _get_exit_status(ignore):
          print(status)
          return 0

def _exec(param):
          if param[0] == "ls": param.append("--color=auto")

          pid = fork()

          if pid == 0:
                    try: execvp(param[0], param)
                    except Exception as e:
                              print("matrixsh: error:", e.args[1] + ":", param[0])
                              exit(e.errno)
          elif pid < 0: print("*** Fork Error")
          else: return waitpid(pid, 0)[1]

## Builtin Programs
programlist = ({"exit": _exit_, "cd": _cd, "get_exit_status": _get_exit_status})

## Exit Status Default
status = 0

while True:
          user = environ["USER"]
          host = gethostname()

          currentDirectory = getcwd()
          currentDirectory = currentDirectory.replace("/home/{}".format(user), "~")

          prompt = "\033[1;32m{}\033[1;37m@\033[1;32m{} \033[1;37m{} \033[00m$ ".format(user, host, currentDirectory)
          if status != 0: prompt = "\033[1;31m{} {}".format(status, prompt)

          try:
                    commandLine = input(prompt)
                    param = commandLine.split()

                    elem = 0
                    while elem < len(param):
                              if param[elem][0] == "$":
                                        try: param[elem] = environ[param[elem][1:]]
                                        except KeyError:
                                                  param.remove(param[elem])
                                                  elem = 0
                              elem += 1

                    if param != []:
                              for progs in programlist:
                                        if param[0] == progs:
                                                  status = programlist[progs](param)
                                                  break
                              else: status = _exec(param)
          except KeyboardInterrupt: print()
          except EOFError: exit(0)
