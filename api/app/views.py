"""
Links class , to handle request urls,
"""

from controller.end_point import QuestionsController


class Links:
    """
    Class to generate urls via static method generate
    """

    @staticmethod
    def generate(app):
        """
        Generate urls on the app context
        It takes no arguments
        :param app: takes in the app variable
        :return: links
        """

        app.add_url_rule('/api/v1/questions/', view_func=QuestionsController.as_view('get_questions'), methods=['GET'],
                         strict_slashes=False)
        app.add_url_rule('/api/v1/questions/<int:question_id>/', view_func=QuestionsController.as_view('get_a_question'),
                         methods=['GET'],  strict_slashes=False)
        app.add_url_rule('/api/v1/questions/', view_func=QuestionsController.as_view('post_a_question'),
                         methods=['POST'],  strict_slashes=False)
        app.add_url_rule('/api/v1/questions/<int:question_id>/answers/',
                         view_func=QuestionsController.as_view('post_an_answer'), methods=['POST'],
                         strict_slashes=False)
