import os
import argparse

SUPHELI = ["error", "failed", "unauthorized", "denied"]

def watch_log(file_path):
    found_supheli = False

    for file in os.listdir(file_path):
        filepath = os.path.join(file_path, file)

        if os.path.isfile(filepath) and file.endswith(".log"):
            with open(filepath, "r", errors="ignore") as f:
                for line in f:
                    if any(word in line.lower() for word in SUPHELI):
                        print(f"[!] Şüpheli işlem bulundu: {file} → {line.strip()}")
                        found_supheli = True

    if not found_supheli:
        print("[+] Bir problem yok.")

def main():
    parser = argparse.ArgumentParser(
        description="LogVigil - Mini Log izleme aracı."
    )
    parser.add_argument(
        "--path", "-p", type=str, default="/var/log",
        help="Log dosyasının yolu (default: /var/log)"
    )

    args = parser.parse_args()
    watch_log(args.path)

if __name__ == "__main__":
    main()
