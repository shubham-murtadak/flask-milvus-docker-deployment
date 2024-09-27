from flask import Flask, jsonify
from pymilvus import connections, db

app = Flask(__name__)

@app.route("/")
def say_hello():
    # Connect to the Milvus server
    conn = connections.connect(host="172.18.0.4", port=19530)

    # Create and use a database named "my_database"
    db.create_database("my_database")
    db.using_database("my_database")

    # Retrieve a list of available databases
    db_list = db.list_database()

    return jsonify({
        "milvus_available databases": db_list,
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
