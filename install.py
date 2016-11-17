import os
os.system("cp src/main.py ~/.gitcmain.py")

alias = 'alias gitc="python ~/.gitcmain.py"\n'
homefolder = os.path.expanduser('~')
bashrc = os.path.abspath('%s/.bashrc' % homefolder)

with open(bashrc, 'r') as f:
  lines = f.readlines()
  if alias not in lines:
    out = open(bashrc, 'a')
    out.write(alias)
    out.close()