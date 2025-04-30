""" Huffman Encoding"""
import os

class Node:
    """ class for node and its use in this program, 'used to build the tree' """
    def __init__(self, prob, symbol, left=None, right=None):
        # probability of symbol
        self.prob = prob
        # symbol
        self.symbol = symbol
        # left node
        self.left = left
        # right node
        self.right = right
        # tree direction (0/1)
        self.code = ''
    def __str__(self):
        """ to prevent pylint errors (2 or more methods needed for a class """
        return self.__class__.__name__
    @staticmethod
    def create():
        """ to prevent pylint errors (2 or more methods needed for a class """
        return object()

# globals
codes = {}
def to_bytes(data):
    """ convert string to bytes for saving to file """
    _b = bytearray()
    for i in range(0, len(data), 8):
        _b.append(int(data[i:i+8], 2))
    return bytes(_b)

def calculate_codes(node, val=''):
    """ add node to codes tree """
    # huffman code for current node
    new_val = val + str(node.code)

    if node.left:
        calculate_codes(node.left, new_val)
    if node.right:
        calculate_codes(node.right, new_val)
    if(not node.left and not node.right):
        codes[node.symbol] = new_val
    return codes

def calculate_probability(data):
    """ A helper function to calculate the probabilities of symbols in given data"""
    symbols = {}
    for element in data:
        if symbols.get(element) is None:
            symbols[element] = 1
        else:
            symbols[element] += 1
    return symbols

def output_encoded(data, coding):
    """ A helper function to output encoded data """
    encoding_output = []
    for _c in data:
        encoding_output.append(coding[_c])
    string = ''.join([str(item) for item in encoding_output])
    return string

def total_gain(data, coding):
    """ show compression/ration before and after compression """
    before_compression = len(data) * 8 # total bit space to store the data before compression
    after_compression = 0
    symbols = coding.keys()
    for symbol in symbols:
        count = data.count(symbol)
        after_compression += count * len(coding[symbol])
        #calculate how many bit is required for that symbol in total
    #print("Space usage before compression (in bits):", before_compression)
    #print("Space usage after compression (in bits):",  after_compression)

def huffman_encoding(data):
    """ huffman encoding routine """
    symbol_with_probs = calculate_probability(data)
    symbols = symbol_with_probs.keys()
    probabilities = symbol_with_probs.values()
    #print("symbols: ", symbols)
    #print("probabilities: ", probabilities)
    nodes = []
    # converting symbols and probabilities into huffman tree nodes
    for symbol in symbols:
        nodes.append(Node(symbol_with_probs.get(symbol), symbol))
    while len(nodes) > 1:
        # sort all the nodes in ascending order based on their probability
        nodes = sorted(nodes, key=lambda x: x.prob)
        # pick 2 smallest nodes
        right = nodes[0]
        left = nodes[1]
        left.code = 0
        right.code = 1
        # combine the 2 smallest nodes to create new node
        new_node = Node(left.prob+right.prob, left.symbol+right.symbol, left, right)
        nodes.remove(left)
        nodes.remove(right)
        nodes.append(new_node)
    huffman_encoding_v = calculate_codes(nodes[0])
   # print("symbols with codes", huffman_encoding_v)
    total_gain(data, huffman_encoding_v)
    encoded_output = output_encoded(data,huffman_encoding_v)
    return encoded_output, nodes[0]

def huffman_decoding(encoded_data, huffman_tree):
    """ huffman decoding algorithm - reverse of encoding """
    tree_head = huffman_tree
    decoded_output = []
    for _x in encoded_data:
        if _x == '1':
            huffman_tree = huffman_tree.right
        elif _x == '0':
            huffman_tree = huffman_tree.left
        try:
            if huffman_tree.left.symbol is None and huffman_tree.right.symbol is None:
                pass
        except AttributeError:
            decoded_output.append(huffman_tree.symbol)
            huffman_tree = tree_head
    string = ''.join([str(item) for item in decoded_output])
    return string

def encode_file():
    ''' encode a file read from the os '''
    with open("demofile.txt", "r",encoding="ascii") as _f:
        _data_ = _f.read()  
    _f.close()
    encoding, tree = huffman_encoding(_data_)
    with open('test_encoded.txt','w') as ofile:
        ofile.write(encoding)
    ofile.close()
    with open('test_encoded.txt','rb') as efile:
         _data_encoded = efile.read()
    print(_data_encoded)
    efile.close()

def decode_file():
    ''' decode a file read from the os '''
    # Determine encoding and tree data
    with open("demofile.txt", "r",encoding="ascii") as _f:
        _data_ = _f.read()
    _f.close()
    _, tree = huffman_encoding(_data_)
    with open('test.bin','rb') as bfile:
        _bindata_ = bfile.read()
    mystring = ""
    for _i in _bindata_:
        mystring = mystring+str(bin(_i)[2:].zfill(8))
    out_file = huffman_decoding(mystring,tree)
    with open('test_decoded.txt', 'w',encoding='ascii') as tfile:
        tfile.write(out_file)
    bfile.close()
    tfile.close()

def compression_stats():
    ''' print compression statistics '''
    #print("Compression statistics")
    _o = os.path.getsize('demofile.txt')
    _c = os.path.getsize('test.bin')
    #print(f'Original file: {_o} bytes')
    #print(f'Compressed file: {_c} bytes')
    comp_ratio = round((((_o-_c)/_o)*100), 0)
    #print(f'Compressed file to about {comp_ratio}% of original')

def perform_memory():
    ''' perform in memory small size '''
    _data_ = "AAAAAAABCCCCCCDDEEEEE"
    encoding, tree = huffman_encoding(_data_)
    print("Encoded output", encoding)
    print("Decoded Output", huffman_decoding(encoding,tree))

def main():
    """ main routine """
#    print("Memory Test\n")
#    perform_memory()
#    print("File Encode Test\n")
    encode_file()
#    print("Compression Stats\n")
#    compression_stats()
#    print("File Decode Test\n")
    decode_file()
if __name__ == "__main__":
    main()
