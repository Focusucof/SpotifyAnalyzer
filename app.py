from main import *

@app.route('/')
def index():
    return render_template('index.html')

#gets input from html form
@app.route('/', methods=['POST'])
def formRes():
    pl_id = request.form['playlist']
    getandsend(pl_id, offset = 0)
    return render_template('result.html')

#disables caching
@app.after_request
def add_header(r):
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r