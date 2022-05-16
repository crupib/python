def toggleKthBit(n, k):
    return (n ^ (1 << (k-1)))
def is_set(x, n):
    return x & 2 ** n != 0 

    # a more bitwise- and performance-friendly version:
    return x & 1 << n != 0

is_set(10, 1)
# Driver code
def main():
   n = 0b11111111
   k = 1
   print("Original byte:     \n",bin(n))
   print("After toggle (bit1)\n", bin(toggleKthBit(n , k)))
   new_byte = toggleKthBit(n , k)
   print(is_set(new_byte,0))
if __name__ == "__main__": 
    main()
