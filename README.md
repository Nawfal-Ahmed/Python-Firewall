README — Python Firewall 

A simple, hands-on Python firewall that uses iptables to block/unblock ports and manage basic rules.
This README gives step-by-step instructions so someone with no network or Linux experience can clone the project, install what’s needed, and run the program on a Linux machine (Kali Linux recommended). The project draws on ideas in the included slide deck (packet inspection, iptables integration, Scapy, GUI ideas). 

Building-a-Python-Firewall

Table of contents

Project overview

Prerequisites (what to download/install)

How to get the code from GitHub (clone / pull)

Step-by-step setup (virtualenv, dependencies)

How to run the program (examples)

How it works (brief explanation)

Safety & testing recommendations

Troubleshooting (common errors + fixes)

Contributing & license

1 — Project overview

This program is a small command-line firewall manager written in Python. It provides these operations:

Block a TCP port (adds iptables rules)

Unblock a TCP port (removes the iptables rules)

View current iptables rules

Flush / clear all iptables rules

The slides that accompany this project explain design choices and recommended best practices (use of iptables, Scapy for packet inspection if you extend this project, testing in Kali Linux). 

Building-a-Python-Firewall

2 — Prerequisites (what to download)

You will need:

A Linux machine. Kali Linux is recommended for learning and testing (slides recommend Kali). 

Building-a-Python-Firewall

git — to clone the repository

python3 (3.8+ recommended) and pip3

(Optional but recommended) virtualenv or venv to isolate Python packages

iptables (built into most Linux distros)

If you plan to add packet sniffing later: scapy (pip package)

Commands to install essentials on a Debian/Ubuntu/Kali system:

# update package lists
sudo apt-get update

# install git, python3, pip, and venv tools
sudo apt-get install -y git python3 python3-pip python3-venv

# verify iptables is available
sudo iptables -L -n


If you need Scapy (only required for advanced packet sniffing/extensions):

pip3 install scapy


(Scapy is recommended in the slides for packet analysis). 

Building-a-Python-Firewall

3 — How to get the code from GitHub

Open a terminal and run:

git clone https://github.com/Nawfal-Ahmed/Python-Firewall.git

cd Python-Firewall


If you don't know the repo URL, open the project page on GitHub and copy the "Clone" URL (HTTPS).

4 — Step-by-step setup (recommended, beginner-friendly)

We’ll create a Python virtual environment and install any project requirements.

Open a terminal and go to the project directory (see section 3).

Create and activate a virtual environment:

# create venv (only needs to be done once)
python3 -m venv venv

# activate it
source venv/bin/activate


Install Python dependencies (if the project has requirements.txt):

# if requirements.txt exists
pip install -r requirements.txt

# otherwise install minimal dependencies
pip install scapy


Make the main script executable (optional):

# adjust filename if your main file is different (e.g., firewall.py)
chmod +x firewall.py

5 — How to run the program (step-by-step with examples)

Important: The script needs to run commands that modify iptables. Those commands require elevated privileges. There are two common ways to run:

Run the whole script with sudo (quick, but gives full root to Python process).

Run the script as a normal user; when it executes iptables it should call sudo internally — you will be prompted for your password. (Your script in this repo uses os.system("sudo iptables ..."), so it will require a sudo password.)

Example — run the script directly:
# from project folder, with virtualenv active
sudo python3 firewall.py
# OR (if script uses internal sudo calls)
python3 firewall.py


You should see a menu similar to:

========== Python Firewall ==========
1. Block a port
2. Unblock a port
3. View current rules
4. Clear all rules
5. Exit

Example interactions

To block port 80 (HTTP):

Choose option 1

Enter 80 when prompted

The script will run:

sudo iptables -A INPUT -p tcp --dport 80 -j DROP
sudo iptables -A OUTPUT -p tcp --dport 80 -j DROP


To view rules:

Choose option 3

The script will run:

sudo iptables -L -n --line-numbers


To clear all firewall rules:

Choose option 4

Confirm y when prompted

The script will run:

sudo iptables -F


Note: Replace firewall.py with the actual filename if your main script has a different name.

6 — How it works (brief explanation)

The Python program provides a simple menu and uses os.system() to call iptables commands to add, delete, list, and flush rules.

The slides recommend possible extensions like integrating Scapy for packet sniffing/inspection, JSON-based rule files, or a GUI (Tkinter/Flask) for management. Those are optional extensions you can add later. 

Building-a-Python-Firewall

7 — Safety & testing recommendations (must read)

Do not run destructive tests on your production machine. Test inside a virtual machine or isolated lab network. The slide deck strongly recommends testing in controlled environments like a VM. 

Building-a-Python-Firewall

Changing iptables can break remote access (SSH). If you're connected remotely (e.g., via SSH), be careful — blocking port 22 will lock you out. Always keep a recovery plan.

Avoid running unknown scripts as root. Review code before running. The project uses sudo iptables — make sure every os.system call is safe.

8 — Troubleshooting (common problems + fixes)

Problem: Permission denied or commands failing
Fix: Run with sudo or grant appropriate privileges. Example: sudo python3 firewall.py

Problem: Running iptables commands returns "command not found"
Fix: Install iptables or use a distribution that provides it (most Linux do). Example: sudo apt-get install -y iptables

Problem: After blocking a port you lose SSH access
Fix: If you’re locked out and have console access (VM host), remove the block rule or flush rules:

# remove specific rule (if you know line number)
sudo iptables -D INPUT <line-number>
# or flush all rules (careful)
sudo iptables -F


Problem: Script throws Python errors about os.system or functions
Fix: Make sure the script filename matches what you run. Check for Python syntax errors (run python3 -m py_compile firewall.py).

9 — Extending the project (ideas)

Add Scapy-based packet inspection for logging suspicious packets. 

Building-a-Python-Firewall

Use a JSON file for configurable rules (whitelist/blacklist).

Build a Tkinter or Flask GUI for easier rule management (slides discuss both options). 

Building-a-Python-Firewall

Add unit tests and simulated network tests (in a VM).

Author: Nawfal Ahmed

Slides and background notes used in this README: Building a Python Firewall (provided with the project). 

Building-a-Python-Firewall

Quick checklist (one-liner steps)
1) git clone https://github.com/Nawfal-Ahmed/Python-Firewall.git
2) cd [<repo>](https://github.com/Nawfal-Ahmed/Python-Firewall) && python3 -m venv venv && source venv/bin/activate
3) pip install -r requirements.txt    (or pip install scapy)
4) sudo python3 firewall.py           (or python3 firewall.py then enter sudo password when prompted

Quick demo (3–5 minutes)

Open two terminals in your Kali VM (Terminal A and Terminal B).

Show your Python firewall script ready

ls -l firewall.py
nano firewall.py   # (show the main menu area briefly)




Start a simple service on port 8080 (Terminal A)

python3 -m http.server 8080


Expected: Serving HTTP on 0.0.0.0 port 8080 ...


Prove it works (Terminal B)

curl -I localhost:8080


Expected output: an HTTP header (HTTP/1.0 200 OK or directory listing).


Show current iptables rules

sudo iptables -L -n --line-numbers


Expected: no DROP rule for dpt:8080.


Run the firewall script and block port 8080

sudo python3 firewall.py


Menu → 1 → enter 8080 to block.

Then in Terminal B:

curl -I localhost:8080


Expected: either curl: (7) Failed to connect... (if iptables returns RST) or curl hangs and eventually times out (if packets are dropped).


Show iptables rule was added

sudo iptables -L -n --line-numbers


Expected: lines showing DROP for tcp dpt:8080 in INPUT and OUTPUT chains (or whichever chain you used). Point to them.

Unblock and re-test
In the firewall menu → 2 → enter 8080.
Then:

curl -I localhost:8080


Expected: HTTP response returns.
Say: “Unblocked — service responds again.”

Wrap up: explain persistence (iptables-persistent) and that script requires sudo.
