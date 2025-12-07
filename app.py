from flask import Flask, render_template
import redis

app = Flask(__name__)

# Connect to local Redis running on WSL
r = redis.Redis(host="redis", port=6379, decode_responses=True)

@app.route("/")
def index():
    count = r.incr("visits")  # increment Redis key
    return render_template("index.html", count=count)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
