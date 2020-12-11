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

单独查看Z矩阵的方法
```
# 属性Z即是残差显著性的矩阵，大于1.96即显著
lsa.Z
```

如果想转换Gseq5为sds文件，可以调用

```
lsa.to_sds(data, "filename.sds")
```
