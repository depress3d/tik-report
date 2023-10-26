import sys
import os
import requests
import random
import time

try:
    import colorama
except ImportError as e:
    input(f"Package {e} is not installed")
    sys.exit(f"pip install {e}")

class ReportThread:
    def __init__(self, url):

        self.url = url
        self.default_headers = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 OPR/100.0.0.0",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 OPR/100.0.0.0",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 OPR/100.0.0.0",
            "Mozilla/5.0 (Linux; Android 12; SM-G993U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5005.115 Mobile Safari/537.36",
            "Mozilla/5.0 (Linux; Android 12; SM-G998U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5005.115 Mobile Safari/537.36",
            "Mozilla/5.0 (Linux; Android 12; SM-G992U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5005.115 Mobile Safari/537.36",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/16A5367e Safari/604.1",
            "Mozilla/5.0 (iPad; CPU iPadOS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/16A5367e Safari/604.1",
            "Mozilla/5.0 (iPod touch; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/16A5367e Safari/604.1",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_0_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Safari/605.1.15",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5005.115 Safari/537.36 Edg/103.0.5005.115",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5005.115 Safari/537.36 Vivaldi/6.1.3035.257",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5005.115 Brave/1.43.120",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5005.115 Safari/537.36",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5005.115 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5005.115 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5005.115 Safari/537.36 EdgHTML/103.0.5005.115",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5005.115 Safari/537.36",
            "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)",
            "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)",
            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
            "Mozilla/5.0 (Linux; Android 12; SM-G993U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5005.115 Mobile Safari/537.36",
            "Mozilla/5.0 (Linux; Android 12; SM-G998U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5005.115 Mobile Safari/537.36",
            "Mozilla/5.0 (Linux; Android 12; SM-G992U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5005.115 Mobile Safari/537.36",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/16A5367e Safari/604.1",
            "Mozilla/5.0 (iPad; CPU iPadOS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/16A5367e Safari/604.1",
            "Mozilla/5.0 (iPod touch; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/16A5367e Safari/604.1",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_0_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Safari/605.1.15",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5005.115 Safari/537.36 Edg/103.0.5005.115",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5005.115 Safari/537.36 Vivaldi/6.1.3035.257",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5005.115 Brave/1.43.120"
        ]
        self.accept_languages = [
           "en-US,en;q=0.9",
            "en-GB,en;q=0.8",
            "fr-FR,fr;q=0.9",
            "es-ES,es;q=0.9",
            "de-DE,de;q=0.9",
            "it-IT,it;q=0.9",
            "pt-PT,pt;q=0.9",
            "nl-NL,nl;q=0.9",
            "sv-SE,sv;q=0.9",
            "no-NO,no;q=0.9",
            "da-DK,da;q=0.9",
            "fi-FI,fi;q=0.9",
            "pl-PL,pl;q=0.9",
            "ru-RU,ru;q=0.9",
            "tr-TR,tr;q=0.9",
            "ja-JP,ja;q=0.9",
            "ko-KR,ko;q=0.9",
            "zh-CN,zh;q=0.9",
            "ar-SA,ar;q=0.9",
            "hi-IN,hi;q=0.9",
            "he-IL,he;q=0.9",
            "th-TH,th;q=0.9",
            "vi-VN,vi;q=0.9",
            "id-ID,id;q=0.9",
            "ms-MY,ms;q=0.9",
            "fil-PH,fil;q=0.9",
            "cs-CZ,cs;q=0.9",
            "hu-HU,hu;q=0.9",
            "el-GR,el;q=0.9",
            "uk-UA,uk;q=0.9",
            "ro-RO,ro;q=0.9",
            "hr-HR,hr;q=0.9",
            "sr-RS,sr;q=0.9",
            "bg-BG,bg;q=0.9",
            "sk-SK,sk;q=0.9",
            "sl-SI,sl;q=0.9",
            "et-EE,et;q=0.9",
            "lv-LV,lv;q=0.9",
            "lt-LT,lt;q=0.9",
            "pl-PL,pl;q=0.9",
            "hu-HU,hu;q=0.9",
            "ro-RO,ro;q=0.9",
            "hr-HR,hr;q=0.9",
            "sr-RS,sr;q=0.9",
            "bg-BG,bg;q=0.9",
            "sk-SK,sk;q=0.9",
            "sl-SI,sl;q=0.9",
            "et-EE,et;q=0.9",
            "lv-LV,lv;q=0.9",
            "lt-LT,lt;q=0.9"
        ]
        self.other_headers = {
            "Referer": "https://www.google.com/",
            "Connection": "keep-alive",
            "DNT": "1",
            "Upgrade-Insecure-Requests": "1",
            "Cache-Control": "max-age=0",
            "TE": "Trailers"
        }

    def run(self):
        total_reports = 0
        reports_per_second = 0
        last_report_time = time.time()

        while True:
            user_agent = random.choice(self.default_headers)
            accept_language = random.choice(self.accept_languages)
            headers = {
                "User-Agent": user_agent,
                "Accept-Language": accept_language,
                **self.other_headers,
            }

            response = requests.post(self.url, headers=headers)

            if response.status_code == 200:
                total_reports += 1
                reports_per_second = total_reports / (time.time() - last_report_time)
                last_report_time = time.time()

                output_text = f"\n[+] Reports sent: {total_reports} ({reports_per_second:.2f} reports/min) Current User-Agent: {user_agent} Current Accept-Language: {accept_language}"
                print(output_text)
            else:
                print("[-] Report failed")

if __name__ == '__main__':

     os.system("cls" if os.name == "nt" else "clear")

     text = '''

 ▄████▄▓██   ██▓ ▄▄▄▄   ▓█████  ██▀███     ▓█████▄  ██▀███   ▄▄▄        ▄████  ▒█████   ███▄    █ ▒███████▒
▒██▀ ▀█ ▒██  ██▒▓█████▄ ▓█   ▀ ▓██ ▒ ██▒   ▒██▀ ██▌▓██ ▒ ██▒▒████▄     ██▒ ▀█▒▒██▒  ██▒ ██ ▀█   █ ▒ ▒ ▒ ▄▀░
▒▓█    ▄ ▒██ ██░▒██▒ ▄██▒███   ▓██ ░▄█ ▒   ░██   █▌▓██ ░▄█ ▒▒██  ▀█▄  ▒██░▄▄▄░▒██░  ██▒▓██  ▀█ ██▒░ ▒ ▄▀▒░ 
▒▓▓▄ ▄██▒░ ▐██▓░▒██░█▀  ▒▓█  ▄ ▒██▀▀█▄     ░▓█▄   ▌▒██▀▀█▄  ░██▄▄▄▄██ ░▓█  ██▓▒██   ██░▓██▒  ▐▌██▒  ▄▀▒   ░
▒ ▓███▀ ░░ ██▒▓░░▓█  ▀█▓░▒████▒░██▓ ▒██▒   ░▒████▓ ░██▓ ▒██▒ ▓█   ▓██▒░▒▓███▀▒░ ████▓▒░▒██░   ▓██░▒███████▒
░ ░▒ ▒  ░ ██▒▒▒ ░▒▓███▀▒░░ ▒░ ░░ ▒▓ ░▒▓░    ▒▒▓  ▒ ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░ ░▒   ▒ ░ ▒░▒░▒░ ░ ▒░   ▒ ▒ ░▒▒ ▓░▒░▒
  ░  ▒  ▓██ ░▒░ ▒░▒   ░  ░ ░  ░  ░▒ ░ ▒░    ░ ▒  ▒   ░▒ ░ ▒░  ▒   ▒▒ ░  ░   ░   ░ ▒ ▒░ ░ ░░   ░ ▒░░░▒ ▒ ░ ▒
░       ▒ ▒ ░░   ░    ░    ░     ░░   ░     ░ ░  ░   ░░   ░   ░   ▒   ░ ░   ░ ░ ░ ░ ▒     ░   ░ ░ ░ ░ ░ ░ ░
░ ░     ░ ░      ░         ░  ░   ░           ░       ░           ░  ░      ░     ░ ░           ░   ░ ░    
                                        (Ramay Shex Ali - IFML)
'''
     print(f'{colorama.Fore.RED}{text}{colorama.Style.RESET_ALL}')

     target_url = input(f" {colorama.Fore.RED} Insert the Target URL from Inspect Element: ").strip()

     if not target_url:
        print("[-] Please enter a valid target URL.")
        sys.exit(1)

     report_thread = ReportThread(target_url)
     report_thread.run()
