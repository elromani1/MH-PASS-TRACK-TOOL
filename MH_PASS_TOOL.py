#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# =====================================================
# Tool Name : MHTOOL
# Module    : MH PASS TOOL
# Author    : Malek Al-Hakem
# Version   : 1.1
# Warning   : Use at your own risk
# =====================================================

import os
import sys
from itertools import permutations

# ================= Colors =================
RED = "\033[91m"
GRN = "\033[92m"
YLW = "\033[93m"
BLU = "\033[94m"
PUR = "\033[95m"
CYN = "\033[96m"
WHT = "\033[0m"

# ================= Deep Banner =================
def banner():
    os.system("clear")
    print(PUR + " ███╗   ███╗██╗  ██╗████████╗ ██████╗  ██████╗ ██╗     ")
    print(PUR + " ████╗ ████║██║  ██║╚══██╔══╝██╔═══██╗██╔═══██╗██║     ")
    print(PUR + " ██╔████╔██║███████║   ██║   ██║   ██║██║   ██║██║     ")
    print(PUR + " ██║╚██╔╝██║██╔══██║   ██║   ██║   ██║██║   ██║██║     ")
    print(PUR + " ██║ ╚═╝ ██║██║  ██║   ██║   ╚██████╔╝╚██████╔╝███████╗")
    print(PUR + " ╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝")
    print(CYN + "                 MHTOOL :: PASS GENERATOR\n")
    print(YLW + "        Author : Malek Al-Hakem")
    print(RED + "        [!] Use at your own risk\n" + WHT)

# ================= Confirmation =================
def confirm():
    print(RED + "[!] WARNING: This tool is for educational & authorized use only." + WHT)
    c = input(GRN + "[?] Press Y to continue: " + WHT).strip().lower()
    if c != "y":
        print(RED + "[x] Aborted." + WHT)
        sys.exit(0)

# ================= Core Logic =================
def product_lists(lists):
    if not lists:
        return [""]
    rest = product_lists(lists[1:])
    res = []
    for i in lists[0]:
        for r in rest:
            res.append(i + r)
    return res

def generate_passwords(data):
    passwords = set()
    fields = [v.lower() for v in data.values() if v]

    def variants(w):
        return {
            w,
            w + "123",
            w + "2024",
            w + "2025",
            w + "00",
            w + "99",
            w[::-1],
            w.capitalize()
        }

    var_lists = [variants(f) for f in fields]

    for v in var_lists:
        passwords.update(v)

    for r in [2, 3]:
        for combo in permutations(var_lists, r):
            passwords.update(product_lists(combo))

    return sorted(passwords)

# ================= Main =================
def main():
    banner()
    confirm()

    keys = [
        "name", "last_name", "birth_day", "birth_month", "birth_year",
        "phone", "city", "fav_name", "keyword1", "keyword2", "keyword3"
    ]

    print(BLU + "[*] Enter target information (leave blank if unknown)\n" + WHT)
    data = {}
    for k in keys:
        data[k] = input(CYN + f"{k}: " + WHT).strip()

    print(GRN + "\n[+] Generating passwords..." + WHT)
    pwds = generate_passwords(data)

    output = "MH_passwords.txt"
    with open(output, "w") as f:
        for p in pwds:
            f.write(p + "\n")

    print(GRN + f"[✓] Done! {len(pwds)} passwords generated" + WHT)
    print(YLW + f"[✓] Saved to: {output}\n" + WHT)

if __name__ == "__main__":
    main()
