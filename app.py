from flask import Flask, request, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    known_genes = {
        "DREB2A": "Helps plants tolerate drought conditions",
        "NHX1": "Regulates sodium ions and salt tolerance",
        "WUS": "Activates callus growth",
        "ARF": "Controls root development",
        "FLC": "Affects flowering time"
    }
    if request.method == "POST":
        content = request.form.get("fasta", "")
        matches = [f"{g}: {f}" for g, f in known_genes.items() if g in content]
        result = "\n".join(matches) if matches else "No known functional genes found."
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
