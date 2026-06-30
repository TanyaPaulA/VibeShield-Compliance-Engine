"""
hello_antigravity.py
====================
Day 1 Onboarding Scratchpad
Workspace : d:/Projects and Patents/agy-day1
Created   : 2026-06-24
Author    : Antigravity IDE (Google DeepMind)

Purpose
-------
Verify that the local sandbox environment is operational and
serve as a clean starting point for Day 1 exploration.
"""

import sys
import platform
from datetime import datetime


def greet() -> None:
    """Print a friendly onboarding greeting and system snapshot."""
    border = "=" * 56
    print(border)
    print("  ***  Hello, Antigravity!")
    print("  Day 1 Onboarding — Environment Check")
    print(border)
    print(f"  Timestamp  : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"  Python     : {sys.version.split()[0]}")
    print(f"  Platform   : {platform.system()} {platform.release()} ({platform.machine()})")
    print(f"  Executable : {sys.executable}")
    print(border)
    print("  [OK] Sandbox environment is OPERATIONAL.")
    print("  Happy coding — let's build something great!")
    print(border)


if __name__ == "__main__":
    greet()
