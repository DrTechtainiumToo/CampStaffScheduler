from code_root.config.settings import INTERFACE_TYPE
from code_root.config.utility import clear_log_file, log_to_file

#python -m cProfile code_root.main

def main(INTERFACE_TYPE):
    
    
    clear_log_file()
    
    import sys
    log_to_file(sys.path[0])

    if INTERFACE_TYPE.lower() == 'web':
        from code_root.interface.website import create_app
        app = create_app()
        import webbrowser
        webbrowser.open("http://127.0.0.1:5000")
        app.run(debug=True)
    elif INTERFACE_TYPE.lower() == 'textual':
        from code_root.interface.textual_framework import textual_interface
        textual_interface
    elif INTERFACE_TYPE.lower() == 'terminal':
        from code_root.interface.terminal import terminal_interface
        terminal_interface #can i run a module, does just putting that there just run it???

if __name__ == "__main__":
    main(INTERFACE_TYPE)

#python -m cProfile -s time your_script.py
#snakeviz profile.prof