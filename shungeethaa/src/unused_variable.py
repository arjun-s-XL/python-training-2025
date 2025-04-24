def add(x, y):
    result = x + y  # Unused variable
    return x + y

# ************* Module unused_variable
# unused_variable.py:1:0: C0114: Missing module docstring (missing-module-docstring)
# unused_variable.py:1:0: C0116: Missing function or method docstring (missing-function-docstring)
# unused_variable.py:2:4: W0612: Unused variable 'result' (unused-variable)