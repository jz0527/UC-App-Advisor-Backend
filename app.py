from flask import Flask

# Airbase API token: patFpWNV63Ls1yb0y.8b397c78ea81e0f70c0e3ad45d1dddec71e9d8c2efcc7290a59f630f29ec2042

app = Flask(__name__)

@app.route('/')
def home():
    return "welcome to the home page."

@app.route('/application_advising')
def application_advising():
    return "Here is where you can get help for your applications."

@app.route('/major_advising')
def major_advising():
    return "Here is where you can get help and support for picking what major to study"

@app.route('/course_selection_advice')
def course_selection_advice():
    return "here is where you can get course selection advice"

@app.route('/additional_resources')
def additional_resources():
    return "here is where you can get additional resources"
    



if __name__ == "__main__":
    app.run(debug=True)
