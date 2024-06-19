from flask import Flask, request, render_template
import joblib
import logging

app = Flask(__name__)


# Cargar el modelo y el vectorizador de sentimiento
try:
    model = joblib.load('/code/app/sentiment_model.joblib')
    vectorizer = joblib.load('/code/app/vectorizer.joblib')
    app.logger.info("Model and vectorizer loaded successfully.")
except Exception as e:
    app.logger.error("Error loading the model or vectorizer:")
    app.logger.error(e)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        text = request.form["text"]
        prueba = [text]  
        try:

            text_transformed = vectorizer.transform(prueba)

            P = model.predict(text_transformed)

            clases = model.classes_

            if clases[P[0]] == 0:
                prediction_label = "Negative"
            elif clases[P[0]] == 2:
                prediction_label = "Neutral"
            else:
                prediction_label = "Positive"
            
            return render_template("index.html", text=text, prediction=prediction_label)
        except Exception as e:
            app.logger.error("Error during prediction:")
            app.logger.error(e)
            return render_template("index.html", text=text, prediction="Error during prediction")
    return render_template("index.html", text="", prediction="")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
