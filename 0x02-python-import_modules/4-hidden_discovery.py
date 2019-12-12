#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    a = dir(hidden_4)
    a.sort
    for i in range(len(a)):
        if not a[i].startswith("__"):
            print(a[i])
        a[i]
