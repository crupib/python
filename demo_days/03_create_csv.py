#!/usr/bin/python3
from argparse import ArgumentParser
from pathlib import Path
import pandas as pd
import csv

def separator_change(in_file, out_files, separator, overwrite=False, check_for_collision=False):
    # check if file already exists
    if not overwrite:
        for file in out_files:
            if Path(file).exists():
                raise ValueError("overwrite was not specified and out-file already exists.")

    # find the current separator
    with open(in_file, "r") as f:
        sniffer = csv.Sniffer()
        sep = sniffer.sniff(f.readline()).delimiter
        # reset to top of file
        f.seek(0)
        if check_for_collision and separator in f.read():
            raise Exception("The separator was found inside the CSV.")
        
    # read in-file
    df = pd.read_csv(in_file, sep=sep)
    # write to out-files
    for file in out_files:
        df.to_csv(file, sep=separator, index=False)

if __name__ == "__main__":
    parser = ArgumentParser(
        # name of program
        prog="CSV separator changer",
        # description
        description="Takes a csv and a separator, loads the csv, changes the separator and then saves the csv to specified files.",
        # bottom text
        epilog="By William Crupi"
    )
    
    # add arguments
    
    # all mandatory arguments are added as positional
    parser.add_argument(
        "in_file", 
        help="The input file to change the separator in"
    )
    # need at least one output file, thus nargs="+" is used
    parser.add_argument(
        "out_files", 
        nargs="+",
        help="The output file(s) to write to"
    )
    # the separator is optional, otherwise "," is used by default
    parser.add_argument(
        "-s", "--separator", 
        default=",", 
        dest="separator",
        help="The separator to change to"
    )
    # two flags, False by default
    parser.add_argument(
        "-c", "--collision_check", 
        action="store_true", 
        dest="check_for_collision",
        help="Whether to check and exit if the separator was detected in the file"
    )
    parser.add_argument(
        "-o", 
        "--overwrite", 
        action="store_true",
        dest="overwrite",
        help="Whether to overwrite the output file(s) if they already exist"
    )

    args = parser.parse_args()

    separator_change(**vars(args))
