Matti:

Byte-compiled / cache
__pycache__/
**/__pycache__/
*.py[cod]
*.pyc
*.pyo
*$py.class


If .pyc files are already tracked, remove them from Git's index (run from the project root):

remove tracked pyc and cache dirs from git, but keep them locally

git rm -r --cached __pycache__ || true

git rm -r --cached *.pyc || true

git commit -m "Ignore __pycache__ and byte-compiled files"



Jackie:

  I had Copilot mainly help walk me through hthe installation of poetry, as I had some issues installing it onto my device at first. I also had Copilot help me in some other areas such as helping me to format some docstrings, though I went back in to edit them and make sure they accurately portrayed what each function/ script was doing. I had it also format the README.md file before i deleted the contents itself and updated it with my own documentation. 
