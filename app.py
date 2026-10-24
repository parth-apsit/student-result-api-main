from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Student Result API is running"})

@app.route("/result", methods=["POST"])
def result():
    data = request.get_json(silent=True) or {}
    marks = data.get("marks")

    if (not isinstance(marks, (int, float))
            or isinstance(marks, bool)
            or not 0 <= marks <= 100):
        return jsonify({"error": "Marks must be between 0 and 100"}), 400

    return jsonify({
        "marks": marks,
        "result": "PASS" if marks >= 40 else "FAIL"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
