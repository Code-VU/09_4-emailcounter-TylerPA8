def countEmail():
    # This first line is provided for you
    name = input("Enter file:")
    if len(name) < 1 : name = "mbox-short.txt"
    senders ={}
    with open(name) as file:
        for line in file:
            if line.startswith("From "):
                line = line.strip()
                line = line.split()
                senders[line[1]] = senders.get(line[1], 0) + 1
    bigsender = max(senders, key = senders.get)
    print(bigsender, max(senders.values()) )

## if you want to test locally run > python counter.py
if __name__ == "__main__":
    countEmail()
