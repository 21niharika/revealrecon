
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

```
##  Example Commands

```bash
# Basic domain recon
python revealrecon.py -d target.com

# Include and exclude subdomains
python revealrecon.py -d target.com --include blog --exclude admin

# Save categorized output
python revealrecon.py -d target.com --save

# Extract live parameterized URLs
python revealrecon.py -d target.com --params --live

# Detect leaked data (emails, tech, IPs)
python revealrecon.py -d target.com --leaks --save

```

🚀 How to Use
1. Clone this repository or download the script:
```bash
git clone https://github.com/yourname/revealrecon.git
cd revealrecon
```
2. Run the script:
```bash
python revealrecon.py -d example.com
```

🛠️ Available Command-Line Flags
```bash
options:
  -h, --help  show this help message and exit
  --params    Show URLs with parameters
  --ext       Show URLs with file extensions
  --live      Show only live URLs/subdomains
  --leaks     Display sensitive info leaks
```

📂 Output Structure

If --save is used, all data is saved under output/ like this:
```bash
output/
├── subdomains.txt
├── urls.txt
├── urls_with_params.txt
├── urls_with_ext.txt
├── urls_included.txt
├── urls_excluded.txt
├── live_subdomains.txt
├── live_urls.txt
├── sensitive_leaks.txt
```


📋 What This Tool Can Do

    Perform passive and active enumeration to extract live subdomains

    Crawl each subdomain and collect:

        Full URLs

        URLs with GET parameters

        URLs pointing to file extensions like .js, .env, .json, .xml

    Check if domains and URLs are live/working

    Detect common sensitive info leaks from page content:

        Email addresses

        IP addresses

        JavaScript file links

        Technologies used

        Database/server hints

    Save each output in a structured way for bug bounty/hacking reports

📎 Sample Use Case

You're participating in a bug bounty or internal VAPT assessment and need to quickly:

    Get all live subdomains

    Extract JS/JSON endpoints

    Find parameter-based links to test for XSS/LFI

    Identify secrets or email leaks

    Save everything in structured files for later testing

RevealRecon does it all in one go.

📌 Author

🧠 Developed by: NIHARIKA MEENA
Cybersecurity Analyst | Bug Bounty Hunter
