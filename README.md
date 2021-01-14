# LSA(lag sequential analysis)
滞后序列分析python版

## 安装

```
pip install pyseqlsa
```
或者
```
pip3 install pyseqlsa
```
## 快速使用
```
from pyseqlsa import LSA
data = [['A', 'B', 'C', 'B', 'C', 'B', 'C'],
        ['C', 'C', 'B', 'A', 'C', 'A', 'B', 'C', 'B', 'C']]

lsa = LSA(['A', 'B', 'C'])
lsa.fit(data)

```

#### 单独查看Z矩阵的方法
```
# 属性Z即是残差显著性的矩阵，大于1.96即显著
lsa.Z
```


#### 如果想转换Gseq5为sds文件，可以调用

```
lsa.to_sds(data, "filename.sds")
```


#### 通过csv获得seqs，并进行滞后序列分析

注意此处默认csv的格式，第一列为序列的id，第二列为code，标题名可以随意，从第二行开始读取，如下所示

| id   | code |
| ---- | ---- |
| 1    | a    |
| 1    | b    |
| 1    | a    |
| 2    | a    |
| 2    | b    |
| 2    | c    |

读取后的数据即可直接用于LSA代码如下所示


```
from pyseqlsa import read_seqs_from_csv
from pyseqlsa import LSA

data = read_seqs_from_csv('test.csv')
lsa = LSA(['A', 'B', 'C'])
lsa.fit(data)

```

#### 通过excel获得seqs，并进行滞后序列分析

注意此处默认csv的格式，第一列为序列的id，第二列为code，标题名可以随意，从第二行开始读取，如下所示

| id   | code |
| ---- | ---- |
| 1    | a    |
| 1    | b    |
| 1    | a    |
| 2    | a    |
| 2    | b    |
| 2    | c    |

读取后的数据即可直接用于LSA代码如下所示


```
from pyseqlsa import read_seqs_from_excel
from pyseqlsa import LSA

data = read_seqs_from_excel('test.xlsx')
lsa = LSA(['a', 'b', 'c'])
lsa.fit(data)

```