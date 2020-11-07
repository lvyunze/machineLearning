from sklearn.decomposition import PCA
import numpy as np
X = np.array([[2, 3, 4], [2, 4, 5], [4, 6, 7]])
# n_components值为2，即保留2个特征
pca = PCA(n_components=2)
pca.fit(X)
print(pca.explained_variance_ratio_)
"""
[0.98112522 0.01887478]
说明：
第一个特征保留0.98112522的信息
第二个特征保留0.01887478的信息
"""
print(pca.transform(X))
"""
pca转化后的数据情况
[[-1.98103531 -0.274771  ]
 [-0.72510925  0.37534417]
 [ 2.70614456 -0.10057317]]
"""

