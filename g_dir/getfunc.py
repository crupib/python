import algorithms
import sys

def top_level_functions(body):
    return (f for f in body if isinstance(f, ast.FunctionDef))

def parse_alg(filename):
    with open(filename, "rt") as file:
        return algorithms.parse(file.read(), filename=filename)

if __name__ == "__main__":
    for filename in sys.argv[1:]:
        print(filename)
        tree = parse_alg(filename)
        for func in top_level_functions(tree.body):
            print("  %s" % func.name)

