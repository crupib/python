#!/usr/local/bin/python3
import base64, sys

base64.decode(open(sys.argv[1], "rb"), open(sys.argv[2], "wb"))
