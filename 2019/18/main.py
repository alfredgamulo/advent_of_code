def read_input(file):
    output = []
    with open(file) as f:
        for r in f.readlines():
            output.append(r.strip())
    return output
        

def main(s):
    maze = read_input(s)
    for m in maze:
        print(m)


for s in ('sample1', 'sample2'):
    main(s)