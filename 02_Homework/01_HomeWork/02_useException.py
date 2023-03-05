try:
    with open("test.txt", "r", encoding="UTF-8") as f:
        print(f.read())
except Exception as e:
    print(e)
