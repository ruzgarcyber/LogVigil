# LogVigil 🛡️

**Mini Log Monitoring Tool | Automatic Security Scanner in Python**

LogVigil automatically scans `.log` files in the folder you specify and detects suspicious activity.  
With this lightweight Python script, you can quickly identify critical errors or unauthorized access attempts on your system.

---

## 🚀 Features
- Scans `.log` files in the specified folder.
- Detects suspicious keywords: `error`, `failed`, `unauthorized`, `denied`.
- Prints detected lines directly to the terminal.
- If no suspicious activity is found, a safe message is displayed.
- CLI support with optional folder path (`--path` or `-p`).

---

## ⚡ Installation
Python 3 is required; no extra libraries are needed.  
Clone the repository or download the files:

```bash
git clone https://github.com/ruzgarcyber/LogVigil
cd LogVigil
```

## 🛠️ Usage

```bash
python logvigil.py --path /var/log
```
> Optional arguments:
- --path or -p: Specify the folder containing log files (default: /var/log).

## 🔎 Example Output
```bash
[!] Suspicious activity detected: auth.log → login failed for user root
[+] No suspicious activity found.
```

## ✨ Contributing
> Feel free to fork the repository and submit pull requests if you want to contribute.
