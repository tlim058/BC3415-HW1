from flask import Flask, render_template, request
import google.generativeai as palm

# Configure the PaLM API with your key
api = "AIzaSyCSoos0XSU8eMk2a0vP6nyEuQerp8HrLEI"
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
            r = palm.chat(messages=q, **model)
            response_message = r.messages[-1]['content']  
        except Exception as e:
            response_message = f"Error: {str(e)}"
        return render_template("makersuite.html", r=response_message)
    return render_template("makersuite.html")

@app.route("/joke", methods=["GET", "POST"])
def joke():
    j = "Which Singapore MRT is the oldest? Pioneer."

    if request.method == "POST":
        return render_template("joke.html", joke=j)
    
    return render_template("joke.html")

if __name__ == "__main__":
    app.run(debug=True)
