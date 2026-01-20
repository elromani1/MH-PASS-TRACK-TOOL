#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import time
from itertools import permutations

# =========================
# Banner
# =========================
def banner():
    os.system("clear")
    print("""

███╗   ███╗ ██╗  ██╗ ████████╗  ██████╗  ██████╗ ██╗     
████╗ ████║ ██║  ██║ ╚══██╔══╝ ██╔═══╝ ██╔═══╝ ██║     
██╔████╔██║ ███████║    ██║    ██████╗  ██████╗ ██║     
██║╚██╔╝██║ ██╔══██║    ██║    ██╔═══╝  ██╔══██╗ ██║     
██║ ╚═╝ ██║ ██║  ██║    ██║    ██║      ██████╔╝ ███████╗
╚═╝     ╚═╝ ╚═╝  ╚═╝    ╚═╝    ╚═╝      ╚═════╝  ╚══════╝
        ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
        ▌   M H T O O L  |  ATTACK   ▐
        ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
     [!] Ethical Hacking Tool
     [!] Use For Awareness & Testing Only

        MH PASS TOOL
        Coded By: Malek Elhakem
        Educational & Ethical Use Only
""")
    time.sleep(1)

# =========================
# Password Logic
# =========================
def product_lists(lists):
    if not lists:
        return [""]
    rest = product_lists(lists[1:])
    result = []
    for item in lists[0]:
        for r_item in rest:
            result.append(item + r_item)
    return result

def variants(word):
    return {
        word,
        word + "123",
        word + "1234",
        word + "2024",
        word + "2025",
        word + "2026",
        word + "00",
        word + "99",
        word[::-1],
        word.capitalize(),
    }

def generate_passwords(data):
    passwords = set()
    fields = [str(v).lower() for v in data.values() if v.strip()]

    var_lists = [variants(f) for f in fields]

    for v in var_lists:
        passwords.update(v)

    for r in [2, 3]:
        for combo in permutations(var_lists, r):
            passwords.update(product_lists(combo))

    return sorted(passwords)

# =========================
# Main Tool
# =========================
def main():
    banner()

    print("[+] Enter Target Information\n")

    keys = [
        "Name",
        "Last Name",
        "Birth Day",
        "Birth Month",
        "Birth Year",
        "Phone Number",
        "Favorite Number",
        "Favorite Name",
        "City",
        "Keyword 1",
        "Keyword 2",
        "Keyword 3",
        "Keyword 4",
        "Keyword 5",
        "Keyword 6",
        "Keyword 7",
        "Keyword 8",
        "Keyword 9"
    ]

    data = {}
    for k in keys:
        data[k] = input(f"{k}: ").strip()

    passwords = generate_passwords(data)

    print(f"\n[✔] Generated {len(passwords)} passwords")

    save_path = input("\n[+] Enter path to save result (example: /home/kali/Desktop): ").strip()
    os.makedirs(save_path, exist_ok=True)

    file_path = os.path.join(save_path, "MH_PASSWORDS.txt")

    with open(file_path, "w") as f:
        for pwd in passwords:
            f.write(pwd + "\n")

    print(f"\n[✔] Password list saved successfully")
    print(f"[✔] File location: {file_path}")

# =========================
# Run
# =========================
if __name__ == "__main__":
    main()

