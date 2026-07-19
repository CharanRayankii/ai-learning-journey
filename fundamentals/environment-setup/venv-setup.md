# 🔧 Python Virtual Environment Setup Guide

## Overview
Virtual environments are isolated Python environments that allow you to manage project-specific dependencies without affecting your system Python installation.

---

## Method 1: Using `venv` (Built-in)
**Pros:** Built-in, no additional installation, lightweight  
**Cons:** Limited features  
**Best For:** Simple projects, beginners

### Steps:

**1. Create a virtual environment:**
```bash
python -m venv venv
```
*(This creates a folder named `venv`)*

**2. Activate the virtual environment:**

**On Windows:**
```bash
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
source venv/bin/activate
```

**3. Your prompt will change to show the environment is active:**
```bash
(venv) C:\Users\YourName\project>  # Windows
(venv) user@machine:~/project$    # macOS/Linux
```

**4. Install packages:**
```bash
pip install package_name
```

**5. Deactivate when done:**
```bash
deactivate
```

**6. Save dependencies:**
```bash
pip freeze > requirements.txt
```

**7. Install dependencies in a new environment:**
```bash
pip install -r requirements.txt
```

---

## Method 2: Using `virtualenv` (Third-party)
**Pros:** More features, faster, supports multiple Python versions  
**Cons:** Requires installation  
**Best For:** Professional projects, multiple Python versions

### Steps:

**1. Install virtualenv (if not installed):**
```bash
pip install virtualenv
```

**2. Create a virtual environment:**
```bash
virtualenv venv
```
*(You can also specify Python version:)*
```bash
virtualenv -p python3.9 venv
```

**3. Activate the virtual environment:**

**On Windows:**
```bash
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
source venv/bin/activate
```

**4. Install packages:**
```bash
pip install package_name
```

**5. Deactivate when done:**
```bash
deactivate
```

**6. Save dependencies:**
```bash
pip freeze > requirements.txt
```

---

## Method 3: Using `conda` (Anaconda/Miniconda)
**Pros:** Best for data science, handles system dependencies, easy package management  
**Cons:** Heavier, larger installation, slower sometimes  
**Best For:** Data science, ML projects, conda packages

### Steps:

**1. Install Anaconda or Miniconda:**
- Download from: https://www.anaconda.com/ or https://docs.conda.io/projects/miniconda/

**2. Create a conda environment:**
```bash
conda create -n myenv python=3.9
```
*(Replace `myenv` with your environment name, `3.9` with desired Python version)*

**3. Activate the conda environment:**

**On Windows:**
```bash
conda activate myenv
```

**On macOS/Linux:**
```bash
conda activate myenv
```

**4. Install packages:**
```bash
conda install package_name
```
*(Or from specific channel:)*
```bash
conda install -c conda-forge package_name
```

**5. Deactivate when done:**
```bash
conda deactivate
```

**6. Save dependencies:**
```bash
conda env export > environment.yml
```

**7. Create environment from file:**
```bash
conda env create -f environment.yml
```

**8. Remove an environment:**
```bash
conda remove -n myenv --all
```

---

## Comparison Table

| Feature | venv | virtualenv | conda |
|---------|------|-----------|-------|
| Installation | Built-in | pip install | Anaconda/Miniconda |
| Setup Speed | Fast | Fast | Slower |
| Python Versions | Limited | Multiple | Multiple |
| Package Management | pip | pip | conda/pip |
| Size | Small | Small | Large |
| Data Science | ✅ | ✅ | ✅✅✅ |
| System Dependencies | ❌ | ❌ | ✅ |
| Learning Curve | Easy | Easy | Medium |

---

## Best Practices

### ✅ DO:
- Always use a virtual environment for projects
- Activate before installing packages
- Keep `requirements.txt` or `environment.yml` updated
- Add `venv/` or `env/` to `.gitignore`
- Use meaningful environment names

### ❌ DON'T:
- Install packages globally (outside virtual environment)
- Commit virtual environment folder to Git
- Mix different environment managers in one project
- Forget to deactivate when switching projects

---

## Useful Commands Quick Reference

| Task | venv | virtualenv | conda |
|------|------|-----------|-------|
| Create | `python -m venv env` | `virtualenv env` | `conda create -n env` |
| Activate (Windows) | `env\Scripts\activate` | `env\Scripts\activate` | `conda activate env` |
| Activate (Mac/Linux) | `source env/bin/activate` | `source env/bin/activate` | `conda activate env` |
| Deactivate | `deactivate` | `deactivate` | `conda deactivate` |
| List packages | `pip list` | `pip list` | `conda list` |
| Export dependencies | `pip freeze > req.txt` | `pip freeze > req.txt` | `conda env export > env.yml` |
| Install from file | `pip install -r req.txt` | `pip install -r req.txt` | `conda env create -f env.yml` |

---

## My Recommendation for AI/ML Learning
**Use `conda`** because:
- Great for data science & ML packages
- Handles complex system dependencies easily
- Better for deep learning frameworks (TensorFlow, PyTorch)
- Excellent package management
- Industry standard in data science

---

**Last Updated:** 2026-07-19
