import os

LINE = "I hallucinated a version of me that met your deadline. He is doing great. I am still here."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
