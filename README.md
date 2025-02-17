### **Is the Mac Quick Start Installing Dev Dependencies?**  
**No, the current Mac quick start installs only the runtime version.**  

🔍 The command in the **Quick Start (Mac Users)** section is:  
```sh
poetry install  # Install runtime dependencies only
```
This **does not include** dev dependencies. If a user wants dev tools, they need to explicitly install them using:  
```sh
poetry install --with dev
```

---

### **✅ Corrections & Clarifications**
1. **Clarify that the default Mac setup is for the runtime version.**
2. **Provide an explicit option for dev setup in the Quick Start section.**
3. **Fix `poetry init` in Step 2** (it’s **not** needed unless creating a new project).
4. **Fix `poetry install --no-root`** → `poetry install --no-dev` is clearer for removing dev dependencies.

---

### **🚀 Updated & Corrected Instructions**

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

### **Quick Start (Mac Users)**
This project was developed on **macOS**, so all instructions assume you're using a Mac.

1. **Clone the repository**  
   ```sh
   git clone <your-repo-url>
   cd SomeDeviousProject
   ```
2. **Install dependencies**  
   - **To install the standard runtime version (no dev tools):**  
     ```sh
     poetry install --no-dev
     ```
   - **To install the development version (includes dev tools):**  
     ```sh
     poetry install --with dev
     ```
3. **Run the program**  
   ```sh
   poetry run python main.py
   ```

---

### **🖥️ Quick Start (Windows Users)**
> 🚨 *Windows users may need to adapt some steps (e.g., installing Poetry manually and handling path differences).*  

1. **Clone the repository**  
   ```sh
   git clone <your-repo-url>
   cd SomeDeviousProject
   ```
2. **Ensure Python & pip are installed**  
   - Check your Python version:  
     ```sh
     python --version
     ```
   - If missing, download and install **Python**: [Download Python](https://www.python.org/downloads/)  
   - Ensure `pip` is installed:  
     ```sh
     python -m ensurepip --default-pip
     ```
3. **Install Poetry** (If not already installed)  
   ```sh
   pip install poetry
   ```
4. **Install dependencies**  
   - **For runtime only:**  
     ```sh
     poetry install --no-dev
     ```
   - **For full development setup:**  
     ```sh
     poetry install --with dev
     ```
5. **Run the program**  
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
Navigate to the project folder:

- **For the development version (includes dev tools):**  
  ```sh
  poetry install --with dev
  ```

- **For the standard runtime version:**  
  ```sh
  poetry install --no-dev
  ```

---

### **🛠 Additional Notes On Using Poetry**
- **To update all dependencies (including dev tools if installed):**  
  ```sh
  poetry update
  ```
- **To remove unnecessary dependencies after cleanup:**  
  ```sh
  poetry install --no-dev
  ```
- **If switching between dev and runtime environments, reset dependencies:**  
  ```sh
  poetry install --no-dev  # Standard install
  poetry install --with dev  # Dev install
  ```

---

### **💡 Summary of Installation Options**
| Installation Type | Command |
|------------------|---------|
| Standard runtime install | `poetry install --no-dev` |
| Full development setup | `poetry install --with dev` |
| Run program | `poetry run python main.py` |

