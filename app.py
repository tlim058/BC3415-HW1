from flask import Flask, render_template, request
import google.generativeai as palm
import textblob

# Configure the PaLM API with your key
api = "AIzaSyBI7-gHGhxr_yyfg_xb8fkywnzvXIK-lzs"
palm.configure(api_key=api)
model = {"model": "models/chat-bison-001"}

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/financial_FAQ", methods=["GET", "POST"])
def financial_FAQ():
    return render_template("financial_FAQ.html")

@app.route("/makersuite", methods=["GET", "POST"])
def makersuite():
    if request.method == "POST":
        q = request.form.get("q")
        try:
            model = palm.GenerativeModel(model_name="gemini-1.5-flash")
            response = model.generate_content([q])
        except Exception as e:
            response = f"Error: {str(e)}"
        return render_template("makersuite.html", r=response.text)
    return render_template("makersuite.html")

@app.route("/joke", methods=["GET", "POST"])
def joke():
    j = "Which Singapore MRT is the oldest? Pioneer."

    if request.method == "POST":
        return render_template("joke.html", joke=j)
    
    return render_template("joke.html")

@app.route("/textblob", methods=["GET", "POST"])
def textblob():
    return render_template("textblob.html")

@app.route("/makersuite2", methods=["GET", "POST"])
def makersuite2():
    if request.method == "POST":
        t = request.form.get("t")
        return render_template("makersuite2.html", sentiment=textblob.TextBlob(t).sentiment)
    return render_template("makersuite2.html")

if __name__ == "__main__":
    app.run(debug=True)
