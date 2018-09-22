## Python3.5
## Builtin Programs

version = "1.2"

import os as _msh_os
import readline as _msh_readline

## History Config
histfile = "{}/.msh_history".format(_msh_os.environ["HOME"])
_msh_readline.set_history_length(1000)

def msh_cd(param):
          if len(param) == 1 or param[1] == "~":
                    _msh_os.chdir(_msh_os.environ["HOME"])
                    return 0
          else:
                    elem = 1
                    while elem < len(param[1:]):
                              if param[elem][-1] == "\\":
                                        param[elem] = " ".join([param[elem][:-1], param.pop(elem + 1)])
                                        elem = 1
                              else:
                                        param[elem] = param.pop(elem + 1)
                    
                    _path = param[1]
                    
                    if param[1] == "-":
                              print(_msh_os.getcwd())
                              return 0
                    else:
                              try:
                                        _msh_os.chdir(_path)
                                        return 0
                              except Exception as e:
                                        print("cd: error:", e.args[1] + ":", _path)
                                        return e.errno

def _msh_exec(param):
          if param[0] == "ls": param.append("--color=auto")

          pid = _msh_os.fork()

          if pid == 0:
                    try: _msh_os.execvp(param[0], param)
                    except Exception as e:
                              print("matrixsh: error:", e.args[1] + ":", param[0])
                              exit(e.errno)
          elif pid < 0: print("*** Fork Error")
          else: return _msh_os.waitpid(pid, 0)[1]

def msh_exit(ignore):
          _msh_readline.write_history_file(histfile)
          exit(0)

## List Of Programs
programlist = {"cd": msh_cd, "exit": msh_exit}
