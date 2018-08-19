from flask import Flask, jsonify, request, Response, json
app = Flask('__name__')

questions = [
    {'ID':'1', 'Title':'Restful APIs', 'Question':'How can i build Restful APIs with flask framework'},
    {'ID':'2', 'Title':'Restful APIs', 'Question':'How can i build Restful APIs with flask framework'},
    {'ID':'3', 'Title':'Restful APIs', 'Question':'How can i build Restful APIs with flask framework'}
]

@app.route('/', methods=['GET'])
def test():
    return jsonify({'message':'Welcome to StackOverflow-lite'})

# get all questions
@app.route('/questions', methods=['GET'])
def get_questions():
    return jsonify(questions)

# add a question
@app.route('/questions', methods=['POST'])
def add_question():
    request_data  = request.get_json()
    if (valid_question(request_data)):
        qtn = {
            'ID': request_data['ID'],
            'Title': request_data['Title'],
            'Question': request_data['Question']
        }
        questions.append(qtn)
        response = Response("", 201, mimetype="application/json")
        response.headers['Location'] = "questions/" + str(request_data['ID'])
        return response
    else:
        bad_object = {
            "error": "Invalid question object",
            "help_string":
                "Request format should be {'Question': 'What are Restful APIs?',"
                "'Title': 'Restful API','ID': 1 }"
        }
        response = Response(json.dumps(bad_object), status=400, mimetype="appliation/json")
        return response
            

# get a question
@app.route('/questions/<int:ID>', methods=['GET'])
def get_a_question(ID):
    qtn = {}
    for Qtn in questions:
        if Qtn['ID'] == ID:
            qtn = {
                'Title':Qtn['Title'],
                'Question':Qtn['Question']
            }
    return jsonify(qtn)

# validate a question
def valid_question(questionObject):
    if "Title" in questionObject and "Question" in questionObject and "ID" in questionObject:
        return True
    else:
        return False




