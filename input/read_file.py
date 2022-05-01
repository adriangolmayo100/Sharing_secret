def first_line(file):
    with open(file) as f:
        line = f.readline()
        if not line.isdigit():
            raise IOError(f"Error, the file '{file}' does not contain a number.")
        secret = int(line)
        return secret
