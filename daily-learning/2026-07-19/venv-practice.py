#!/usr/bin/env python3
"""
Day 1: Virtual Environment Setup - Practice Code
Topic: Understanding venv, virtualenv, and conda

This file demonstrates practical examples of working with virtual environments.
"""

# ============================================================================
# METHOD 1: Using venv (Built-in)
# ============================================================================

"""
Step-by-step instructions for venv:

1. Create environment:
   python -m venv venv

2. Activate:
   Windows: venv\Scripts\activate
   macOS/Linux: source venv/bin/activate

3. Install packages:
   pip install package_name

4. Check installed packages:
   pip list

5. Create requirements file:
   pip freeze > requirements.txt

6. Install from requirements:
   pip install -r requirements.txt

7. Deactivate:
   deactivate

Key Points:
- Built-in (no installation needed)
- Lightweight
- Good for beginners
- Simple projects
"""

# ============================================================================
# METHOD 2: Using virtualenv (Third-party)
# ============================================================================

"""
Step-by-step instructions for virtualenv:

1. Install virtualenv:
   pip install virtualenv

2. Create environment:
   virtualenv venv
   OR specify Python version:
   virtualenv -p python3.9 venv

3. Activate:
   Windows: venv\Scripts\activate
   macOS/Linux: source venv/bin/activate

4. Install packages:
   pip install package_name

5. Deactivate:
   deactivate

6. Delete environment:
   rm -rf venv  (macOS/Linux)
   rmdir venv   (Windows)

Advantages over venv:
- More features
- Better performance
- Supports multiple Python versions
- More control over environment
"""

# ============================================================================
# METHOD 3: Using conda (Anaconda/Miniconda) - RECOMMENDED FOR ML/AI
# ============================================================================

"""
Step-by-step instructions for conda:

1. Install Anaconda or Miniconda:
   Download from https://www.anaconda.com/ or
   https://docs.conda.io/projects/miniconda/

2. Create environment:
   conda create -n myenv python=3.9

3. List environments:
   conda env list

4. Activate:
   conda activate myenv

5. Install packages:
   conda install package_name
   OR from specific channel:
   conda install -c conda-forge package_name

6. Install multiple packages:
   conda install numpy pandas matplotlib scikit-learn

7. Create requirements file:
   conda env export > environment.yml

8. Create environment from file:
   conda env create -f environment.yml

9. Update environment:
   conda env update -f environment.yml --prune

10. Deactivate:
    conda deactivate

11. Delete environment:
    conda remove -n myenv --all

Why conda is best for ML/AI:
- Handles system dependencies
- Pre-compiled packages (faster)
- Great package repository
- Industry standard
- Better for data science packages
"""

# ============================================================================
# COMPARISON & BEST PRACTICES
# ============================================================================

comparison = {
    "venv": {
        "installation": "Built-in",
        "size": "Small",
        "setup_speed": "Fast",
        "features": "Basic",
        "best_for": "Beginners, simple projects",
        "learning_curve": "Very Easy"
    },
    "virtualenv": {
        "installation": "pip install virtualenv",
        "size": "Small",
        "setup_speed": "Fast",
        "features": "Advanced",
        "best_for": "Professional projects, multiple Python versions",
        "learning_curve": "Easy"
    },
    "conda": {
        "installation": "Anaconda/Miniconda",
        "size": "Large",
        "setup_speed": "Medium",
        "features": "Comprehensive",
        "best_for": "Data Science, ML/AI projects",
        "learning_curve": "Medium"
    }
}

# Print comparison
print("=" * 70)
print("VIRTUAL ENVIRONMENT COMPARISON")
print("=" * 70)

for method, details in comparison.items():
    print(f"\n{method.upper()}:")
    for key, value in details.items():
        print(f"  {key:<20}: {value}")

# ============================================================================
# BEST PRACTICES
# ============================================================================

best_practices = [
    "✅ Always use a virtual environment for each project",
    "✅ Activate environment before installing packages",
    "✅ Keep requirements.txt or environment.yml updated",
    "✅ Add venv/, env/ to .gitignore",
    "✅ Use meaningful environment names",
    "✅ Document your Python version and dependencies",
    "✅ Deactivate when switching projects",
    "✅ For ML/AI: Use conda instead of venv",
]

print("\n" + "=" * 70)
print("BEST PRACTICES")
print("=" * 70)
for practice in best_practices:
    print(practice)

# ============================================================================
# COMMON COMMANDS CHEAT SHEET
# ============================================================================

commands_cheat_sheet = {
    "Create": {
        "venv": "python -m venv env",
        "virtualenv": "virtualenv env",
        "conda": "conda create -n env python=3.9"
    },
    "Activate (Windows)": {
        "venv": "env\\Scripts\\activate",
        "virtualenv": "env\\Scripts\\activate",
        "conda": "conda activate env"
    },
    "Activate (macOS/Linux)": {
        "venv": "source env/bin/activate",
        "virtualenv": "source env/bin/activate",
        "conda": "conda activate env"
    },
    "Deactivate": {
        "venv": "deactivate",
        "virtualenv": "deactivate",
        "conda": "conda deactivate"
    },
    "List Environments": {
        "venv": "ls -la",
        "virtualenv": "ls -la",
        "conda": "conda env list"
    },
    "Delete": {
        "venv": "rm -rf env",
        "virtualenv": "rm -rf env",
        "conda": "conda remove -n env --all"
    }
}

print("\n" + "=" * 70)
print("COMMANDS CHEAT SHEET")
print("=" * 70)

for task, tools in commands_cheat_sheet.items():
    print(f"\n{task}:")
    for tool, cmd in tools.items():
        print(f"  {tool:<15}: {cmd}")

# ============================================================================
# MY RECOMMENDATION
# ============================================================================

print("\n" + "=" * 70)
print("MY RECOMMENDATION FOR THIS JOURNEY")
print("=" * 70)
print("""
For my AI/ML learning journey, I should use:

🏆 CONDA (Anaconda/Miniconda)

Why?
✅ Best for data science & ML packages
✅ Handles complex system dependencies
✅ Pre-compiled packages = faster setup
✅ Industry standard in ML community
✅ Better package ecosystem for ML
✅ Great for deep learning (TensorFlow, PyTorch)

Setup Command:
$ conda create -n ailearning python=3.9
$ conda activate ailearning
$ conda install numpy pandas matplotlib scikit-learn jupyter
""")

print("=" * 70)
