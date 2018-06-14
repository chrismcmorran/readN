def read_first_n(file, n):
    try:
        fd = open(file, 'r')
        lines = fd.readlines()[0:n]
        return lines
    except:
        raise FileNotFoundError


def read_last_n(file, n):
    try:
        fd = open(file, 'r')
        lines = fd.readlines()
        return lines[len(lines) - n:]
    except:
        raise FileNotFoundError
