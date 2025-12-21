from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ara")
def ara():
    sorgu = request.args.get("q")
    return f"Aranan tarif: {sorgu}"

if __name__ == "__main__":
    app.run(debug=True)

# Create your views here.
