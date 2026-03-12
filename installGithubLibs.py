import os
from rich import print

cockroach = "https://github.com/Inferno-God1001/cockroach.git"
notify = "https://github.com/Inferno-God1001/notify.git"
tikcheck = "https://github.com/Inferno-God1001/TikCheck.git"


try:
    os.system(f"pip install git+{cockroach} && pip install git+{notify} && pip install git+{tikcheck}")
    print("[green bold]Successfully installing libraries from GitHub.")
except Exception as e:
    print()
    print(f"[yellow]{e}")
    print()
    print("[red bold]There was an error installing the libraries.")    
