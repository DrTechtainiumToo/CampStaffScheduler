# **📚 Project Documentation**

## **📌 Important Links - _Please Read_**
Want to understand **why** this project exists and the journey behind it? Check out the project reflection:  

- **RECOMMENDED READ:** 📖 **[Project Reflection](docs/project-reflection.md)** – Key insights and takeaways.  
- 📖 **[Project Documentation](docs/docs-README.md)** – Overview of all documentation.  

---

## **🚀 Project Setup & Running Instructions**

### **⚠️ Disclaimer for Windows Users**
> 🚨 *This project was developed on macOS. While Python is an interpreted language, some dependencies or commands may behave differently on Windows. If you encounter issues, consider adapting the setup process or contributing updated instructions!*  

---

## **⚡ Quick Start**
This project was developed on **macOS**, but it should work on **Windows** and **Linux** with Poetry.

### **1️⃣ Clone the Repository**
```sh
git clone <your-repo-url>
cd SomeDeviousProject
```

### **2️⃣ Install Dependencies**
Choose the appropriate installation:

| **Use Case** | **Command** |
|-------------|------------|
| **Just run the program** (minimal install) | `poetry install` |
| **Full development setup** (testing, debugging) | `poetry install --with dev` |

### **3️⃣ Run the Program**
```sh
poetry run python main.py
```

---

## **🖥️ Windows-Specific Instructions**
> 🚨 *Windows users may need to adapt some steps (e.g., installing Poetry manually and handling path differences).*  

1. **Ensure Python & pip are Installed**  
   - Check your Python version:  
     ```sh
     python --version
     ```
   - If missing, download and install **Python**: [Download Python](https://www.python.org/downloads/)  
   - Ensure `pip` is installed:  
     ```sh
     python -m ensurepip --default-pip
     ```

2. **Install Poetry** (If not already installed)  
   ```sh
   pip install poetry
   ```

3. **Install Dependencies**  
   - **For runtime only:**  
     ```sh
     poetry install
     ```
   - **For full development setup:**  
     ```sh
     poetry install --with dev
     ```

4. **Run the Program**  
   ```sh
   poetry run python main.py
   ```

---

## **🔧 Advanced Setup & Configuration**
### **1️⃣ Install Poetry (Dependency Management)**
If you haven’t installed Poetry yet, run:

**Mac:**
```sh
curl -sSL https://install.python-poetry.org | python3 -
poetry --version  # Verify installation
```

**Windows:**
```sh
pip install poetry
```

### **2️⃣ Initialize Poetry (Only If Needed)**
If the project does not already have a `pyproject.toml` file:
```sh
poetry init  # First-time setup (not needed if cloning a repo)
```

---

## **🛠 Additional Notes On Using Poetry**
- **To update all dependencies (including dev tools if installed):**  
  ```sh
  poetry update
  ```
- **To reset dependencies (e.g., switching between runtime and dev mode):**  
  ```sh
  poetry install  # Standard install (runtime only)  
  poetry install --with dev  # Full dev install
  ```

---

## **💡 Summary of Installation Options**
| **Installation Type** | **Command** |
|----------------------|-------------|
| Standard install (runtime only) | `poetry install` |
| Full development setup | `poetry install --with dev` |
| Run program | `poetry run python main.py` |

---
