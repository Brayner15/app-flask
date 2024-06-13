from flask import Flask, request, render_template
import joblib

app = Flask(__name__)

# Cargar el modelo de sentimiento
try:
    model = joblib.load('/code/app/sentiment_model.pkl')
    print("Model loaded successfully.")
except Exception as e:
    print("Error loading the model:")
    print(e)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        text = request.form["text"]
        try:
            # Realizar la predicción
            prediction = model.predict([text])[0]
            return render_template("index.html", text=text, prediction=prediction)
        except Exception as e:
            print("Error during prediction:")
            print(e)
            return render_template("index.html", text=text, prediction="Error during prediction")
    return render_template("index.html", text="", prediction="")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
