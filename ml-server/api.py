from flask import Flask, request, jsonify
import lstm
import yolo
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/predict')
def home():
    query = request.args.get('text')
    result = lstm.predict(query)
    data = {"prediction":str(result)}
    print(data)
    return jsonify(data), 200, {'Custom-Header': 'Custom-Value'}

# @app.route('/predict-image', methods=['POST'])
# def upload_image():
#     print(request.form['image'])
#     if 'image' not in request.files:
#         return jsonify({'error': 'No file part'}), 400
#     image_base64 = request.files['image']
#     try:
#         image_data = base64.b64decode(image_base64)
#         image = Image.open(BytesIO(image_data))
#         predictions = yolo.predict("input.jpg")
#         result = {
#             'predictions': predictions
#         }
#         return jsonify({"message": "Image uploaded successfully!"}), 200
#     except Exception as e:
#         return jsonify({"error": f"Failed to process image: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5001)
