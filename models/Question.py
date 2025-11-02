from models.QuestionFrame import QuestionFrame


class Question:
    def __init__(self, number: int, net_worth: int, safe_option: int, risk_option: int, question_frame: QuestionFrame):
        """
        Initializes an instance of the class
        :param number: The question number
        :param net_worth: The reference net worth for the question
        :param safe_option: The amount of money for the safe option
        :param risk_option: The amount of money for the risky option
        :param question_frame: The frame of the question (loss or win)
        """
        self.number = number
        self.net_worth = net_worth
        self.safe_option = safe_option
        self.risk_option = risk_option
        self.question_frame = question_frame