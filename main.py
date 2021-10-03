import os
from flask import Flask, jsonify, request, render_template
from transformers import pipeline

app = Flask(__name__)

model_path = "./Distilbert"

#text = "I hate you"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    classify = pipeline("sentiment-analysis", model=model_path, tokenizer=model_path)
    text = 'Text: {}'.format(request.form['text'])
    label = 'Sentiment Analysis Result: ' + classify(request.form['text'])[0]["label"]
    score = 'Sentiment Analysis Score: ' + str(round(classify(request.form['text'])[0]["score"], 5))

    return render_template('index.html', value1 = text, label = label, score = score) #




"""
@app.route("/", methods=['GET', 'POST'])
def index():
    print(request.method)
    if request.method == 'POST':
        if request.form.get('Submit') == 'Submit':
            # pass
            print("Submit")
            classify = pipeline("sentiment-analysis", model=model_path, tokenizer=model_path)
            dictionnaire = {
            'Sentiment Analysis ': classify(text),
            'Text Analyzed': text,}
          return jsonify(classify)

        else:
            # pass # unknown
            return render_template("index.html")
            
    return render_template("index.html")

"""

"""
@app.route('/',)
def classify():
  # Your function
  classify = pipeline("sentiment-analysis", model=model_path, tokenizer=model_path)

  dictionnaire = {
        'Sentiment Analysis ': classify(text),
        'Text Analyzed': text,
  }
  submit_button = form.form_submit_button(label='Submit')

  return jsonify(dictionnaire)"""




if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google Cloud
    # Run, a webserver process such as Gunicorn will serve the app.
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))