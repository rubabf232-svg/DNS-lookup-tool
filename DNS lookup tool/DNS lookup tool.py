import socket

print("=" * 50)
print("           DNS Lookup Tool")
print("=" * 50)

domain = input("Enter domain (example.com): ").strip()

try:
    ip = socket.gethostbyname(domain)

    print("\nLookup Result")
    print("-" * 30)
    print("Domain :", domain)
    print("IP Address :", ip)

except socket.gaierror:
    print("Invalid domain or DNS lookup failed.")