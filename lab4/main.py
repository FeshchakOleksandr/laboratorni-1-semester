from colorama_mod import run_colorama
from emoji_mod import run_emoji
from cowsay_mod import run_cowsay
from art_mod import run_art
from tabulate_mod import run_tabulate
from humanize_mod import run_humanize
from validators_mod import run_validators
from requests_mod import run_requests
from pyfiglet_mod import run_pyfiglet
from bs4_mod import run_bs4

from math_mod import run_math
from random_mod import run_random
from datetime_mod import run_datetime
from os_mod import run_os
from json_mod import run_json

def main():
    print("=== ВИКОНАННЯ ЛАБОРАТОРНОЇ РОБІТИ №4 ===\n")
    
    print("1. Colorama:")
    run_colorama()
    
    print("\n2. Emoji:")
    run_emoji()
    
    print("\n3. Cowsay:")
    run_cowsay()
    
    print("\n4. Art:")
    run_art()
    
    print("\n5. Tabulate:")
    run_tabulate()
    
    print("\n6. Humanize:")
    run_humanize()
    
    print("\n7. Validators:")
    run_validators()
    
    print("\n8. Requests:")
    run_requests()
    
    print("\n9. Pyfiglet:")
    run_pyfiglet()
    
    print("\n10. BeautifulSoup:")
    run_bs4()
    
    print("\n11. Math (вбудована):")
    run_math()
    
    print("\n12. Random (вбудована):")
    run_random()
    
    print("\n13. Datetime (вбудована):")
    run_datetime()
    
    print("\n14. OS (вбудована):")
    run_os()
    
    print("\n15. JSON (вбудована):")
    run_json()
    
    print("\n=== ВСЕ УСПІШНО ВИКОНАНО ===")

if __name__ == "__main__":
    main()