from app import app
from flask import render_template
from .request import get_quotes 


@app.route('/index')
def index():

    random_quotes = get_quotes('random')
    print(random_quotes)
    title = 'Inspire you '

    return render_template('index.html', title=title,random=random_quotes)

if __name__ == "__main__":
    
    app.run(debug=True)