from flask import Flask, request, render_template
app = Flask(__name__)

@app.route("/")

@app.route("/", methods=["POST"])
def word_count():
    sentence = word_count.form.get("sentence")
    words = len(sentence.split(' '))
    chars = 0
    for c in sentence:
        chars = chars + 1
    avg = chars/words
    return render_template("index.html", word_count=words, char_count=chars,avg_word_length=avg)




    c




