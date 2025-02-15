from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/comments')
def get_comments():
    comments = [
        {"name": "A", "date": "2025-02-15", "comment": "The product is great!"},
        {"name": "B", "date": "2025-02-14", "comment": "Good for its price."},
        {"name": "C", "date": "2025-02-13", "comment": "The shipment arrived very slowly."}
    ]
    return jsonify(comments)

if __name__ == '__main__':
    app.run(debug=True)
