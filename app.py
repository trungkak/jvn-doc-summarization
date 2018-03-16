# -*- coding: utf-8 -*-

import sys
from summarizer import TextSummarizer
import os

if __name__ == '__main__':
    i_path = sys.argv[1]
    o_path = sys.argv[2]

    if not os.path.exists(i_path):
        print('Wrong file path!!!')
        exit(1)

    i_path = os.path.abspath(i_path)
    o_path = os.path.abspath(o_path)

    summarizer = TextSummarizer(i_path)

    abstract = summarizer.summarize()

    with open(o_path, 'w') as f:
        f.write(abstract)

    print('Successfully create abstract, abstract file is at: ' + o_path)
    exit(0)



