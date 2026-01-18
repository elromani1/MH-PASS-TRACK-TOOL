#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import time
import sys

# =========================
# Banner Function
# =========================
def banner():
    os.system("clear")
    print("""
███╗   ███╗ ██╗  ██╗ ████████╗ ██████╗  ██████╗ ██╗     
████╗ ████║ ██║  ██║ ╚══██╔══╝ ██╔══██╗ ██╔═══╝ ██║     
██╔████╔██║ ███████║    ██║    ██████╔╝ ██████╗ ██║     
██║╚██╔╝██║ ██╔══██║    ██║    ██╔═══╝  ██╔══██╗ ██║     
██║ ╚═╝ ██║ ██║  ██║    ██║    ██║      ██████╔╝ ███████╗
╚═╝     ╚═╝ ╚═╝  ╚═╝    ╚═╝    ╚═╝      ╚═════╝  ╚══════╝

        MH PASS TOOL
        Coded By: Malek Elhakem
        For Educational & Ethical Use Only
""")
    time.sleep(2)

# =========================
# Main Tool
# =========================
def main():
    banner()

    print("[+] Welcome to MH PASS TOOL\n")

    # طلب البيانات بدل ملف
    target = input("[+] Enter Target Name/IP: ").strip()
    username = input("[+] Enter Username: ").strip()
    note = input("[+] Any Notes (optional): ").strip()

    print("\n[+] Where do you want to save the result?")
    save_path = input("[+] Enter full path (example: /home/kali/Desktop): ").strip()

    # إنشاء المجلد لو مش موجود
    try:
        os.makedirs(save_path, exist_ok=True)
    except Exception as e:
        print(f"[X] Path Error: {e}")
        sys.exit()

    # اسم الملف
    file_name = "MH_Result.txt"
    full_path = os.path.join(save_path, file_name)

    # محتوى الملف
    result = f"""
==============================
 MH PASS TOOL RESULT
==============================
Target   : {target}
Username : {username}
Notes    : {note}

Tool     : MH PASS TOOL
Author   : Malek Elhakem
Status   : Completed Successfully
==============================
"""

    # حفظ البيانات
    try:
        with open(full_path, "a") as f:
            f.write(result)

        print("\n[✔] Done!")
        print(f"[✔] Result saved in: {full_path}")

    except Exception as e:
        print(f"[X] Failed to save file: {e}")

# =========================
# Run Tool
# =========================
if __name__ == "__main__":
    main()
