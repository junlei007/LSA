"""
@author: JunLei_D
@contact: junlei007.love@163.com
@file: lsa.py
@time: 2020/11/30 11:06
@desc: 关于滞后序列方法的pyhton实现
"""

import numpy as np
import pandas as pd
from pprint import pprint


class LSA:
    """
    滞后序列分析，python版
    """

    def __init__(self, code_set):
        """
        :param seqs: 编码的序列
        :param code_set: 编码集合
        """
        self.seqs = None
        self.code_set = list(code_set)
        self.code_length = len(code_set)
        self.transform_array = np.zeros([self.code_length, self.code_length])
        self.Z = np.zeros([self.code_length, self.code_length])

    def _get_frequency_array(self, output=True):
        for seq in self.seqs:
            if seq:
                last_code = seq[0]
                for act in seq[1:]:
                    idx1 = self.code_set.index(last_code)
                    idx2 = self.code_set.index(act)
                    self.transform_array[idx1][idx2] += 1
                    last_code = act
        if output:
            pprint(pd.DataFrame(self.transform_array, columns=self.code_set, index=self.code_set))

    def _adjusted_residual_z(self, output):
        array = self.transform_array
        length = self.code_length
        i = array.sum(axis=1)
        j = array.sum(axis=0)
        N = array.sum()
        eij = np.dot(i.reshape(length, 1), j.reshape(1, length)) / N
        i_minus = 1 - i / N
        j_minus = 1 - j / N
        c_ij = np.sqrt(np.dot(i_minus.reshape([length, 1]), j_minus.reshape([1, length])) * eij)
        z_ij = (array - eij) / c_ij
        self.Z = z_ij.round(3)
        self.Z_frame = pd.DataFrame(self.Z, columns=self.code_set, index=self.code_set)
        if output:
            pprint(self.Z_frame)

    def fit(self, seqs, output=True):
        """
        :param seqs: 序列
        :param output: 是否print输出，默认为True，若为False，就不打印
        :return:
        """
        self.seqs = seqs
        self._get_frequency_array(output)
        self._adjusted_residual_z(output)

    def to_sds(self, seqs, file_name, user_name='Student'):
        with open(file_name, 'w+') as f:
            f.write("Event\n")
            f.write("($Behavior = {})\n".format(' '.join(self.code_set)))
            f.write("Type(Clinic Control);\n")

            for idx, i in enumerate(seqs[:-1]):
                f.write('\n')
                f.write("% {} #{}\n".format(user_name, idx + 1))
                f.write("{};\n".format(' '.join(i)))

            f.write('\n')
            f.write("% {} #{}\n".format(user_name, idx + 2))
            f.write("{}/\n".format(' '.join(seqs[-1])))


if __name__ == '__main__':
    data = [['A', 'B', 'C', 'B', 'C', 'B', 'C'],
            ['C', 'C', 'B', 'A', 'C', 'A', 'B', 'C', 'B', 'C']]

    lsa = LSA(['A', 'B', 'C'])
    lsa.fit(data)
    # lsa.to_sds(data, "2.sds")
