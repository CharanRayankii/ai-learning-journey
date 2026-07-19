# Virtual Environment Setup

There are three common ways to set up a Python virtual environment.

## Method 1: Using Conda

1. Open the terminal in VS Code.
2. Create a new environment with a specific Python version:

   ```bash
   conda create -p venv python=3.12
   ```

   - Replace `3.12` with the version you want.
   - The `-p venv` option creates the environment in a folder called `venv`.

3. Activate the environment:

   ```bash
   conda activate ./venv
   ```

   - If you created the environment at a different path, use that path instead.

4. Deactivate when finished:

   ```bash
   conda deactivate
   ```

> Note: Conda can create an environment with a Python version different from the system Python installed on your machine.

## Method 2: Using Python `venv`

1. Create a new virtual environment:

   ```bash
   python -m venv myenv
   ```

2. Activate the environment on Windows:

   ```powershell
   .\myenv\Scripts\Activate
   ```

   On macOS/Linux use:

   ```bash
   source myenv/bin/activate
   ```

3. Install packages with pip:

   ```bash
   pip install numpy
   ```

4. Deactivate when finished:

   ```bash
   deactivate
   ```

## Method 3: Using `virtualenv`

1. Install `virtualenv` if needed:

   ```bash
   pip install virtualenv
   ```

2. Create a new virtual environment:

   ```bash
   virtualenv -p python3 virtual_env
   ```

3. Activate the environment on Windows:

   ```powershell
   .\virtual_env\Scripts\Activate
   ```

   On macOS/Linux use:

   ```bash
   source virtual_env/bin/activate
   ```

4. Deactivate when finished:

   ```bash
   deactivate
   ```

---

## Quick Notes

- On Windows, use `Activate` from the `Scripts` folder, not `active`.
- On macOS/Linux, use `source .../bin/activate`.
- Use `pip install <package>` inside the activated environment.
- Use `deactivate` or `conda deactivate` to exit the environment.

