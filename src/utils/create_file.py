def create_file(path, data=""):
    with open(path, "w") as file:
        file.write(data)
