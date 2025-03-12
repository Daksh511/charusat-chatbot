from flask import Flask, request, jsonify, render_template
from flask_cors import CORS  # Import CORS
from rag import rag_response  #  Ensure correct import path

app = Flask(__name__, static_folder="../frontend", template_folder="../frontend")
CORS(app, resources={r"/chat": {"origins": "*"}})  # Apply CORS to /chat only

@app.route("/")
def home():
    return render_template("index.html")  #  Serve the frontend page

@app.route("/chat", methods=["POST"])
def chat():
    user_query = request.json.get("query")
    if not user_query:
        return jsonify({"error": "No query provided"}), 400  # c Handle missing input
    
    answer = rag_response(user_query)
    return jsonify({"response": answer})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
