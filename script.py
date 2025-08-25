#!/usr/bin/env python3
print(r"""

░██████╗░██╗████████╗███████╗░█████╗░  ██╗░░██╗░█████╗░░██████╗██╗░░██╗
██╔════╝░██║╚══██╔══╝██╔════╝██╔══██╗  ██║░░██║██╔══██╗██╔════╝██║░░██║
██║░░██╗░██║░░░██║░░░█████╗░░███████║  ███████║███████║╚█████╗░███████║
██║░░╚██╗██║░░░██║░░░██╔══╝░░██╔══██║  ██╔══██║██╔══██║░╚═══██╗██╔══██║
╚██████╔╝██║░░░██║░░░███████╗██║░░██║  ██║░░██║██║░░██║██████╔╝██║░░██║
░╚═════╝░╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝  ╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝

░█████╗░██████╗░░██████╗░░█████╗░███╗░░██╗██╗███████╗███████╗██████╗░
██╔══██╗██╔══██╗██╔════╝░██╔══██╗████╗░██║██║╚════██║██╔════╝██╔══██╗
██║░░██║██████╔╝██║░░██╗░███████║██╔██╗██║██║░░███╔═╝█████╗░░██████╔╝
██║░░██║██╔══██╗██║░░╚██╗██╔══██║██║╚████║██║██╔══╝░░██╔══╝░░██╔══██╗
╚█████╔╝██║░░██║╚██████╔╝██║░░██║██║░╚███║██║███████╗███████╗██║░░██║
░╚════╝░╚═╝░░╚═╝░╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝╚══════╝╚══════╝╚═╝░░╚═╝

      """)

import argparse

def format_hash(iterations, salt, hash_value):

    john = f"$pbkdf2-sha256${iterations}.{salt}${hash_value}"

    hashcat = f"sha256:{iterations}:{salt}:{hash_value}"

    return john, hashcat


def main():
    parser = argparse.ArgumentParser(description="Format Gitea PBKDF2 hashes for cracking tools.")
    parser.add_argument("-i", "--iterations", required=True, help="Number of PBKDF2 iterations (e.g. 50000)")
    parser.add_argument("-s", "--salt", required=True, help="Salt (hex string from DB)")
    parser.add_argument("-H", "--hash", required=True, help="Hash (derived key in hex)")

    args = parser.parse_args()

    john, hashcat = format_hash(args.iterations, args.salt, args.hash)

    print("\n[+] John the Ripper format:")
    print(john)
    print("\n[+] Hashcat format (-m 10900):")
    print(hashcat)
    print()


if __name__ == "__main__":
    main()
