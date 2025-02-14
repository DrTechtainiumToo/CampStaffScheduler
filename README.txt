Project Setup & Running Instructions

🚀 Quick Start (Mac Users)
This project was developed on macOS, so all instructions assume you’re using a Mac.

git clone <your-repo-url>
cd SomeDeviousProject
poetry install  # Install dependencies
poetry run python main.py  # Run the program
🔧 Advanced Setup & Configuration
1️⃣ Install Poetry (Dependency Management)

If you haven’t installed Poetry yet, run:

curl -sSL https://install.python-poetry.org | python3 -
poetry --version  # Verify installation
2️⃣ Initialize Poetry (Only If Needed)

Navigate to the project folder:

cd /path/to/your/project
poetry init  # First-time setup (only if pyproject.toml is missing)
3️⃣ Running the Project

poetry run python main.py
📌 Notes for Future Me (In Case I Forget)

📦 Updating Dependencies
If you add new packages or update dependencies, inside the Poetry virtual environment, run:

pip freeze > requirements.txt
To install the dependencies in another environment:

pip install -r requirements.txt
To check installed packages in the current environment:

pip list
🛠 Git Workflow Cheatsheet

📌 Setting Up a Git Repository

git clone <repo-url>  # Clone a repo
cd <repo-folder>  # Move into the repo folder
📝 Making Changes & Pushing to GitHub

git status  # See what changed
git add .  # Stage all changed files
git commit -m "Your commit message"  # Commit changes
git push origin main  # Push changes to GitHub
🔄 Pulling Changes (If Working in a Team)

git pull origin main  # Pull the latest changes
🔍 Type Checking (Add Notes Later)

Add instructions for pytype and mypy here when needed.
🛠 Converting Pip-Based Dependencies to Poetry

If you need to scan through files for dependencies and convert them to Poetry:

pip uninstall pipreqs  # Uninstall pipreqs if needed
pipreqs . --force  # Generate requirements.txt
cat requirements.txt | xargs poetry add  # Convert dependencies to Poetry
🔄 Ensuring Reproducibility with Poetry

poetry lock  # Lock dependencies for reproducibility
🐍 Managing Python Versions in Poetry
Poetry defaults to using system Python, but you can force it to use your pyenv version:

poetry env use $(pyenv which python)
If that doesn’t work, manually specify:

poetry env use /Users/yourname/.pyenv/versions/<desired_version>/bin/python
To make sure all environments use pyenv, run:

poetry config virtualenvs.prefer-active-python true

Helpful notes on poetry
also TOML requires boolean values to be lowercase.
By default, if you don’t set an upper bound in your project’s pyproject.toml, Poetry might assume a broader range (possibly including Python 4.0.0)
to run evneryhtin inside a vienv in poetry: poetry shell



For me: 
textual docs: https://textual.textualize.io
Additonally im using Black for formatting so: 
# for formatting, black {source_file_or_directory}

To run mypy:
mypy .


PROJECT HISTORY AND EXPLINATION: 
for when i merge with mian that has an updated readme
