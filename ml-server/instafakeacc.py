import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import tensorflow as tf
from tensorflow.keras.layers import Dense, Activation, Dropout
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.metrics import Accuracy
from sklearn import metrics
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report, accuracy_score, roc_curve, confusion_matrix

# Load the training and testing data
instagram_df_train = pd.read_csv('insta_train.csv')
instagram_df_test = pd.read_csv('insta_test.csv')

# # Display the first few rows of each dataframe
# print(instagram_df_train.head())
# print(instagram_df_test.head())

# Performing Exploratory Data Analysis (EDA)

# # Getting dataframe info
# print(instagram_df_train.info())

# # Get the statistical summary of the dataframe
# print(instagram_df_train.describe())

# # Checking if null values exist
# print(instagram_df_train.isnull().sum())

# # Get the number of unique values in the "profile pic" feature
# print(instagram_df_train['profile pic'].value_counts())

# # Get the number of unique values in "fake" (Target column)
# print(instagram_df_train['fake'].value_counts())

# print(instagram_df_test.info())
# print(instagram_df_test.describe())
# print(instagram_df_test.isnull().sum())
# print(instagram_df_test['fake'].value_counts())

# Perform Data Visualizations

# # Visualize the data
# sns.countplot(instagram_df_train['fake'])
# plt.show()

# # Visualize the private column data
# sns.countplot(instagram_df_train['private'])
# plt.show()

# # Visualize the "profile pic" column data
# sns.countplot(instagram_df_train['profile pic'])
# plt.show()

# # Visualize the data distribution
# plt.figure(figsize=(20, 10))
# sns.histplot(instagram_df_train['nums/length username'], kde=True)
# plt.show()

# # Correlation plot
# plt.figure(figsize=(20, 20))
# cm = instagram_df_train.corr()
# ax = plt.subplot()
# # heatmap for correlation matrix
# sns.heatmap(cm, annot=True, ax=ax)
# plt.show()

# sns.countplot(instagram_df_test['fake'])
# sns.countplot(instagram_df_test['private'])
# sns.countplot(instagram_df_test['profile pic'])

# Preparing Data to Train the Model

# Training and testing dataset (inputs)
X_train = instagram_df_train.drop(columns=['fake'])
X_test = instagram_df_test.drop(columns=['fake'])

# Training and testing dataset (Outputs)
y_train = instagram_df_train['fake']
y_test = instagram_df_test['fake']

# Scale the data before training the model
from sklearn.preprocessing import StandardScaler

scaler_x = StandardScaler()
X_train = scaler_x.fit_transform(X_train)
X_test = scaler_x.transform(X_test)

y_train = tf.keras.utils.to_categorical(y_train, num_classes=2)
y_test = tf.keras.utils.to_categorical(y_test, num_classes=2)

# # print the shapes of training and testing datasets
# print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)

Training_data = len(X_train) / (len(X_test) + len(X_train)) * 100
Testing_data = len(X_test) / (len(X_test) + len(X_train)) * 100

# print(f"Training Data: {Training_data}%")
# print(f"Testing Data: {Testing_data}%")

# Building and Training Deep Learning Model

model = tf.keras.models.Sequential()
model.add(Dense(50, input_dim=X_train.shape[1], activation='relu'))
model.add(Dense(150, activation='relu'))
model.add(Dropout(0.3))
model.add(Dense(150, activation='relu'))
model.add(Dropout(0.3))
model.add(Dense(25, activation='relu'))
model.add(Dropout(0.3))
model.add(Dense(2, activation='softmax'))

model.summary()

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

epochs_hist = model.fit(X_train, y_train, epochs=50, verbose=1, validation_split=0.1)

# Access the Performance of the model

# print(epochs_hist.history.keys())

# plt.plot(epochs_hist.history['loss'])
# plt.plot(epochs_hist.history['val_loss'])
# plt.title('Model Loss Progression During Training/Validation')
# plt.ylabel('Training and Validation Losses')
# plt.xlabel('Epoch Number')
# plt.legend(['Training Loss', 'Validation Loss'])
# plt.show()

# predicted = model.predict(X_test)

# predicted_value = []
# test = []
# for i in predicted:
#     predicted_value.append(np.argmax(i))

# for i in y_test:
#     test.append(np.argmax(i))

# print(classification_report(test, predicted_value))

# plt.figure(figsize=(10, 10))
# cm = confusion_matrix(test, predicted_value)
# sns.heatmap(cm, annot=True)
# plt.show()
