from app import app
from flask import render_template



@app.route('/index')
def index():

    
  
    title = 'Inspire you '

    return render_template('index.html', title=title,)

if __name__ == "__main__":
    
    app.run(debug=True)