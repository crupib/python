import argparse
parser = argparse.ArgumentParser(prog='fuckme.py')
parser.add_argument('--foo', help='foo help %(prog)s program')
args = parser.parse_args()
