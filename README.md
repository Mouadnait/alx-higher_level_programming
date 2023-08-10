# Higher Level Python Programming Exercises
Exercises to learn Python 3.4.3 at [Alx School](https://www.alxafrica.com/). 
These exercises are designed to take the student from a complete novice to writing fully functional programs in Python.

* [0x00. Python - Hello, World](./0x00-python-hello_world)
* [0x01. Python - if/else, loops, functions](./0x01-python-if_else_loops_functions)

## Styling and Specifications
All programs were written from the Bash shell, with Vim.
### Compilation
All programs must run with pyton 3.4.3 on Ubuntu 14.04, and pass all style checks with [Pycodestyle](https://pypi.org/project/pycodestyle/)
All scripts require execution permissions:
```
chmod u+x file
```
To Run the scripts:
```
python3 script.py
./script.sh
```
To check the styling:
```
pycodestyle script.py
```
### Directory Structure
Each directory is named according to the key concept shared by all exercises in the directory. They are numbered sequentially to provide a linear timeline, and build on the key concepts from all previous concepts. Each directory contains a README.md with a short description of the program or script, and some useful links to the material. The directory [extras][extras] contains solutions to problems that do not pertain directly to the material, but was used for extracurricular study. Many are solutions to prompts from Project Euler, and are numbered according to their schema.

### [setup.sh](setup.sh)
Also contained in the repository's root directory is setup.sh.

#### Description:
This file sets up a directory based on the raw html from the assignment page. First, it creates the directory, then it creates all necessary files with their exact file name. Each file is populated with a template. It creates a .gitignore and its own README.md with a list of all the assignment files.
#### Use:
1. Grab the raw HTML from the assignment page on the internet. ``CMD + u`` for mac will bring the HTML source up. ``CTL + u`` for Linux or Windows. Copy and paste it into a file with a name of your choosing.
2. Run with ``./setup.sh``, when prompted, enter in the name of the HTML page, and the name of the header.

### Tools
* [Python 3.4.3](https://www.python.org/downloads/release/python-343/)
* [Installing Python from The Source Code](http://www.diveintopython.net/installing_python/source.html)
* [PIP](https://docs.python.org/3.4/installing/) - (PIP Installs Packages) Python's package manager
* [Pycodestyle](https://pypi.org/project/pycodestyle/) - The Python style checker
* [vim](http://www.vim.org/) - The CLI text editor
