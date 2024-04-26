from flask import Flask, render_template, request, redirect, url_for
from scraper import scrape_linkedin_profile 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('input_form.html')

@app.route('/process_id', methods=['POST'])
def process_id():
    linkedin_id = request.form['linkedin_id']
    return redirect(url_for('show_profile', linkedin_id=linkedin_id))

@app.route('/profile/<linkedin_id>')
def show_profile(linkedin_id):
    response = scrape_linkedin_profile(linkedin_id)
    if 'error' in response:
        return render_template('error.html', error=response['error'])
    else:
        return render_template('profile.html', data=response)

if __name__ == '__main__':
    app.run(debug=True)
