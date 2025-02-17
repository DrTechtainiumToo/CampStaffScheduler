# **PEP 8 Naming Guidelines** (by GPT-4)

## **General Naming Guidelines**
- Use **clear, descriptive names**; avoid single-letter variables except for counters or iterators in small loops.
- Avoid names that are **too general or too wordy**—strike a balance between brevity and clarity.

## **Variables**
- Use **lowercase single letters, words, or words separated by underscores**.
- **Example:**  
  ```python
  counter = 0
  employee_name = "John Doe"
  ```

## **Functions and Methods**
- Use **lowercase words separated by underscores** to improve readability.
- **Example:**  
  ```python
  def calculate_salary():
      pass

  def send_message(text):
      pass
  ```

## **Constants**
- Use **uppercase letters with underscores** separating words.
- **Example:**  
  ```python
  MAX_OVERFLOW = 100
  TOTAL_EMPLOYEES = 500
  ```

## **Classes**
- Use **CapWords (CamelCase)** convention—each word starts with a capital letter, without underscores.
- **Example:**  
  ```python
  class BankAccount:
      pass

  class EmployeeRecord:
      pass
  ```

## **Modules and Packages**
- Use **short, lowercase names**.  
- Use **underscores in module names if needed for readability**, but **avoid them in package names**.
- **Examples:**
  - **Modules:** `calculator.py`, `db_utils.py`
  - **Packages:** Prefer `mypackage` over `my_package`

## **Special Names**
- **Double leading and trailing underscores (`__`)** are reserved for **special methods and variables** (dunder methods).
- **Example:**  
  ```python
  class Example:
      def __init__(self):
          pass
      
      def __str__(self):
          return "Example class"
  ```

## **Private or "Internal" Use**
- Use a **single leading underscore (`_`)** to indicate a **non-public method or attribute**.
- **Example:**  
  ```python
  class Cache:
      def __init__(self):
          self._internal_data = {}

      def _internal_helper(self):
          pass
  ```

## **Avoiding Conflicts with Python Keywords**
- Append a **single trailing underscore (`_`)** to avoid naming conflicts with Python keywords.
- **Example:**  
  ```python
  class_ = "Reserved name workaround"
  from_ = "Avoids conflict with 'from' keyword"
  ```

## **Type Variables (PEP 484)**
- Use **CapWords**, preferring short names: `T`, `AnyStr`, `Num`.
- Add suffixes **`_co`** or **`_contra`** for **covariant** or **contravariant** behavior.
- **Example:**  
  ```python
  from typing import TypeVar

  T = TypeVar("T")
  AnyStr = TypeVar("AnyStr", str, bytes)
  Num_co = TypeVar("Num_co", covariant=True)
  ```

---