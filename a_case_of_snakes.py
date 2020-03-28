sample = [
("szWindowContents", "window_contents"),
("iAirflowParameter", "airflow_parameter"),
("fMixtureRatio", "mixture_ratio"),
("mix2Drag", "mix2_drag"),
]


def main():
    import sys
    for line in sys.stdin.readlines():
        solution = solver(line.strip('\n'))
        print(solution)


def test(sample_list):
    for samp, result in sample_list:
        solution = solver(samp)


        print(f'{solution} == {result}: {solution==result}')


def solver(hungarian):
    import re
    p = re.compile('([A-Z][a-z,1-9]+)')
    words = p.findall(hungarian)
    if len(words)<2: # hacky
        words = re.findall('([a-z,1-9]+)([A-Z][a-z]+)',hungarian)[0]

    return '_'.join([w.lower() for w in words])

    
if __name__ == "__main__":
    main()
    # test(sample)

