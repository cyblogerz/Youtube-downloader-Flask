from flask import Flask,render_template,request,redirect
from pytube import YouTube
import os
app = Flask(__name__)

def musdwnld(url):
    yt = YouTube(url)
    stream = yt.streams.filter(only_audio=True).first()
    print("Downloading song ")
    output = stream.download("C:\\Users\\pranavajay\\Music\\")
    base,ext = os.path.splitext(output)
    new_file = base +'.mp3'
    os.rename(output, new_file)
    print("Downloaded")
    # speak("Song downloaded succesfully!")

@app.route('/',methods = ["POST","GET"])
def main():
    if request.method == "POST":
        url = request.form["url"]
        musdwnld(url)
        

    return render_template('index.html')



if __name__ == "__main__":
    app.run(debug=True)