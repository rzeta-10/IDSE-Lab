# CS22B1093 ROHAN G

import pandas as pd
import math
import matplotlib.pyplot as plt

df = pd.read_csv("diabetes.csv")

# print(df.head())
# print(list(df.columns))
# print(df.info())

# split = int(0.8*(df.shape[0]))

# train_df = df.iloc[:split]
# print(train_df)
# print(train_df.describe())
# train_df = train_df.drop(columns=['Outcome'])
# test_df = df.iloc[split:]
# print(train_df.describe())
# print(test_df)

train_df = df.sample(frac=0.8,random_state=42)
test_df = df.drop(train_df.index)

train_feature = train_df.drop(columns=['Outcome'])
train_labels = train_df['Outcome']

test_feature = test_df.drop(columns=['Outcome'])
test_labels = test_df['Outcome']

def normalize(df):
    return ((df - df.min())/(df.max()-df.min()))

train_feature = normalize(train_feature)
test_feature = normalize(test_feature)

def cal_centroid(feature, labels, class_label):
    class_feature = feature[labels == class_label]
    centroid = class_feature.mean()
    return centroid
    
centroid_non_diabetic = cal_centroid(train_feature, train_labels, 0)
centroid_diabetic = cal_centroid(train_feature, train_labels, 1)

def euclidean_distance(p1,p2):
    dist = math.sqrt(sum((p1-p2)**2))
    return dist
    
def classify(test_sample, centroid_non_diabetic, centroid_diabetic):
    dist_non_diabetic = euclidean_distance(test_sample, centroid_non_diabetic)
    dist_diabetic = euclidean_distance(test_sample, centroid_diabetic)
    
    if dist_non_diabetic < dist_diabetic :
        return 0
    else:
        return 1
        
predict = []

for index, test_sample in test_feature.iterrows():
    prediction = classify(test_sample, centroid_non_diabetic, centroid_diabetic)
    predict.append(prediction)
    
predict_label = pd.Series(predict, index=test_feature.index)

accuracy = (predict_label == test_labels).mean()
print(f"Accuracy is : {accuracy * 100: .2f}%")

# Normalized data accuracy - 70% , without normalized data accuracy - 66%

result = pd.DataFrame({'Actual': test_labels, 'Predicted': predict_label})
print(result)

print("Normalized data accuracy - 70% , without normalized data accuracy - 66%")