from flask import Flask ,render_template

app = Flask(__name__)

@app.route('/')
def g():
    return render_template('f.html')
def sayt():
    return render_template('b.html')

def d():
    return render_template('d.html')

def s():
    return render_template('s.html')    


if __name__=='__main__':
    app.run(debug=True)