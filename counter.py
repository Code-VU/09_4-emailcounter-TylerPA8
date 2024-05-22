def countEmail():
    # This first line is provided for you
    name = input("Enter file:")
    if len(name) < 1 : name = "mbox-short.txt"
    senders ={}
    with open(name) as file:
        for lines in file:
            if lines.startswith("From "):
                lines = lines.strip()
                lines = lines.split()
                senders[lines[1]] = senders.get(lines[1], 0) + 1
    bigsender = max(senders, key = senders.get)
    print(bigsender, max(senders.values()) )

## if you want to test locally run > python counter.py
if __name__ == "__main__":
    countEmail()
