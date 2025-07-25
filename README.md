
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
python3 reconx.py -d example.com

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
| Flag                                       | Description                                      |
| ------------------------------------------ | ------------------------------------------------ |
| -d, --domain                               | **(Required)** Target domain for enumeration     |                               

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


#Screenshots

<img width="1920" height="1029" alt="Screenshot 2025-07-12 010206" src="https://github.com/user-attachments/assets/950865d7-48b3-4917-b6f5-2fbbab610984" />
<img width="1920" height="1029" alt="Screenshot 2025-07-12 010137" src="https://github.com/user-attachments/assets/832598c8-3483-497a-b30d-d140296c9763" />
<img width="1920" height="1029" alt="Screenshot 2025-07-12 010724" src="https://github.com/user-attachments/assets/b5f62f90-e33b-4cc3-88bf-f7e368b100f0" />
<img width="1920" height="1029" alt="Screenshot 2025-07-12 010659" src="https://github.com/user-attachments/assets/a6b92d2b-69de-4e13-bbc0-b2d67bdcfd97" />
<img width="1920" height="1029" alt="Screenshot 2025-07-12 010650" src="https://github.com/user-attachments/assets/374c790a-9148-427c-9993-1acc1e9cbc33" />
<img width="1920" height="1029" alt="Screenshot 2025-07-12 010556" src="https://github.com/user-attachments/assets/ae60d906-e708-49a1-a9b0-65a2165c54cb" />
<img width="1920" height="1029" alt="Screenshot 2025-07-12 010546" src="https://github.com/user-attachments/assets/3bfde71b-d9d9-4903-b901-5097c243dd05" />

📌 Author

🧠 Developed by: NIHARIKA MEENA
Cybersecurity Analyst | Bug Bounty Hunter
