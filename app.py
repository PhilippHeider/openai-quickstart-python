import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")

from flask import Flask, redirect, render_template, request, url_for
app = Flask(__name__)
app.debug = True

@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        animal = request.form["animal"]
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=generate_prompt(animal),
            temperature=0.8,
            max_tokens=256
        )
        return redirect(url_for("index", result=response.choices[0].message.content))

    result = request.args.get("result")
    return render_template("index.html", result=result)

def generate_prompt(animal):
    prompt_messages = [
        {"role": "system", "content": "You are an assistant and you will be provided with animals! Your task is to generate aimal names."},
        {"role": "user", "content": "Cat"},
        {"role": "assistant", "content": "Captain Sharpclaw, Agent Fluffball, The Incredible Feline"},
        {"role": "user", "content": "Dog"},
        {"role": "assistant", "content": "Ruff the Protector, Wonder Canine, Sir Barks-a-Lot"},
        {"role": "user", "content": animal}
    ]
    return prompt_messages