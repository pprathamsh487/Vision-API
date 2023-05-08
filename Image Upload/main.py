import requests
import json
from flask import Flask, jsonify, request, render_template
from base64Converter import imageConverter
app = Flask(__name__)


@app.route('/', methods =  ['GET','POST'])
def home():
    """Docstring"""
    if(request.method == 'GET'):
        return render_template('index.html')
    
    if request.method == 'POST':
        img = request.files['image']
        img = img.read()
        print("Image after reading", img)
        base64Img = imageConverter(image=img)
        
        ## call the Vision API
        
        url = "https://vision.googleapis.com/v1/images:annotate?key=AIzaSyBb5vuGhpE22TCt0H1ZVk5jADy4qx_01g8"
        data = {
            "requests": [
                {
                    "image": {
                    "content": base64Img
                    },
                    "features": [
                    {
                        "type": "TEXT_DETECTION",
                        "maxResults": 10
                    }
                    ]
                }
            ]
        }
        response = requests.post(url,json=data)
        with open('output.json', 'w') as outfile:
            json.dump(response.json(), outfile)
        print("data is", data)
        print("Final Vision Response",response.json)
        desc = response.json()['responses'][0]['textAnnotations'][0]['description']
        # return jsonify({"message":"Image uploaded successfully","status-code":"200"})
        return render_template('output.html', output=desc)
if __name__ == "__main__":
    app.run(debug=True)