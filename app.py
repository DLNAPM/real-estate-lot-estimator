from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/estimate", methods=["POST"])
def estimate():
    data = request.get_json()
    try:
        lot_size = float(data["lotSize"])
        estimate_value = round(lot_size * 127, 2)
        return jsonify({
            "estimate": estimate_value,
            "city": data["city"],
            "zipCode": data["zipCode"]
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=81)
