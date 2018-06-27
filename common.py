
def print_header(index):
    n = 20
    msg = "example %d" % index

    print '\n'
    print "*" * n
    print get_middle_line(n, msg)
    print "*" * n


def get_middle_line(n, msg):
    result = "*" * ((n - len(msg)) / 2 - 1) + ' ' + msg + ' ' + "*" * ((n - len(msg)) / 2 - 1)
    if n > (n - len(msg)) / 2 * 2 + len(msg):
        return result + "*"
    else:
        return result
