from sklearn.metrics import *  # pip install scikit-learn
import matplotlib.pyplot as plt # pip install matplotlib
import pandas as pd # pip install pandas
import os

'''
读取数据

需要读取模型输出的标签（predict_label）以及原本的标签（true_label）

'''
target_loc = "./test.txt"     # 真实标签所在的文件
target_data = pd.read_csv(target_loc, sep="\t", names=["loc","type"])
true_label = [i for i in target_data["type"]]


predict_loc = "./pred_result.csv"     # 3.ModelEvaluate.py生成的文件

predict_data = pd.read_csv(predict_loc,encoding="GBK")#,index_col=0)

predict_label = predict_data.to_numpy().argmax(axis=1)

predict_score = predict_data.to_numpy().max(axis=1)

'''
    常用指标：精度，查准率，召回率，F1-Score
'''
# 精度，准确率， 预测正确的占所有样本种的比例
accuracy = accuracy_score(true_label, predict_label)
print("精度: ",accuracy)

# 查准率P（准确率），precision(查准率)=TP/(TP+FP)

precision = precision_score(true_label, predict_label, labels=None, pos_label=1, average='macro') # 'micro', 'macro', 'weighted'
print("查准率P: ",precision)

# 查全率R（召回率），原本为对的，预测正确的比例；recall(查全率)=TP/(TP+FN)
recall = recall_score(true_label, predict_label, average='macro') # 'micro', 'macro', 'weighted'
print("召回率: ",recall)

# F1-Score
f1 = f1_score(true_label, predict_label, average='macro')     # 'micro', 'macro', 'weighted'
print("F1 Score: ",f1)


'''
混淆矩阵
'''
label_names = []
data_root = r"./enhance_dataset"
for a,b,c in os.walk(data_root):
    if len(b) != 0:
        print(b)
        label_names = b

confusion = confusion_matrix(true_label, predict_label, labels=[i for i in range(len(label_names))])


plt.matshow(confusion, cmap=plt.cm.Oranges)   # Greens, Blues, Oranges, Reds

plt.rcParams["font.sans-serif"] = ["SimHei"]  # 设置中文字体
plt.rcParams["font.size"] = 8
plt.rcParams["axes.unicode_minus"] = False  # 该语句解决图像中的“-”负号的乱码问题

plt.colorbar()
for i in range(len(confusion)):
    for j in range(len(confusion)):
        plt.annotate(confusion[j,i], xy=(i, j), horizontalalignment='center', verticalalignment='center')
plt.ylabel('True label')
plt.xlabel('Predicted label')


plt.xticks(range(len(label_names)), label_names,rotation=270)
plt.yticks(range(len(label_names)), label_names)
plt.title("Confusion Matrix")
plt.show()


