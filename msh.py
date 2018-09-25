#!/usr/bin/env python3.5
## Python3.5
## Matrix Shell

version = "1.3"

from os import *
from readline import *
from readline import parse_and_bind as bind
from msh_builtins import *
from msh_builtins import _msh_exec
from socket import gethostname

## Initial Exit Status
status = 0

## Binds
bind("set colored-stats on")
bind("set match-hidden-files off")
bind("set completion-query-items -1")
bind("set completion-prefix-display-length 0")
bind("TAB: complete")

## Completer
set_completer_delims(" ")
set_completer(msh_completer)

## History File
if path.isfile(histfile) == False: write_history_file(histfile)

read_history_file(histfile)

while True:
          user = environ["USER"]
          host = gethostname()

          currentDirectory = getcwd()
          currentDirectory = currentDirectory.replace("/home/{}".format(user), "~")

          ## DO NOT remove the NEWLINE
          prompt = "\033[1;32m{}\033[1;37m@\033[1;32m{} \033[1;37m{}\033[00m\n$ ".format(user, host, currentDirectory)
          if status != 0: prompt = "\033[1;31m{} {}".format(status, prompt)

          try:
                    ## Prompt
                    commandLine = input(prompt)
                    param = commandLine.split()

                    ## Shell Special Characters
                    elem = 0
                    while elem < len(param):
                              if param[elem][0] == "$":
                                        if param[elem][1:] == "?":
                                                  param[elem] = str(status)
                                        else:
                                                  try: param[elem] = environ[param[elem][1:]]
                                                  except KeyError:
                                                            param.remove(param[elem])
                                                            elem = 0
                              elif param[elem] == "~": param[elem] = environ["HOME"]
                              elif param[elem][-1] == "\\" and param[elem][:-1] != "":
                                        param[elem] = " ".join([param[elem][:-1], param.pop(elem + 1)])
                                        elem = 0
                              
                              elem += 1

                    ## Run Commands
                    if param != []:
                              for progs in programlist:
                                        if param[0] == progs:
                                                  status = programlist[progs](param)
                                                  break
                              else: status = _msh_exec(param)
          except KeyboardInterrupt: print()
          except EOFError: msh_exit(0)
