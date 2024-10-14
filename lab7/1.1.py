import pandas as pd
import math

# Load the dataset
df = pd.read_csv("diabetes.csv")

# Shuffle the dataset and split into training and testing sets
train_df = df.sample(frac=0.8, random_state=42)  # 80% for training
test_df = df.drop(train_df.index)                # Remaining 20% for testing

# Separate features and labels for training data
train_feature = train_df.drop(columns=['Outcome'])
train_labels = train_df['Outcome']
test_feature = test_df.drop(columns=['Outcome'])
test_labels = test_df['Outcome']

# Function to calculate the centroid for a given class label
def cal_centroid(feature, labels, class_label):
    class_feature = feature[labels == class_label]
    centroid = class_feature.mean()
    return centroid

# Calculate centroids for class 0 (non-diabetic) and class 1 (diabetic)
centroid_non_diabetic = cal_centroid(train_feature, train_labels, 0)
centroid_diabetic = cal_centroid(train_feature, train_labels, 1)

# Function to calculate Euclidean distance between two points
def euclidean_distance(p1, p2):
    dist = math.sqrt(sum((p1 - p2) ** 2))
    return dist

# Function to classify a sample based on minimum distance to centroids
def classify(test_sample, centroid_non_diabetic, centroid_diabetic):
    dist_non_diabetic = euclidean_distance(test_sample, centroid_non_diabetic)
    dist_diabetic = euclidean_distance(test_sample, centroid_diabetic)
    
    if dist_non_diabetic < dist_diabetic:
        return 0
    else:
        return 1

# Predict labels for the test set
predict = []
for index, test_sample in test_feature.iterrows():
    prediction = classify(test_sample, centroid_non_diabetic, centroid_diabetic)
    predict.append(prediction)

# Convert predictions to a Pandas Series
predict_label = pd.Series(predict, index=test_feature.index)

# Calculate the accuracy
original_accuracy = (predict_label == test_labels).mean()
print(f"Original Accuracy is : {original_accuracy * 100:.2f}%")

# Display actual vs. predicted outcomes
result = pd.DataFrame({'Actual': test_labels, 'Predicted': predict_label})
print(result)

# Improved Classifier Code with Normalization and Weights
# Normalize the data using Min-Max scaling
def normalize(df):
    return (df - df.min()) / (df.max() - df.min())

# Normalize both training and testing features
train_feature_norm = normalize(train_feature)
test_feature_norm = normalize(test_feature)

# Define feature weights (adjust based on importance)
feature_weights = {
    'Pregnancies': 1.0,
    'Glucose': 2.0,
    'BloodPressure': 1.0,
    'SkinThickness': 1.0,
    'Insulin': 1.5,
    'BMI': 2.0,
    'Age': 1.0
}

# Weighted Euclidean distance calculation
def weighted_euclidean_distance(point1, point2, weights):
    distance = math.sqrt(sum(weights[col] * (point1[col] - point2[col]) ** 2 for col in point1.index))
    return distance

# Classify based on weighted minimum distance
def classify_min_distance_weighted(test_sample, centroid_non_diabetic, centroid_diabetic, weights):
    distance_to_non_diabetic = weighted_euclidean_distance(test_sample, centroid_non_diabetic, weights)
    distance_to_diabetic = weighted_euclidean_distance(test_sample, centroid_diabetic, weights)
    return 0 if distance_to_non_diabetic < distance_to_diabetic else 1

# Calculate centroids for the normalized data
centroid_non_diabetic_norm = cal_centroid(train_feature_norm, train_labels, 0)
centroid_diabetic_norm = cal_centroid(train_feature_norm, train_labels, 1)

# Predict for the normalized test set using weighted classifier
improved_predictions = []
for index, test_sample in test_feature_norm.iterrows():
    prediction = classify_min_distance_weighted(test_sample, centroid_non_diabetic_norm, centroid_diabetic_norm, feature_weights)
    improved_predictions.append(prediction)

# Convert improved predictions to a Pandas Series
improved_predict_label = pd.Series(improved_predictions, index=test_feature.index)

# Calculate the improved accuracy
improved_accuracy = (improved_predict_label == test_labels).mean()
print(f"Improved Accuracy is : {improved_accuracy * 100:.2f}%")

# Display actual vs. improved predicted outcomes
improved_result = pd.DataFrame({'Actual': test_labels, 'Improved Predicted': improved_predict_label})
print(improved_result)

# Comparison of both classifiers
comparison = pd.DataFrame({
    'Actual': test_labels,
    'Original Predicted': predict_label,
    'Improved Predicted': improved_predict_label
})
print(comparison)
