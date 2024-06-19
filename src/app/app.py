from flask import Flask, request, render_template
import joblib
import logging

app = Flask(__name__)

# Configurar el logging para que muestre mensajes de depuración
logging.basicConfig(level=logging.DEBUG)

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
        prueba = [text]  # Convertir el texto de entrada en una lista de un solo elemento
        try:
            # Transformar el texto usando el vectorizador
            text_transformed = vectorizer.transform(prueba)
            # Realizar la predicción
            P = model.predict(text_transformed)
            # Obtener las clases del modelo
            clases = model.classes_
            # Asignar la etiqueta adecuada
            if clases[P[0]] == 0:
                prediction_label = "Negativo"
            elif clases[P[0]] == 2:
                prediction_label = "Neutro"
            else:
                prediction_label = "Positivo"
            
            return render_template("index.html", text=text, prediction=prediction_label)
        except Exception as e:
            app.logger.error("Error during prediction:")
            app.logger.error(e)
            return render_template("index.html", text=text, prediction="Error during prediction")
    return render_template("index.html", text="", prediction="")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
