from flask import request, jsonify, Response, json
from flask.views import MethodView
from models.app_data import AppData


class QuestionsController(MethodView):
    """A class-based view that dispatches request methods to the corresponding
        class methods. For example, if you implement a ``get`` method, it will be
        used to handle ``GET`` requests. :
    """

    @staticmethod
    def get(question_id=None):
        """
        responds to get requests
        :param question_id:
        :return:
        """
        questions = AppData.stack_overflow_db
        # Return a specific question
        if question_id:
            question_ = {}
            for qtn in questions:
                if qtn['question_id'] == question_id:
                    question_ = {
                        'question_id': qtn['question_id'],
                        'title': qtn['title'],
                        'Answers': qtn['Answers']
                    }

            return jsonify(question_)
        else:
            # return all questions
            return jsonify({'questions': questions})

    @staticmethod
    def post(question_id=None):
        """
        responds to post requests
        :param question_id:
        :return:
        """
        if str(request.url_rule) == "/api/v1/questions/":
            return QuestionsController.handle_post_question()

        if str(request.url_rule) == "/api/v1/questions/<int:question_id>/answers/":
            return QuestionsController.handle_answers(question_id)

        return 'Errors'  # ReturnHandlers.could_not_process_request()

    # Post a question
    @staticmethod
    def handle_post_question():
        questions = AppData.stack_overflow_db
        request_data = request.get_json()
        if valid_question(request_data):
            post_question = {
                'question_id': request_data['question_id'],
                'title': request_data['title'],
                'person_who_asked': request_data['person_who_asked'],
                'the_question': request_data['the_question'],
                'Answers': request_data['Answers']
            }
            questions.append(post_question)
            response = Response("", 201, mimetype="application/json")
            response.headers['Location'] = "questions/" + str(request_data['question_id'])
            return response
        else:
            bad_object = {
                "error": "Invalid Question Format",
                "help format": "Request format should be {'question_id': '5','title': 'API',"
                            "'person_who_asked': '7.99','the_question': 'Your Question' }"
            }
            response = Response(json.dumps(bad_object), status=400, mimetype="application/json")
            return response

    # Adding an answer to a specific question
    @staticmethod
    def handle_answers(question_id):
        questions = AppData.stack_overflow_db
        request_data = request.get_json()
        for question_ in questions:
            if question_['question_id'] == question_id:
                question_['Answers'].append(request_data['Answers'])
            else:
                continue
        response = Response("", status="204")
        response.headers['Location'] = "/api/v1/questions/" + str(question_id) + "/"
        return response

# validate a question
def valid_question(questionObject):
    if "title" in questionObject and "the_question" in questionObject and "person_who_asked" and "question_id" in questionObject:
        return True
    else:
        return False