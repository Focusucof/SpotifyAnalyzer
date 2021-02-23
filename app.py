from main import *

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def formRes():
    pl_id = request.form['playlist']
    getandsend(pl_id, offset)
    return render_template('result.html')