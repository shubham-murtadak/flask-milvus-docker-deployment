from flask import Flask, jsonify
import os
from pymilvus import MilvusClient
from pymilvus import connections  # Import for connection-related functions

app = Flask(__name__)

# Retrieve Milvus connection details from environment variables (recommended)
milvus_host = os.getenv("MILVUS_HOST")
milvus_port = int(os.getenv("MILVUS_PORT", 19530))  # Default port if not set

@app.route("/")
def say_hello():
    """
    Connects to Milvus using either environment variables or local IP (fallback).

    Returns JSON response with a greeting and list of Milvus collections (if connection successful).
    """

    try:
        # Connect to Milvus using preferred method (environment variables)
        if milvus_host and milvus_port:
            client = MilvusClient(uri=f"http://{milvus_host}:{milvus_port}")
        else:
            # Fallback to local IP (consider service discovery for better practice)
            client = MilvusClient(uri="http://localhost:19530")

        print(f"Successfully connected to Milvus at {client.uri}")

        # List all collection names in Milvus
        collections = client.list_collections()

        return jsonify({
            "msg": f"Hello from Flask! API Key (replace with actual key)",
            "milvus_collections": collections
        })

    except connections.MilvusException as e:
        print(f"Error connecting to Milvus: {e}")
        return jsonify({
            "error": "Failed to connect to Milvus"
        }), 500  # Internal Server Error

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)