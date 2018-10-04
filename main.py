from flask import Flask, render_template,  request


app = Flask(__name__)

def convert_dollars(amount):
    RATE = 4.9769 #this is the dollar cedi rate
    #return the cedi equivalent
    cedis = amount * RATE
    return round(cedis, 2)

@app.route("/convert", methods=["GET","POST"])
def convert():
    if request.method == 'POST':
        amount = request.form["amount"]
        cedis = convert_dollars(float(amount))
    return render_template("result.html", val=cedis)

@app.route("/")
def homepage():
    return render_template("home.html")


if __name__ == '__main__':
    app.run()