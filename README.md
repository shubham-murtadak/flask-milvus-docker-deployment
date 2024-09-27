# Milvus Flask Integration Documentation 🚀

## Overview 🌟

This documentation provides instructions for setting up a Flask application that integrates with a Milvus database using Docker. The setup allows you to run both Milvus and Flask containers easily.

## Included Files 📁

- `app.py`: Contains the code for the Flask application and its integration with Milvus.
- `Dockerfile`: Defines the instructions to build the Flask image.
- `docker-compose.yml`: Manages the Milvus and Flask containers, ensuring they can communicate effectively.
- `requirements.txt`: Lists the required Python packages for the Flask application.

## Getting Started 🛠️

### Prerequisites ✅

- Ensure you have [Docker](https://www.docker.com/get-started) and [Docker Compose](https://docs.docker.com/compose/install/) installed on your machine.

### Installation Steps 📥

1. **Download the Project**
   - Ensure you have the project files (app.py, Dockerfile, docker-compose.yml, requirements.txt) in a single directory.

2. **Navigate to Project Directory**
   ```bash
   cd path/to/your/project
   ```

3. **Run the Docker Containers**
   Use the following command to build and start the containers:
   ```bash
   docker-compose up --build
   ```

### Addressing Errors ⚠️

1. **Version Compatibility**:
   - Ensure the version of `pymilvus` matches the version of the Milvus server.
   - For Milvus server version **2.4.5** (as specified in `docker-compose.yml`):
     - Use the following version of `pymilvus` in your `requirements.txt`:
       ```
       pymilvus==2.4.4
       ```

### Container Addresses 🌐

- **Milvus Container**: 
  - Host: `172.18.0.4`
  - Port: `19530`

- **Flask Container**: 
  - Address: `http://localhost:5000/`

### Accessing the Application 🖥️

- After successfully running the command, open your web browser and go to `http://localhost:5000/` to access the Flask application, which connects to the Milvus database.

### Important Note ⚡

- Before running the `docker-compose up --build` command, ensure that any previous instances of the Milvus container are stopped. You can stop any running containers with the following command:
  ```bash
  docker stop <container_id>
  ```

## Conclusion 🎉

By following the above steps, you should have both the Milvus and Flask containers running, allowing you to interact with the database through your Flask application. For more information, refer to the [Milvus documentation](https://milvus.io/docs/release_notes.md). 

---

### Author ✍️
**Shubham Murtadak**

If this documentation helps you, please consider giving it a star! ⭐

--- 
