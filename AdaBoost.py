from sklearn.ensemble import AdaBoostClassifier as AdaBoost
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn import metrics
import pandas as pd
import time

# 读取数据
f = pd.read_csv("./data/iris.csv")
x = f.iloc[:, 0:4]
y = f.iloc[:, 4]

# 归一化（使用极差法）
scaler = MinMaxScaler()
x = scaler.fit_transform(x)

# 随机分类训练集与测试集
trainX, testX, trainY, testY = train_test_split(
    x, y, test_size=0.2, random_state=1)

# AdaBoost模型
start = time.perf_counter()
modle = AdaBoost(n_estimators=50, learning_rate=0.2, random_state=1)
modle.fit(trainX, trainY)
end = time.perf_counter()
print('Running time: %s ms' % ((end-start) * 1000))

# 输出评估结果
expected = testY
predict = modle.predict(testX)
print(metrics.classification_report(expected, predict))

# 建立混淆矩阵
lable = list(set(expected))
matrix = pd.DataFrame(metrics.confusion_matrix(
    expected, predict, labels=lable), index=lable, columns=lable)
print(matrix)