import sys


def main() -> None:
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===")
    print("-" * 50)

    archivist_id = input("Input Stream active. Enter archivist ID: ")
    status_report = input("Input Stream active. Enter status report: ")

    print("-" * 50)

    print(f"[STANDARD] Archive status from {archivist_id}: {status_report}")

    print("[ALERT] System diagnostic: Communication"
          " channels verified", file=sys.stderr)

    print("[STANDARD] Data transmission complete")

    print("-" * 50)
    print("Three-channel communication test successful.")


if __name__ == "__main__":
    main()
