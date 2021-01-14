"""
@author: JunLei_D
@contact: junlei007.love@163.com
@file: preprosessing.py
@time: 2021/1/14 17:32
@desc:
"""
import pandas as pd
from collections import defaultdict


def frame2seqs(frame):
    data = defaultdict(list)
    for i in frame.values:
        data[i[0]].append(i[1])

    data = [i for i in data.values()]
    return data


def read_seqs_from_csv(file_name):
    data = pd.read_csv(file_name)
    return frame2seqs(data)


def read_seqs_from_excel(file_name):
    data = pd.read_excel(file_name)
    return frame2seqs(data)


if __name__ == '__main__':
    pass

