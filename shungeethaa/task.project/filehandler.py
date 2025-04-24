from pathlib import Path
if Path ('app_logging.log').exists():
    print("File exists!")

with open('app_logging.log') as f:
    data = f.read()
    print(f.tell())
    f.seek(0)