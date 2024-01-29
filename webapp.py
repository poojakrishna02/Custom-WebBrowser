from flask import Flask, flash, redirect, render_template, request,session,abort

app = Flask(__name__)

@app.route("/")
def Hello():
    return "Hello World!!"

@app.route("/test")
def test():
    return render_template('demo.html')

if __name__ == "__main__":
    app.run()
    