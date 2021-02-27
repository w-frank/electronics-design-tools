"""Binary Test Vector Generator

This script generates text files containing binary test vector data for use as
input stimulus to digital circuit simulation and verification testbenches. For
example, the resultant text file can be loaded into VHDL using the TEXTIO
package.

The script can be run from the command line with the following optional flags:
    -n  : bit width of test vectors (default = 4)
    -df : number of times to duplicate and concatenate vector (default = 1)
    -t  : sequence type ("count", "random", "gray", default = "count")
    -f  : file name (default = "test_vectors.txt")

    usage: python test_vector_generator.py [-h] [-n N] [-df DF] [-t T] [-f F]

"""

import os
import sys
import random
import argparse


def gray_code_gen(N):
    """Generates the sequence of binary gray codes of width N

    Parameters
    ----------
    N : integer
        Width of the binary gray codes

    Returns
    -------
    data : list
        The list of generated binary gray codes of width N
    """
    data = []
    for i in range(0, 1 << N):
        gray = i ^ (i >> 1)
        data.append(gray)
    return data


def main():
    # Parse the command line arguments
    parser = argparse.ArgumentParser(description='Binary test vector generator')
    parser.add_argument("-n", default=4, type=int, help="Bit width of test "
                        "vectors")
    parser.add_argument("-df", default=1, type=int, help="Duplication factor")
    parser.add_argument("-t", default="count", type=str, help="Sequence type of"
                        "test vectors")
    parser.add_argument("-f", default="test_vectors.txt", type=str,
                        help="Filename of generated text file")

    args = parser.parse_args()

    seq_type = args.t
    bit_width = args.n
    duplication_factor = args.df
    file_name = args.f

    num_samples = 2**bit_width

    # Generate list of test vectors depending on required type
    if (seq_type == "count"):
        vectors = range(num_samples)
    elif (seq_type == "random"):
        vectors = [random.randint(0, num_samples-1) for value in
                   range(num_samples)]
    elif (seq_type == "gray"):
        vectors = gray_code_gen(bit_width)
    else:
        vectors = []

    # Write test vectors to specified text file
    with open(os.path.join(sys.path[0], file_name), 'w') as f:
        for vector in vectors:
            for duplicate in range(duplication_factor):
                f.write('{0:0{1}b}'.format(vector, bit_width))
            f.write('\n')

        f.close()


if __name__ == "__main__":
    main()
