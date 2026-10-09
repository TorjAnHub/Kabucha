import os
import time
import random
import string
import subprocess

os.system("clear" if os.name != "nt" else "cls")

YELLOW = "\033[93m"
WHITE = "\033[97m"
RED = "\033[91m"
DARK_RED = "\033[31m"
GRAY = "\033[90m"
RESET = "\033[0m"

BANNER = r"""
 ██  ██   ███   █████▄ ▄█  █▄ ▄█████ ▄█  █▄   ███
 ██▄█▀   ██ ██  ██ ▄█▀ ██  ██ ██     ██▄▄██  ██ ██
 ██▀█▄  ██▀▀▀██ ██ ▀█▄ ██  ██ ██     ██▀▀██ ██▀▀▀██
 ██  ██  ██ ██  █████▀ ▀████▀ ▀█████ ▀█  █▀  ██ ██
"""

TARGET_ID = "SS40022d-x.z12d3"
TARGET_IMG = "https://k.top4top.io/p_3934krzkh1.png"

def open_url(url):
    try:
        subprocess.run(["xdg-open", url], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except Exception:
        try:
            subprocess.run(["sensible-browser", url], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except Exception:
            pass

def loading_anim(seconds=3):
    dots = ["Loading...", "Loading..", "Loading."]
    end_time = time.time() + seconds
    i = 0
    while time.time() < end_time:
        print(f"\r{dots[i % 3]}", end="", flush=True)
        time.sleep(0.5)
        i += 1
    print("\r          \r", end="", flush=True)

def cyber_reveal_link(target_url):
    chars = string.ascii_letters + string.digits + ":/._-"
    revealed = ""
    print("Decrypting Link: ", end="", flush=True)
    
    for real_char in target_url:
        for _ in range(3):
            fake_char = random.choice(chars)
            print(f"\rDecrypting Link: {revealed}{DARK_RED}{fake_char}{RESET}", end="", flush=True)
            time.sleep(0.05)
        revealed += real_char
        print(f"\rDecrypting Link: {revealed}", end="", flush=True)
        time.sleep(0.4)
    
    print("\n")

def draw_normal_header():
    os.system("clear" if os.name != "nt" else "cls")
    print(BANNER)
    print(f"OSINT\n{GRAY}v1.0{RESET}\n")

def draw_dark_header():
    os.system("clear" if os.name != "nt" else "cls")
    print(f"{DARK_RED}{BANNER}{RESET}")
    print(f"{DARK_RED}OSINT\nv1.0{RESET}\n")

def run_dark_session():
    draw_dark_header()
    while True:
        dark_cmd = input("> ").strip()
        if not dark_cmd:
            continue

        if dark_cmd.lower() == "snapchat":
            user_id_input = input("User ID: ").strip()
            if user_id_input == TARGET_ID:
                loading_anim(5)
                draw_dark_header()
                cyber_reveal_link(TARGET_IMG)
                open_url(TARGET_IMG)

                while True:
                    back_cmd = input("> ").strip()
                    if back_cmd.lower() == "back":
                        draw_dark_header()
                        break
            else:
                loading_anim(3)
                print(f"{WHITE}Invalid User ID{RESET}\n")

        elif dark_cmd.lower() == "back":
            draw_normal_header()
            break
        else:
            loading_anim(3)
            print(f"{WHITE}Command: {dark_cmd}{RESET}")
            print(f"{WHITE}Status: Not Recognized{RESET}\n")

draw_normal_header()

while True:
    query = input("> ").strip()
    if not query:
        continue

    if query.lower() == "dark":
        pwd = input("Password: ").strip()
        if pwd == "123":
            run_dark_session()
        else:
            print(f"{WHITE}Access Denied{RESET}\n")
        continue

    loading_anim(3)

    if "nrmeenyastta" in query.lower() or "snapchat.com/@nrmeenyastta" in query.lower():
        print(f"Platform: {YELLOW}Snapchat{RESET}")
        print(f"Name: {WHITE}𖤓🌐📍N{RESET}")
        print(f"Username: {WHITE}@nrmeenyastta{RESET}")
        print(f"User ID: {WHITE}{TARGET_ID}{RESET}")
        print(f"Profile Link: {WHITE}https://snapchat.com/add/nrmeenyastta{RESET}")
        print("-" * 35)

        while True:
            sub_query = input("> ").strip()
            if not sub_query:
                continue

            if sub_query.lower() == "dark":
                pwd = input("Password: ").strip()
                if pwd == "123":
                    run_dark_session()
                    print(f"Platform: {YELLOW}Snapchat{RESET}")
                    print(f"Name: {WHITE}𖤓🌐📍N{RESET}")
                    print(f"Username: {WHITE}@nrmeenyastta{RESET}")
                    print(f"User ID: {WHITE}{TARGET_ID}{RESET}")
                    print(f"Profile Link: {WHITE}https://snapchat.com/add/nrmeenyastta{RESET}")
                    print("-" * 35)
                else:
                    print(f"{WHITE}Access Denied{RESET}\n")
                continue

            if sub_query.lower() == "back":
                draw_normal_header()
                break

            loading_anim(3)
            draw_normal_header()
            cyber_reveal_link(TARGET_IMG)
            open_url(TARGET_IMG)

            while True:
                inner_query = input("> ").strip()
                if inner_query.lower() == "dark":
                    pwd = input("Password: ").strip()
                    if pwd == "123":
                        run_dark_session()
                        draw_normal_header()
                        print(f"Image Link: {WHITE}{TARGET_IMG}{RESET}\n")
                    else:
                        print(f"{WHITE}Access Denied{RESET}\n")
                    continue

                if inner_query.lower() == "back":
                    draw_normal_header()
                    break

            if inner_query.lower() == "back":
                break

    else:
        print(f"Target: {WHITE}{query}{RESET}")
        print(f"Status: {WHITE}Not Found{RESET}\n")
