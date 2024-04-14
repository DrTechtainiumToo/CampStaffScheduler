__author__ = "Andrew Dybala"
__copyright__ = "Copyright Restricted"
__credits__ = ["Andrew Dybala", "GPT4 as assistant"]
__license__ = "License Name and Info"
__version__ = "1.3.2"
__maintainer__ = "Andrew Dybala"
__email__ = "andrew@dybala.com"
__status__ = "In development"

#import logging
from interface import web_app
from interface.terminal import terminal_interface
from backend.data import file_manager
from config import settings, utility
import asyncio
import os

#logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main(): 
    #does execution logic
    
    interface_type = os.getenv('INTERFACE_TYPE', 'terminal')  # Default to terminal if not set #TODO fix later
    if interface_type.lower() == 'web':
        web_app.run() #define this later
    else:
        terminal_interface #can i run a module, does just putting that there just run it???

if __name__ == "__main__":
    main()


"""
async def main_logic():
    # Your main application logic here
    await asyncio.sleep(1)  # Simulating some asynchronous operation
    print("Main logic executed")

if __name__ == "__main__":
    asyncio.run(main_logic())"""
