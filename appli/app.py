from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/")
def home():
    return jsonify(
        {
            "project": "TP-Sec-Web",
            "status": "ok",
            "message": "Application web initialisee pour l'etape 2.",
        }
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)