from hosts_controller import get_hosts, add_host

from flask import Flask, jsonify, request, render_template, send_from_directory


app = Flask(__name__)


@app.route("/api/hosts", methods=['GET'])
def api_get_hosts():
    return jsonify(get_hosts())

@app.route("/api/hosts", methods=['POST'])
def api_add_host():
    return jsonify(add_host(request.get_json()))

@app.route("/ui", methods=['GET'])
def ui_main():
    return render_template('tableView.html', hosts=get_hosts())


# resources route
@app.route('/public/<path:path>')
def send_resource(path):
    """
    Router for public assets
    """
    print(f"getting {path}")
    return send_from_directory('public', path)
