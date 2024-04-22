__author__ = "Andrew Dybala"
__copyright__ = "Copyright Restricted"
__credits__ = ["Andrew Dybala", "GPT4 as assistant"]
__license__ = "License Name and Info"
__version__ = "1.3.5"
__maintainer__ = "Andrew Dybala"
__email__ = "drtechtainium@gmail.com"
__status__ = "In development"
__compiler__ = "Python 3.12.0"

#https://medium.com/@joshuale/a-practical-guide-to-python-project-structure-and-packaging-90c7f7a04f95
#https://docs.python-guide.org/writing/structure/


#import logging
from interface import web_app
from interface.terminal import terminal_interface
from backend.data import file_manager
from config import settings, utility
import asyncio
import os
import logging

def main(): 
    interface_type = os.getenv('INTERFACE_TYPE', 'terminal')  # Default to terminal if not set #TODO fix later
    if interface_type.lower() == 'web':
        web_app.run() #define this later
    else:
        terminal_interface #can i run a module, does just putting that there just run it???

if __name__ == "__main__":
    main()

#python -m cProfile -s time your_script.py
#snakeviz profile.prof