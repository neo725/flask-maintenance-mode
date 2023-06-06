from flask import Flask, abort, send_from_directory
# from MyResponse import MyResponse

app = Flask(__name__)
# app.response_class = MyResponse

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    if path.startswith('images/'):
        return send_from_directory('./', path, conditional=True)
    else:
        return example_route()

def example_route():
    response = app.make_response('Server Planned Maintenance')
    # response.status_code = 593
    response.status = '593 Server Planned Maintenance'

    html = '<html><body><img src="/images/oops-bubble-svg.png" /><h3>Server Planned Maintenance !</h3></body></html>'
    response.set_data(html)

    return response

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int("5000"), debug=True)

# apt install build-essential binutils gcc libpcre3-dev libssl-dev zlib1g-dev
