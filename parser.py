def check(s, left, right):
    b = 0
    for c in s:
        if c == left:
            b += 1
        if c == right:
            if b == 0:
                return False
            b -= 1
    return b == 0

def is_paired(input_string: str):
    parens=check(input_string, left='(',right=')')
    brackets=check(input_string, left='[',right=']')
    braces=check(input_string, left='{',right='}')
    return parens, brackets, braces

def main():
    """ Put all your testing code here"""
    codestr="if x==y then  { run program }().execute[0]"
    parens, brackets, braces = is_paired(codestr)
    if parens and brackets and braces:
       print("Code passes check")
    else:
      print("Code failed check")

if __name__ == '__main__':
    main()

