"""
Python Install

Many PCs and Macs will have python already installed.

To check if you have python installed on a Windows PC, 
search in the start bar for Python or run the following 
on the Command Line (cmd.exe):

c:\Users\Nurhan>python --version

"""



"""

Python Quickstart

Python is an interpreted programming language,
this means that as a developer you write Python (.py) 
files in a text editor and then put those files 
into the python interpreter to be executed.

The way to run a python file is like this on the command line:

C:\Users\Nurhan>python hi_world.py
"""



"""
Python Version

To check the Python version of the editor, 
you can find it by importing the sys module:
"""
import sys

print(sys.version)



"""
The Python Command Line

To test a short amount of code in python
sometimes it is quickest and easiest not to 
write the code in a file. This is made 
possible because Python can be run as 
a command line itself.

C:\Users\Nurhan>py
Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> print("Hello World")
Hello World
>>> exit()

"""