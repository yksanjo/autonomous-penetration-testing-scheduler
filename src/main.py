from datetime import datetime, timezone


def main() -> None:
    print("autonomous-penetration-testing-scheduler initialized at", datetime.now(timezone.utc).isoformat())


if __name__ == "__main__":
    main()
