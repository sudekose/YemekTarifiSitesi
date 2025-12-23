from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    malzemeler = [
        {"isim": "Domates", "resim": "domates.png"},
        {"isim": "Patates", "resim": "patates.png"},
        {"isim": "Soğan", "resim": "sogan.png"},
        {"isim": "Biber", "resim": "biber.png"},
    ]
    return render_template("index.html", malzemeler=malzemeler)

if __name__ == "__main__":
    app.run(debug=True)
