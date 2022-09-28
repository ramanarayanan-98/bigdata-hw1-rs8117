#!/usr/bin/env python
"""An advanced Mapper, using Python iterators and generators."""
import sys
import re


def read_input(input, n, q):
    for line in input:
        # split the line into words; keep returning each word
        if q == 3:
            # Took HTML Parser regex from https://uibakery.io/regex-library/html-regex-python
            line = re.sub(r"<(?:\"[^\"]*\"['\"]*|'[^']*'['\"]*|[^'\">])+>", "", line)
            line = " ".join(line.split()[1:])
            line = re.sub(r"[^a-z\d]", " ", line.lower())
            splits = line.split()
            yield [",".join(comb) for comb in zip(splits, splits[1:])]
        else:
            line = re.sub(r'[^a-z\d]', ' ', line.lower())
            splits = line.split()
            if n == 1:
                yield splits
            elif n == 2:
                yield [",".join(comb) for comb in zip(splits, splits[1:])]
            else:
                yield [",".join(comb) for comb in zip(splits, splits[1:], splits[2:])]


def main(n,q):
    # input comes from STDIN (standard input)
    data = read_input(sys.stdin, n, q)

    for combinations in data:
        for comb in combinations:
            print('%s%s%d' % (comb, " ", 1))


# how to test locally in bash/linus: cat <input> | python mapper.py
if __name__ == "__main__":
    # print("Execute with command line argument as input to ngram_count in the range [1, 2, 3]\n")
    ngram_count = 1
    question_num = 2
    if len(sys.argv) > 2:
        question_num = int(sys.argv[2])
    if len(sys.argv) > 1:
        ngram_count = int(sys.argv[1])

    if ngram_count in [1, 2, 3] and question_num in [2, 3]:
        main(ngram_count, question_num)
    else:
        raise Exception("Invalid input. Enter ngram_count in range [1, 2, 3] and question_num in range [2, 3]")