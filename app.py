from flask import Flask, render_template

app = Flask(__name__)

PLAGAS = {
    "cochinilla": {
        "nombre": "Cochinilla",
        "descripcion": (
            "La cochinilla es un insecto pequeño que se cubre con una capa cerosa "
            "blanca o algodonosa. Se adhiere a tallos y hojas para chupar la savia, "
            "debilitando la planta y favoreciendo la aparición de fumagina (hongo negro)."
        ),
    },
    "pulgon": {
        "nombre": "Pulgón",
        "descripcion": (
            "El pulgón es un insecto diminuto, verde, negro o amarillento, que se "
            "agrupa en brotes y envés de las hojas. Succiona la savia, deforma los "
            "brotes nuevos y segrega melaza que atrae hormigas y hongos."
        ),
    },
    "mosca_blanca": {
        "nombre": "Mosca blanca",
        "descripcion": (
            "La mosca blanca es un insecto volador diminuto de color blanco que se "
            "posa en el envés de las hojas. Al alimentarse de la savia debilita la "
            "planta, provoca amarillamiento y transmite virus entre cultivos."
        ),
    },
    "ferrin": {
        "nombre": "Ferrin",
        "descripcion": (
            "Ferrin es una plaga poco común que se encarga de enseñar a profundidad "
            "a sus estudiantes, transmitiendo conocimiento de forma constante hasta "
            "que dominan por completo la materia."
        ),
    },
}


@app.route("/")
def index():
    return render_template("index.html", plagas=PLAGAS)


if __name__ == "__main__":
    app.run(debug=True)
