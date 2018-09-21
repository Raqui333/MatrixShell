## Python3.5
## CD

from os import chdir, environ, getcwd

def _cd(param):
          if len(param) == 1 or param[1] == "~": chdir(environ["HOME"])
          else:
                    _path = " ".join(param[1:])
                    if param[1][0] != "-":
                              try: chdir(_path)
                              except FileNotFoundError: print("cd: error: no such file or directory:", _path)
                    elif param[1][1:] == "": print(getcwd())
                    else: print("cd: warning: function not implemented:", param[1])
