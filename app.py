import requests
from flask import Flask, jsonify, make_response
app = Flask(__name__)

INSTAGRAM_MEDIA_LINK = "https://www.instagram.com/{username}/media/"

@app.route("/")
def index():
    return jsonify({
        "msg": "Welcome to PyPhotoAnalytics",
        "routes": ["/api", "/api/users", "/api/users/<username>"]
    })

@app.route("/api")
def api():
    return jsonify({"msg": "Welcome to PyPhotoAnalytics API"})

@app.route("/api/users/")
def get_users():
    return jsonify({"msg": "specify username /api/users/<username>"})

@app.route("/api/users/<username>")
def get_user_media(username):
    url = INSTAGRAM_MEDIA_LINK.format(username=username)
    response = requests.get(url);
    if response.status_code == 200:
        data = response.json()
        return jsonify(**data)
    else:
        return jsonify({"msg": "Oh gawd no"})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({"error": "Not Found"}), 404)

if __name__ == "__main__":
    app.run(debug=True)
