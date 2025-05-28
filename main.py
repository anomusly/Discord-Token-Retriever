import sys
import platform
import os
import time
import re
from datetime import datetime
from pystyle import Write, Colors
from colorama import Fore, Style, init
import requests as anomus
from termcolor import colored

init(autoreset=True)

ascii = """
                ██████╗ ███████╗███████╗██╗██████╗ ███████╗
                ██╔══██╗██╔════╝██╔════╝██║██╔══██╗██╔════╝
                ██║  ██║█████╗  ███████╗██║██████╔╝█████╗
                ██║  ██║██╔══╝  ╚════██║██║██╔══██╗██╔══╝
                ██████╔╝███████╗███████║██║██║  ██║███████╗
                ╚═════╝ ╚══════╝╚══════╝╚═╝╚═╝  ╚═╝╚══════╝
                🚀 Ultimate Discord Token Retriever 🚀
"""

def clear():
    if platform.system() == 'Windows':
        os.system('cls & title Discord Token Retriever v1')
    elif platform.system() == 'Linux':
        os.system('clear')
        sys.stdout.write('\x1b]0;Discord Token Retriever v1\x07')
    elif platform.system() == 'Darwin':
        os.system("clear && printf '\\e[3J'")
        os.system('echo - n - e "\x1b]0;Discord Token Retriever v1\x07"')

def log_message(message, color='white'):
    timestamp = datetime.now().strftime("%H:%M:%S")
    print(colored(f"[{timestamp}] {message}", color))

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

clear()
log_message("🚀 Discord Token Retriever v1 - Initializing...", 'cyan')


HEADERS = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9",
    "Cache-Control": "no-cache",
    "Dnt": "1",
    "Pragma": "no-cache",
    "Priority": "u=1, i",
    "Referer": "https://discord.com/channels/@me",
    "Sec-Ch-Ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"Windows"',
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "X-Debug-Options": "bugReporterEnabled",
    "X-Discord-Locale": "en-US",
    "X-Discord-Timezone": "Asia/Calcutta",
    "X-Super-Properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyNi4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTI2LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjMwNzE3MSwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbCwiZGVzaWduX2lkIjowfQ=="
}

def login(email, password):
    """Attempt to login to Discord and retrieve token"""
    try:
        anomus_login = 'https://discord.com/api/v9/auth/login'
        anomus_payload = {'email': email, 'password': password}

        log_message(f"🔐 Attempting login for: {email}", 'yellow')

        anomus_response = anomus.post(anomus_login, json=anomus_payload, headers=HEADERS, timeout=10)

        if anomus_response.status_code == 200:
            anomus_data = anomus_response.json()
            anomus_token = anomus_data.get('token')
            if anomus_token:
                log_message(f"✅ Login successful for: {email}", 'green')
                return anomus_token
            else:
                log_message(f"❌ No token in response for: {email}", 'red')
                return None
        elif anomus_response.status_code == 400:
            log_message(f"❌ Invalid credentials for: {email}", 'red')
            return None
        elif anomus_response.status_code == 429:
            log_message(f"⚠️ Rate limited! Waiting 60 seconds...", 'yellow')
            time.sleep(60)
            return None
        else:
            log_message(f"❌ Login failed for {email} - Status: {anomus_response.status_code}", 'red')
            return None

    except anomus.exceptions.RequestException as e:
        log_message(f"🌐 Network error for {email}: {str(e)}", 'red')
        return None
    except Exception as e:
        log_message(f"💥 Unexpected error for {email}: {str(e)}", 'red')
        return None

def save_token(email, password, token):
    """Save token to multiple output files"""
    try:
        with open('tokens.txt', 'a', encoding='utf-8') as f:
            f.write(f'{token}\n')

        with open('evs.txt', 'a', encoding='utf-8') as f:
            f.write(f'{email}:{password}:{token}\n')

        with open('output.txt', 'a', encoding='utf-8') as f:
            f.write(f'{email}:{password}:{token}\n')

        log_message(f"💾 Token saved for: {email}", 'green')

    except Exception as e:
        log_message(f"💥 Error saving token for {email}: {str(e)}", 'red')

def process_emails():
    """Process email:password combinations from emails.txt"""
    try:
        if not os.path.exists('emails.txt'):
            log_message("❌ emails.txt file not found! Please create it with email:password combinations.", 'red')
            input("Press Enter to exit...")
            return

        with open('emails.txt', 'r', encoding='utf-8') as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]

        if not lines:
            log_message("❌ emails.txt is empty! Please add email:password combinations.", 'red')
            input("Press Enter to exit...")
            return

        log_message(f"📧 Found {len(lines)} email combinations to process", 'cyan')

        successful = 0
        failed = 0

        for i, line in enumerate(lines, 1):
            try:
                if ':' not in line:
                    log_message(f"⚠️ Invalid format in line {i}: {line}", 'yellow')
                    failed += 1
                    continue

                parts = line.split(':', 1) 
                if len(parts) != 2:
                    log_message(f"⚠️ Invalid format in line {i}: {line}", 'yellow')
                    failed += 1
                    continue

                email, password = parts
                email = email.strip()
                password = password.strip()

                if not validate_email(email):
                    log_message(f"⚠️ Invalid email format: {email}", 'yellow')
                    failed += 1
                    continue

                log_message(f"📊 Processing {i}/{len(lines)}: {email}", 'cyan')

                token = login(email, password)
                if token:
                    save_token(email, password, token)
                    successful += 1
                    log_message(f"🎉 Success: {email}", 'green')
                else:
                    failed += 1
                    log_message(f"💔 Failed: {email}", 'red')

                if i < len(lines):
                    log_message("⏳ Waiting 3 seconds before next request...", 'yellow')
                    time.sleep(3)

            except Exception as e:
                log_message(f"💥 Error processing line {i}: {str(e)}", 'red')
                failed += 1
                continue

        log_message(f"📊 Processing complete! ✅ Success: {successful} | ❌ Failed: {failed}", 'cyan')

    except Exception as e:
        log_message(f"💥 Critical error in process_emails: {str(e)}", 'red')

    input("Press Enter to exit...")

if __name__ == '__main__':
    try:
        Write.Print(ascii, Colors.purple_to_blue, interval=0.01)
        log_message("🎯 Discord Token Retriever v1 - Ready!", 'green')
        log_message("📝 Make sure your emails.txt contains email:password combinations", 'yellow')
        time.sleep(2)
        process_emails()
    except KeyboardInterrupt:
        log_message("\n🛑 Process interrupted by user", 'yellow')
    except Exception as e:
        log_message(f"💥 Critical error: {str(e)}", 'red')
        input("Press Enter to exit...")
