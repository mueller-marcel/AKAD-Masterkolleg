from models.Question import Question
from models.RiskProfile import RiskProfile

def create_explanation_prompt() -> str:
    """
    Create the explanation prompt to explain the behavior experiment
    :returns The explanation prompt in the German language
    """

    return str()


def create_question_prompt(risk_profile: RiskProfile, questions: list[Question]) -> str:
    """
    Creates the prompt to ask a question of the behavior experiment using the given risk profile
    :param risk_profile: The risk profile to use
    :param questions: The question of the behavior experiment
    :returns: The prompt to ask in the German language
    """
    return str()