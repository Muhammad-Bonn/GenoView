from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    if request.method == "POST":
        content = request.form.get("fasta", "")
        known_genes = {
            "DREB2A": "Helps plants tolerate drought conditions",
            "NHX1": "Regulates sodium ions and salt tolerance",
            "WUS": "Activates callus growth",
            "ARF": "Controls root development",
            "FLC": "Affects flowering time"
        }
        matches = []
        for gene, function in known_genes.items():
            if gene in content:
                matches.append(f"{gene}: {function}")
        if not matches:
            result = "No known functional genes found."
        else:
            result = "\n".join(matches)

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
