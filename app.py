from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

# Basic Part: Serve static profile page at default route ('/')
@app.route('/')
def home():
    return render_template('index.html')

# Advanced Part: Serve profile page at '/profile' and redirect default route to it
@app.route('/profile')
def profile():
    return render_template('index.html')

@app.route('/')
def redirect_to_profile():
    return redirect(url_for('profile'))

if __name__ == '__main__':
    app.run(debug=True)