try:
    with open("Tempfile.txt","r") as fp:
        print(fp.read())
except FileNotFoundError:
    print("No such file")
