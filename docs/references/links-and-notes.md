# **Development Notes & Useful Links**


### **Development Tools & Commands**

## **📌 Notes for Future Me (In Case I Forget)**

### **📦 Updating Dependencies**
If you add new packages or update dependencies, inside the Poetry virtual environment, run:

```sh
pip freeze > requirements.txt
```

To install the dependencies in another environment:

```sh
pip install -r requirements.txt
```

To check installed packages in the current environment:

```sh
pip list
```

---

## **🛠 Git Workflow Cheatsheet**
### **📌 Setting Up a Git Repository**
```sh
git clone <repo-url>  # Clone a repo
cd <repo-folder>  # Move into the repo folder
```

### **📝 Making Changes & Pushing to GitHub**
```sh
git status  # See what changed
git add .  # Stage all changed files
git commit -m "Your commit message"  # Commit changes
git push origin main  # Push changes to GitHub
```

### **🔄 Pulling Changes (If Working in a Team)**
```sh
git pull origin main  # Pull the latest changes
```

---

## **🔍 Type Checking (TODO: Add Notes Later)**
- Instructions for **pytype** and **mypy** to be added later.

---

## **🛠 Converting Pip-Based Dependencies to Poetry**
If you need to scan through files for dependencies and convert them to **Poetry**, run:

```sh
pip uninstall pipreqs  # Uninstall pipreqs if needed
pipreqs . --force  # Generate requirements.txt
cat requirements.txt | xargs poetry add  # Convert dependencies to Poetry
```

---

## **🔄 Ensuring Reproducibility with Poetry**
Lock dependencies to ensure a reproducible environment:

```sh
poetry lock
```

---

## **🐍 Managing Python Versions in Poetry**
Poetry defaults to using **system Python**, but you can force it to use **pyenv**:

```sh
poetry env use $(pyenv which python)
```

If that doesn’t work, manually specify the Python version:

```sh
poetry env use /Users/yourname/.pyenv/versions/<desired_version>/bin/python
```

To make sure **all environments** use pyenv, run:

```sh
poetry config virtualenvs.prefer-active-python true
```

---

## **📌 General Notes**

## **📌 Helpful Notes on Poetry**
- **TOML** requires **boolean values to be lowercase**.
- By default, if you **don’t** set an **upper bound** in `pyproject.toml`, **Poetry might assume a broader range** (including Python 4.0.0).
- To **run everything inside a virtual environment** in Poetry, use:

  ```sh
  poetry shell
  ```


- **Static Type Checking**  
  Run `mypy` for static type checking:  
  ```sh
  mypy {program.py}
  ```
- **Code Formatting**  
  Using **Black** for formatting:  
  ```sh
  black {source_file_or_directory}
  ```
- **Profiling & Performance Analysis**
  - Run Python’s built-in profiler:
    ```sh
    python -m cProfile -s time your_script.py
    ```
    This sorts the output by execution time (`-s time`) to identify bottlenecks.
  - Use **Snakeviz** for visual profiling analysis:
    ```sh
    snakeviz profile.prof
    ```
    This launches a graphical, web-based viewer to explore profiling data.

- **Removing Cached/Bloat Files from Git Commits**
  ```sh
  git rm --cached -r **/__pycache__/
  git rm --cached -r *.pyc
  ```

---

## **📌 Python Documentation & References**
- 📖 [Official Python C API Docs](https://docs.python.org/3/c-api/intro.html)
- 📖 [Python Project Structure & Packaging](https://medium.com/@joshuale/a-practical-guide-to-python-project-structure-and-packaging-90c7f7a04f95)
- 📖 [Structuring Python Projects](https://docs.python-guide.org/writing/structure/)
- 📖 [Python Module Index](https://docs.python.org/3/py-modindex.html)

---

## **📌 GUI Development**
### **🚀 General Python GUI Resources**
- 📖 [Python GUI Programming Wiki](https://wiki.python.org/moin/GuiProgramming)
- 📖 [Comparison of Python GUI Libraries](https://www.pythonguis.com/faq/which-python-gui-library/)
- 📖 [Best Python GUI Libraries](https://www.bairesdev.com/blog/best-python-gui-libraries/)

### **🖥️ GUI Toolkits**
- **Flet** ([flet.dev](https://flet.dev))  
  🚀 Fast but not ideal for long-term maintainability.  
  🎥 [YouTube Tutorial](https://www.youtube.com/watch?v=JJCjAUmNXBs)

### **🌐 Web-Based GUI**
- **Flask** ([Flask Docs](https://flask.palletsprojects.com/en/3.0.x/))

### **📱 Flutter for Desktop & Mobile**
- [Flutter Official Site](https://flutter.dev)  
  🚨 Free for commercial use, but requires learning **Dart**.  
- [Flutter-Python Starter Project](https://github.com/maxim-saplin/flutter_python_starter)  
- [Flutter Desktop Install Guide (Mac)](https://docs.flutter.dev/get-started/install/macos/desktop)
- [Connecting Python Backend to Flutter App](https://medium.com/@sudeshnb/to-connect-a-python-backend-to-a-flutter-mobile-app-a9f61f8d54f2#:~:text=78-,To%20connect%20a%20Python%20backend%20to%20a%20Flutter%20mobile%20app,for%20handling%20the%20app%27s%20state.)

---

## **📌 Library Documentation**
- **Python Prompt Toolkit** → 📖 [Documentation](https://python-prompt-toolkit.readthedocs.io/en/master/)

---

## **📌 macOS Shell & Application Scripting**
- [How to Create macOS Shell Applications](https://mathiasbynens.be/notes/shell-script-mac-apps)
- [macOS Shell Script Examples](https://gist.github.com/mathiasbynens/674099)

---

## **📌 Excel Plugin/Add-in Development**
- 🎥 [Python Excel Add-in Tutorial](https://youtu.be/K6pRl7XHBAU?feature=shared)
- 🎥 [Ribbon Customization in Python](https://www.youtube.com/watch?v=G_Egf3oxghI)
- 🎥 [Unknown but interesting?](https://www.youtube.com/watch?v=MwZwr5Tvyxo)

---

## **📌 Other GUI Design Tools**
- **Tkinter Designer**  
  📥 [Download from GitHub](https://github.com/ParthJadhav/Tkinter-Designer)  
  🎥 [YouTube Setup Guide](https://www.youtube.com/watch?v=9oaqCMwcoQ4)

---

