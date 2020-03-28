

sample = [
("110 0x187 300 T / d", 1032),
("180 A 0x10e 0x18c N 95", 1084),
("423 0xac 417 0o20 q &", 1179),
("0x14e 0b10000 247 284 0o447 268", 1444),
]


def main():
    import sys
    for line in sys.stdin.readlines():
        solution = solver(line.strip('\n'))
        print(solution)


def test(sample_list):
    for sample, result in sample_list:
        solution = solver(sample)

        print(solution)
        print(result)
        print('')


def smart_int(s):
    try:
        return int(s,0)
    except ValueError:
        return ord(s)
    


def solver(l):
    elements = l.split(' ')

    int_elements = [smart_int(el) for el in elements]

    return sum(int_elements)

    
    
    
    
if __name__ == "__main__":
    # main()
    test(sample)

