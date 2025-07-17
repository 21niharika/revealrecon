
# 🔍 RevealRecon

**RevealRecon** is a powerful Python-based reconnaissance tool designed for subdomain and URL enumeration, parameter and file-type detection, and light passive information gathering — all without relying on external tools like Amass or Gau.

> ⚡ Built for speed and simplicity — everything in one command  
> 👩‍💻 Developed with ❤️ by NIHARIKA

---

## ✨ Features

- Fast and recursive subdomain enumeration
- Crawls and extracts live URLs from multiple passive sources
- Detects:
  - Parameterized URLs
  - File extensions (e.g., `.js`, `.php`, `.html`, `.csv`, etc.)
- Organizes output into categorized sections
- Saves results into neatly structured files
- Optionally includes/excludes subdomains
- Displays useful leaked info: emails, IPs, server tech, etc.

---

## 📦 Requirements

- Python 3.8+
- `requests`, `re`, `argparse`, `tldextract`, `beautifulsoup4`, etc.

Install requirements:
```bash
pip install -r requirements.txt
