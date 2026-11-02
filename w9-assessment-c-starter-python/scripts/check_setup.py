"""
Setup check for the Assessment C starter kit (Python).
Run from the repo folder:  python scripts/check_setup.py     (Windows: py scripts\\check_setup.py)
Green = ready. Red = fix before your first task (raise your hand if stuck).
"""
import importlib.util
import socket
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
problems = 0


def ok(msg):
    print(f"  OK    {msg}")


def bad(msg, fix):
    global problems
    problems += 1
    print(f"  FIX   {msg}\n        -> {fix}")


def info(msg):
    print(f"  INFO  {msg}")


def run(cmd):
    try:
        return subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True, check=True).stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        return None


print("\nAssessment C setup check (Python)\n")

if sys.version_info >= (3, 9):
    ok(f"Python {sys.version.split()[0]}")
else:
    bad(f"Python {sys.version.split()[0]} is too old", "Install Python 3.12+ from https://python.org (check 'Add python.exe to PATH').")

for module, package in (("requests", "requests"), ("dotenv", "python-dotenv")):
    if importlib.util.find_spec(module):
        ok(f"{package} installed")
    else:
        bad(f"{package} not installed", "Run:  python -m pip install -r requirements.txt   (Windows: py -m pip install -r requirements.txt)")
if importlib.util.find_spec("pandas"):
    info("pandas installed (optional for Task 3)")
else:
    info("pandas not installed. Optional: the built-in csv module is enough for Task 3.")

git_version = run(["git", "--version"])
if git_version:
    ok(git_version)
else:
    bad("Git not found", "Install Git from https://git-scm.com, then reopen VS Code.")
git_name, git_email = run(["git", "config", "user.name"]), run(["git", "config", "user.email"])
if git_name and git_email:
    ok(f"Git identity: {git_name} <{git_email}>")
else:
    bad("Git name/email not set", 'Run:  git config --global user.name "Your Name"  and  git config --global user.email "you@example.com"')
if run(["git", "rev-parse", "--is-inside-work-tree"]) == "true":
    ok("This folder is a Git repo")
else:
    info("Not a Git repo yet. That is expected before launch step 4 (git init).")

required = ["ai/workshops_spring2026.csv", "ai/baseline_summary.md", "ai/prompt_scaffold.md", "api/task2.py",
            "mock-api/server.py", "data/raw.csv", "run_pipeline.py", "notes/data_cleaning_log.md",
            "notes/reflection.md", "README.md", ".env.example", "requirements.txt"]
missing = [f for f in required if not (ROOT / f).exists()]
if not missing:
    ok(f"All {len(required)} starter files present")
else:
    bad(f"Missing files: {', '.join(missing)}", "Re-extract the starter kit zip into this folder.")

if (ROOT / ".env").exists():
    info(".env exists (Task 2). Make sure .gitignore keeps it out of Git.")
else:
    info("No .env yet. You will create it in Task 2.")

try:
    with socket.create_connection(("127.0.0.1", 5050), timeout=1.5):
        info("Mock API is running on port 5050.")
except OSError:
    info("Mock API not running. That is fine until Task 2 (python mock-api/server.py).")

print("\nREADY: no problems found.\n" if problems == 0 else f"\nNOT READY: fix the {problems} item(s) marked FIX above.\n")
sys.exit(0 if problems == 0 else 1)
