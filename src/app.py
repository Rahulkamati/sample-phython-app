from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory "database" for demo purposes
items = [
    {"id": 1, "name": "Apple"},
    {"id": 2, "name": "Banana"},
]


@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Welcome to the Sample Flask API"})


@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "ok"})


@app.route("/items", methods=["GET"])
def get_items():
    return jsonify(items)


@app.route("/items/<int:item_id>", methods=["GET"])
def get_item(item_id):
    item = next((i for i in items if i["id"] == item_id), None)
    if item is None:
        return jsonify({"error": "Item not found"}), 404
    return jsonify(item)


@app.route("/items", methods=["POST"])
def create_item():
    data = request.get_json()
    if not data or "name" not in data:
        return jsonify({"error": "Missing 'name' field"}), 400

    new_item = {
        "id": items[-1]["id"] + 1 if items else 1,
        "name": data["name"],
    }
    items.append(new_item)
    return jsonify(new_item), 201


if __name__ == "__main__":
    app.run(debug=True)