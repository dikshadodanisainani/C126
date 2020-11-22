from flask import Flask, jsonify, request
from classifier import  get_prediction
#import cv2
app = Flask(__name__)

@app.route("/predict-digit", methods=["POST"])
def predict_data():
  print("Inside predict_data")
  #image = cv2.imdecode(np.fromstring(request.files.get("digit").read(), np.uint8), cv2.IMREAD_UNCHANGED)
  image = request.files.get("digit")
  print("Image name ", image )
  prediction = get_prediction(image)
  print("Prediction is ", prediction)
  return jsonify({
    "prediction": prediction
  }), 200

if __name__ == "__main__":
  app.run(debug=True)
