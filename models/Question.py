from models.QuestionFrame import QuestionType


class Question:
    def __init__(self, name: str, net_worth: int, safe_option: int, risk_option: int, question_type: QuestionType):
        """
        Initializes an instance of the class
        :param net_worth: The reference net worth for the question
        :param safe_option: The amount of money for the safe option
        :param risk_option: The amount of money for the risky option
        """
        self.name = name
        self.net_worth = net_worth
        self.safe_option = safe_option
        self.risk_option = risk_option
        self.question_frame = question_type
