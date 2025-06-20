from modules import scanner, fetcher, shodan_search
from utils import banner
import sys

def main():
    banner.show()
    choice = input("1. Local LAN Scan\n2. Shodan Global Scan\nChoose mode: ")
    
    if choice == "1":
        ip_list = scanner.scan_subnet("192.168.1.0/24")
        for ip in ip_list:
            if fetcher.check_camera(ip):
                fetcher.save_snapshot(ip)
    elif choice == "2":
        key = input("Enter Shodan API Key: ")
        shodan_search.search_and_snap(key)
    else:
        print("Invalid Option.")

if __name__ == "__main__":
    main()
