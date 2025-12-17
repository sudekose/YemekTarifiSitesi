# YemekTarifiSitesi
from flask import Flask

app = Flask(__name__)

@app.route('/')
def ana_sayfa():
    return "Yemek Tarifi Sitemiz Yakında Burada!"

if __name__ == '__main__':
    app.run(debug=True)