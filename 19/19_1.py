inp = """Al => ThF
Al => ThRnFAr
B => BCa
B => TiB
B => TiRnFAr
Ca => CaCa
Ca => PB
Ca => PRnFAr
Ca => SiRnFYFAr
Ca => SiRnMgAr
Ca => SiTh
F => CaF
F => PMg
F => SiAl
H => CRnAlAr
H => CRnFYFYFAr
H => CRnFYMgAr
H => CRnMgYFAr
H => HCa
H => NRnFYFAr
H => NRnMgAr
H => NTh
H => OB
H => ORnFAr
Mg => BF
Mg => TiMg
N => CRnFAr
N => HSi
O => CRnFYFAr
O => CRnMgAr
O => HP
O => NRnFAr
O => OTi
P => CaP
P => PTi
P => SiRnFAr
Si => CaSi
Th => ThCa
Ti => BP
Ti => TiTi
e => HF
e => NAl
e => OMg

CRnCaCaCaSiRnBPTiMgArSiRnSiRnMgArSiRnCaFArTiTiBSiThFYCaFArCaCaSiThCaPBSiThSiThCaCaPTiRnPBSiThRnFArArCaCaSiThCaSiThSiRnMgArCaPTiBPRnFArSiThCaSiRnFArBCaSiRnCaPRnFArPMgYCaFArCaPTiTiTiBPBSiThCaPTiBPBSiRnFArBPBSiRnCaFArBPRnSiRnFArRnSiRnBFArCaFArCaCaCaSiThSiThCaCaPBPTiTiRnFArCaPTiBSiAlArPBCaCaCaCaCaSiRnMgArCaSiThFArThCaSiThCaSiRnCaFYCaSiRnFYFArFArCaSiRnFYFArCaSiRnBPMgArSiThPRnFArCaSiRnFArTiRnSiRnFYFArCaSiRnBFArCaSiRnTiMgArSiThCaSiThCaFArPRnFArSiRnFArTiTiTiTiBCaCaSiRnCaCaFYFArSiThCaPTiBPTiBCaSiThSiRnMgArCaF"""


class Node:
    def __init__(self, replace, new):
        self.replace = replace
        self.new = new
        self.parent = None
        self.children = []
        self.live = True

    def add_child(self, child):
        self.children.append(child)
        child.parent = self
        return child

    def is_root(self):
        return self.parent is None

    def is_leaf(self):
        return len(self.children) == 0

    def result_str(self):
        result = "" if self.is_root() else self.parent.result_str()
        return result[:self.replace[0]] + self.new + result[self.replace[1]:]

    def root(self):
        if self.is_root():
            return self
        return self.parent.root()

    def nodes(self):
        nodes = []
        if self.live:
            nodes.append(self)
        for child in self.children:
            for node in child.nodes():
                if node.live:
                    nodes.append(node)
        return nodes

    def leafs(self):
        for node in self.nodes():
            if node.is_leaf():
                yield node


def swap(molecule, sub):
    molecules = set()
    if sub[0] in molecule:
        i = molecule.find(sub[0])
        while i >= 0:
            molecules.add(molecule[:i] + sub[1] + molecule[i+len(sub[0]):])
            i = molecule.find(sub[0], i+1)
    return molecules


def grow(build, sub, target):
    outcome = 0
    molecule = build.result_str()
    if sub[0] in molecule:
        i = molecule.find(sub[0])
        while i >= 0:
            result = molecule[:i] + sub[1] + molecule[i+len(sub[0]):]
            if target == result:
                return True, outcome
            duplicate = any(map(lambda node: node.result_str() == result, build.root().nodes()))
            # if not (duplicate or len(target) < len(result)):
            if not duplicate:
                new = Node((i, i+len(sub[0])), sub[1])
                build.add_child(new)
                outcome += 1
            i = molecule.find(sub[0], i + 1)
    return False, outcome


def process_input():
    with open("input.txt") as file:
        data = file.read().splitlines()
    # data = inp.splitlines()

    molecule = data[-1]
    # molecule = "HOH"
    # subs = [('e', 'H'),
    #         ('e', 'O'),
    #         ('H', 'HO'),
    #         ('H', 'OH'),
    #         ('O', 'HH')]
    subs = [tuple(line.split(' => ')) for line in data[:-2]]

    return subs, molecule


def evalp1(data):
    subs, molecule = data
    molecules = set()

    for sub in subs:
        molecules.update(swap(molecule, sub))

    return len(molecules)


def evalp2(data):
    subs, molecule = data

    subs = [tuple(reversed(sub)) for sub in subs]
    target = 'e'
    root = Node((0, 0), molecule)
    # root = Node((0, 0), 'e')

    steps = 0
    while True:
        steps += 1
        print("\nstep", steps)
        builds = list(root.leafs())
        if len(builds) == 0:
            raise Exception("something wrong")
        print(len(builds), "children", end='')
        for i, build in enumerate(builds):
            print("\nchild", i+1)
            if i == len(builds) // 2:
                print(build.result_str())
            for sub in subs:
                done, outcome = grow(build, sub, target)
                if done:
                    return steps
                print(outcome, '|', sep='', end='')
            if len(build.children) == 0:
                build.live = False
                print("\ndead")


def main():
    data = process_input()
    part1 = evalp1(data)
    print("Part 1:")
    print(part1)
    print("Part 2:")
    print(evalp2(data))


if __name__ == "__main__":
    main()
