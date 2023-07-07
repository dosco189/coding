from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        words = float(request.form['words'])
        minutes = words / 120

        if minutes < 6:
            result = f"{minutes} minutes"
        else:
            cut = minutes % 6
            words_cut = cut * 120
            result = f"{minutes} minutes is too long. Cut {words_cut} words to make it under 6 minutes."
        
        return render_template('index.html', result=result)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
