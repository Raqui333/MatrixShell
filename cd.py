## Python3.5
## CD

version = "1.0"

from os import chdir, environ, getcwd

def _cd(param):
          if len(param) == 1 or param[1] == "~":
                    chdir(environ["HOME"])
                    return 0
          else:
                    _path = " ".join(param[1:])
                    if param[1] == "-":
                              print(getcwd())
                              return 0
                    else:
                              try:
                                        chdir(_path)
                                        return 0
                              except Exception as e:
                                        print("cd: error:", e.args[1] + ":", _path)
                                        return e.errno
