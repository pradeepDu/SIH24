import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from tensorflow.keras.preprocessing.text import Tokenizer, tokenizer_from_json
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Embedding, LSTM, Dense, SpatialDropout1D
import json

# Load the CSV file
df = pd.read_csv('dt_phrases_4.csv')

# Text Preprocessing
max_words = 5000
max_len = 100
tokenizer = Tokenizer(num_words=max_words, lower=True)
tokenizer.fit_on_texts(df['Data'].values)
X = tokenizer.texts_to_sequences(df['Data'].values)
X = pad_sequences(X, maxlen=max_len)
tokenizer_json = tokenizer.to_json()
# Save the tokenizer JSON to a file
with open('tokenizer.json', 'w') as json_file:
    json_file.write(tokenizer_json)

# Labels
y = df['Labels']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = Sequential()
model.add(Embedding(max_words, 128, input_length=max_len))
model.add(SpatialDropout1D(0.2))
model.add(LSTM(100, dropout=0.2, recurrent_dropout=0.2))
model.add(Dense(2, activation='softmax'))
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(X_train, y_train, epochs=5, batch_size=64, validation_data=(X_test, y_test), verbose=2)
y_pred = model.predict(X_test)
y_pred_labels = y_pred.argmax(axis=1)
print(classification_report(y_test, y_pred_labels))
new_text = ['Is anyone else talking about the dangers of amphetamines?']
new_text_seq = tokenizer.texts_to_sequences(new_text)
new_text_pad = pad_sequences(new_text_seq, maxlen=max_len)
prediction = model.predict(new_text_pad)
print(f"Prediction: {'Drug-related' if prediction.argmax() == 1 else 'Non-drug-related'}")

model.save('lstm.h5')

# def predict(new_text):
#     with open('tokenizer.json', 'r') as json_file:
#         json_string = json_file.read()
#         tokenizer = tokenizer_from_json(json_string)
#     max_len = 100
#     model = load_model('lstm.h5')
#     print(new_text)
#     new_text_seq = tokenizer.texts_to_sequences([new_text])
#     new_text_pad = pad_sequences(new_text_seq, maxlen=max_len)
#     prediction = model.predict(new_text_pad)
#     # print(f"Prediction: {'Drug-related' if prediction.argmax() == 1 else 'Non-drug-related'}")
#     return prediction.argmax()

print(predict('I want that ice cream'))
