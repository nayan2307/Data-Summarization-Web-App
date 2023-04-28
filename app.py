from flask import Flask, render_template
from flask import request as req
import requests
import json

app = Flask(__name__)
@app.route("/", methods = ["GET", "POST"])
def Index():
    return render_template("index.html")


@app.route("/Summarize" , methods = ["GET", "POST"])
def Summarize():
    if req.method == "POST":

        API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
        headers = {"Authorization": "Bearer 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"}


        data = req.form["data"]
        min_len =  20 #int(input("enter a min value for no. of words: " ))
        max_len= int(req.form["max_Len"])   # int(input("enter a max value for no. of words : " ))
        # this value has to sconverted to integer bcoz APi criteria is to process the "integer" and 
        # "req.form["max_Len"]" gives a string value.

        def query(payload):
            data = json.dumps(payload)
            response = requests.post(API_URL, headers=headers, json=payload)
            return json.loads(response.content.decode("utf-8"))


        output = query({
            "inputs": data,
            "parameters": {"max_length": max_len , "min_length" : min_len },
        })[0]

    

    # = requests.get('https://api.github.com')
    #print(response)

        return render_template("index.html" , result = output["summary_text"] , min_l = min_len)
    else:
        return render_template("index.html")








if __name__ == '__main__':
     app.debug= True
     app.run()




