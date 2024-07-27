from flask import Flask

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
