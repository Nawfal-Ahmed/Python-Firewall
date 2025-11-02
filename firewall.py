#!/usr/bin/env python3
import os

def block_port(port):
    """Block incoming and outgoing TCP traffic on a specific port."""
    print(f"\n[+] Blocking port {port} ...")
    os.system(f"sudo iptables -A INPUT -p tcp --dport {port} -j DROP")
    os.system(f"sudo iptables -A OUTPUT -p tcp --dport {port} -j DROP")
    print(f"[✓] Port {port} is now blocked.")

def unblock_port(port):
    """Remove the blocking rule for the given port."""
    print(f"\n[+] Unblocking port {port} ...")
    os.system(f"sudo iptables -D INPUT -p tcp --dport {port} -j DROP")
    os.system(f"sudo iptables -D OUTPUT -p tcp --dport {port} -j DROP")
    print(f"[✓] Port {port} is now unblocked.")

def show_rules():
    """Display current iptables rules."""
    print("\n[+] Current iptables rules:")
    os.system("sudo iptables -L -n --line-numbers")

def clear_all_rules():
    """Flush all firewall rules."""
    print("\n[!] Clearing all iptables rules...")
    os.system("sudo iptables -F")
    print("[✓] All rules cleared.")

def main():
    while True:
        print("\n========== Python Firewall ==========")
        print("1. Block a port")
        print("2. Unblock a port")
        print("3. View current rules")
        print("4. Clear all rules")
        print("5. Exit")
        print("====================================")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            port = input("Enter port number to block: ").strip()
            if port.isdigit():
                block_port(port)
            else:
                print("Invalid port number.")
        elif choice == "2":
            port = input("Enter port number to unblock: ").strip()
            if port.isdigit():
                unblock_port(port)
            else:
                print("Invalid port number.")
        elif choice == "3":
            show_rules()
        elif choice == "4":
            confirm = input("Are you sure you want to clear all rules? (y/n): ").lower()
            if confirm == "y":
                clear_all_rules()
        elif choice == "5":
            print("Exiting firewall control...")
            break
        else:
            print("Invalid option, try again.")

if __name__ == "__main__":
    main()
