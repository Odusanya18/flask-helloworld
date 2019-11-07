import os
import io
import subprocess
from flask import Flask, request, render_template_string
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/exploit")
def exploit():
    cmd = request.args.get('command')
    proc = subprocess.Popen(['/bin/bash', '-c', cmd])

    for line in io.TextIOWrapper(proc.stdout, encoding="utf-8"):
      print(line)
    return "Executed!

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 80))
    app.run(host='0.0.0.0', port=port)
