from flask import Flask, jsonify
import os
from utility import make_get_request
app = Flask(__name__)
  @app.route('/', methods=['GET'])
  def hello():
      return 'Hello world, almost there!'
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
