
import argparse
import requests
import re
import os
from urllib.parse import urlparse, parse_qs
from bs4 import BeautifulSoup

# Stylish banner
def banner():
    print("""
\033[1;36m
██████╗ ███████╗██║       ██║ ███████╗ █████╗ ██╗     ██████╗ ███████╗ ██████╗ ██████╗ ███╗    ██╗ 
██╔══██╗██╔════╝║██║     ██║  ██╔════╝██╔══██╗██║     ██╔══██╗██╔════╝██╔════╝██╔═══██╗████╗  ██║
██████╔╝█████╗   ║██║   ██║   █████╗  ███████║██║     ██████╔╝█████╗  ██║      ██║   ██║██╔██╗ ██║
██╔══██╗██╔══╝    ║██  ██║    ██╔══╝  ██╔══██║██║     ██╔══██╗██╔══╝  ██║      ██║   ██║██║╚██╗██║
██║  ██║███████╗    ║██║      ███████╗██║  ██║███████╗██║  ██║███████╗╚██████╗╚██████╔╝██║ ╚████║
╚═╝  ╚═╝╚══════╝    ╚══╝      ╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝
                                                                                        -by NIH@RIK@
\033[0m
    """)

# Output saving
def save_output(data, filename):
    os.makedirs("output", exist_ok=True)
    with open(os.path.join("output", filename), "w") as f:
        f.write("\n".join(sorted(set(data))))

# Check if URL is alive
def is_alive(url):
    try:
        res = requests.head(url, timeout=3, allow_redirects=True)
        return res.status_code < 400
    except:
        return False

# Discover basic subdomains
def discover_subdomains(domain):
    subdomains = set()
    wordlist = ['www', 'mail', 'test', 'dev', 'api', 'beta']
    for word in wordlist:
        sub = f"http://{word}.{domain}"
        if is_alive(sub):
            subdomains.add(sub)
    return subdomains

# Crawl basic URLs
def discover_urls(domain):
    urls = set()
    base_url = f"http://{domain}"
    try:
        res = requests.get(base_url, timeout=5)
        soup = BeautifulSoup(res.text, 'html.parser')
        for a in soup.find_all("a", href=True):
            href = a["href"]
            if href.startswith("/"):
                href = f"{base_url}{href}"
            if domain in href:
                urls.add(href)
    except:
        pass
    return urls

# Extract parameterized URLs
def extract_params(urls):
    return [u for u in urls if "?" in u]

# Extract extension-based URLs
def extract_extensions(urls, extensions=[".js", ".json", ".php", ".aspx", ".zip"]):
    return [u for u in urls if any(u.lower().endswith(ext) for ext in extensions)]

# Leak detection
def detect_leaks(urls):
    leaks = []
    email_regex = r"[\w.-]+@[\w.-]+\.\w+"
    ip_regex = r"(?<!\d)(?:\d{1,3}\.){3}\d{1,3}(?!\d)"
    tech_regex = r"(apache|nginx|php|mysql|express|flask|django|node\.js|tomcat)"
    for url in urls:
        try:
            res = requests.get(url, timeout=3)
            content = res.text
            leaks += re.findall(email_regex, content)
            leaks += re.findall(ip_regex, content)
            leaks += re.findall(tech_regex, content, re.IGNORECASE)
        except:
            pass
    return set(leaks)

# Main
def main():
    parser = argparse.ArgumentParser(description="RevealRecon - Subdomain & URL Discovery Tool")
    parser.add_argument("domain", help="Target domain name (e.g., example.com)")
    parser.add_argument("--params", action="store_true", help="Show URLs with parameters")
    parser.add_argument("--ext", action="store_true", help="Show URLs with file extensions")
    parser.add_argument("--live", action="store_true", help="Show only live URLs/subdomains")
    parser.add_argument("--leaks", action="store_true", help="Display sensitive info leaks")
    args = parser.parse_args()

    banner()

    domain = args.domain
    print(f"[+] Target: {domain}\n")

    # Subdomain Discovery
    print("[*] Discovering subdomains...")
    subdomains = discover_subdomains(domain)
    if args.live:
        subdomains = [s for s in subdomains if is_alive(s)]
    print("\n[+] Subdomains Found:")
    for s in subdomains:
        print(f"  - {s}")
    save_output(subdomains, "subdomains.txt")

    # URL Discovery
    print("\n[*] Crawling URLs...")
    urls = discover_urls(domain)
    if args.live:
        urls = [u for u in urls if is_alive(u)]
    print("\n[+] URLs Found:")
    for u in urls:
        print(f"  - {u}")
    save_output(urls, "urls.txt")

    # Parameterized URLs
    if args.params:
        param_urls = extract_params(urls)
        print("\n[+] Parameterized URLs:")
        for pu in param_urls:
            print(f"  - {pu}")
        save_output(param_urls, "urls_with_params.txt")

    # Extension-based URLs
    if args.ext:
        ext_urls = extract_extensions(urls)
        print("\n[+] URLs with Extensions:")
        for eu in ext_urls:
            print(f"  - {eu}")
        save_output(ext_urls, "urls_with_ext.txt")

    # Leak Detection
    if args.leaks:
        print("\n[*] Scanning for sensitive leaks...")
        leaks = detect_leaks(urls)
        if leaks:
            print("\n[+] Leaks Found:")
            for item in leaks:
                print(f"  - {item}")
            save_output(leaks, "leaks_found.txt")
        else:
            print("[-] No obvious leaks detected.")

    print("\n[✓] All results saved in 'output/' directory.")

if __name__ == "__main__":
    main()
