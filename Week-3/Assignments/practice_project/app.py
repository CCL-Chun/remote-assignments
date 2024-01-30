from flask import (Flask, request, render_template,json,
                   redirect, url_for, make_response)

app = Flask(__name__)

def get_cookies():
    try:
        data = json.loads(request.cookies.get('users'))
    except TypeError:
        data = {}
    return data

@app.route("/sum.html")
def add():
    return render_template("add.html")

@app.route("/data")
def sigma():
    num = request.args.get('number',None)
    if num is None:
        return "Lack of Parameter."
    try:
        num_int = int(num) #change to int type
    except ValueError: #not [0-9]*
        return "Wrong Parameter. Don't put any non-integer value."
    if num_int <= 0: #only accept positive integer
        return "Don't put any negative value or zero."

    result = sum(range(num_int + 1)) #sigma sum
    return str(result) #return a string is important

@app.route('/myName')
def myName():
    name = get_cookies()
    if name:
        return render_template("knownuser.html", name = name['name'])
    else:
        return render_template("entry.html",saves = name)

@app.route('/trackName', methods=['POST'])
def trackName():
    response = make_response(redirect(url_for('myName')))
    data = get_cookies()
    data.update(dict(request.form.items()))
    response.set_cookie('users',json.dumps(data))
    return response

if __name__ == "__main__":
    app.run(port=3000,debug=True)
