# LSA
滞后序列分析python版

```
data = [['A', 'B', 'C', 'B', 'C', 'B', 'C'],
        ['C', 'C', 'B', 'A', 'C', 'A', 'B', 'C', 'B', 'C']]

lsa = LSA(['A', 'B', 'C'])
lsa.fit(data)

```

```
# 属性Z即是残差显著性的矩阵，大于1.96即显著
lsa.Z
```
