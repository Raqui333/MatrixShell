## Python3.5
## Builtin Programs

import os as _msh_os

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
          exit(0)

def msh_get_exit_status(ignore):
          print(status)
          return 0
          
## Exit Status Default
status = 0

## List Of Programs
programlist = {"cd": msh_cd, "exit": msh_exit, "get_exit_status": msh_get_exit_status}
