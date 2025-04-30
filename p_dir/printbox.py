def print_in_a_frame(words, borderchar = '*'):
    size = max(len(word) for word in words)
    print(borderchar * (size + 4))
    for word in words:
        print('{bc} {:<{}} {bc}'.format(word, size, bc = borderchar))
    print(borderchar * (size + 4))
def main():
   print_in_a_frame("Box this message because my balls hurt".split())
   print_in_a_frame("Box this message".split(), '+')
   print_in_a_frame("Box this message".split(), '-')
if __name__ == '__main__':
   main()
