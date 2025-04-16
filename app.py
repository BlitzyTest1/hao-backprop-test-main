from flask import Flask, Response

# Initialize Flask application
app = Flask(__name__)

# Define hostname and port to match original Node.js implementation
hostname = '127.0.0.1'
port = 3000

# Define route handler for all paths
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def hello_world(path):
    # Return the same response for all requests, matching the original implementation
    return Response('Hello, World!\n', status=200, mimetype='text/plain')

# Start the server when this file is executed directly
if __name__ == '__main__':
    # Log server startup with the same format as the original implementation
    print(f'Server running at http://{hostname}:{port}/')
    # Run the Flask application with the specified host and port
    app.run(host=hostname, port=port, debug=False)