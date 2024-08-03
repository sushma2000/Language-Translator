from flask import Flask, request, render_template
import re
import requests

app = Flask(__name__)# to instantiate flask

def check(language,output):
    url = "https://google-translate20.p.rapidapi.com/translate"
    #payload = "{\"target\": \""+language+"\",\"text\": \""+output+"\",\"type\": \"plain\"\r\n}"
    payload="text="+output+"&tl="+language+"&sl=en"
    print(payload)
    headers = {
    'content-type': "application/x-www-form-urlencoded",
    'x-rapidapi-key': "9441b54ff3mshcbd5ab67f3166dbp19bc0ejsna24de97f865d",
    'x-rapidapi-host': "google-translate20.p.rapidapi.com"

    }
    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.text)
    return response.json()['data']['translation']

#home page
@app.route('/')
def home():
    return render_template('home.html')

#home page
@app.route('/translator')
def translator():
    return render_template('translator.html')

#translator page
@app.route('/translate',  methods=['POST'])
def translate():
    language=request.form['type']
    output = request.form['output']
    print(output)
    translated = check(language,output)
    return render_template('translate.html',translated=translated)


if __name__ == "__main__":
    app.run(debug=True)
