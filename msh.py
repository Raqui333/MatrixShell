#!/usr/bin/env python3.5
## Python3.5
## Matrix Shell

version = "1.1"

from os import *
from msh_builtins import *
from msh_builtins import _msh_exec
from socket import gethostname

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
                              else: status = _msh_exec(param)
          except KeyboardInterrupt: print()
          except EOFError: exit(0)
