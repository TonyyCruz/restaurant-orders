def create_a_txt_file(path, data=""):
    if not path.endswith(".txt"):
        raise TypeError("Invalid file type")
    with open(path, "w") as file:
        file.write(data)
