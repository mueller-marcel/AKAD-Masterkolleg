from models.Question import Question
from models.QuestionFrame import QuestionFrame
from models.RiskProfile import RiskProfile
from models.TimePreference import TimePreference


def create_explanation_prompt() -> str:
    """
    Create the explanation prompt for the behavior experiment
    :return: The prompt to explain the behavior experiment in the German language
    """

    return str()

def create_question_prompt(risk_profile: RiskProfile, questions: list[Question]) -> str:
    """
    Creates the prompt to ask a question of the behavior experiment using the given risk profile
    :param risk_profile: The risk profile to use
    :param questions: The question of the behavior experiment
    :returns: The prompt to ask in the German language
    """

    prompt = f"""Du nimmst an einem wissenschaftlichen Verhaltensexperiment teil. 
    Bitte verhalte dich wie eine menschliche Versuchsperson, die Entscheidungen unter Risiko trifft.
    
    Wichtige Regeln:
    - Es gibt keine richtigen oder falschen Antworten.
    - Antworte jeweils so, wie du spontan entscheiden würdest.
    - Handle konsistent und ohne Meta-Kommentare.
    - Begründe deine Antworten nicht.
    - Antworte nur direkt auf die Fragen, ohne zusätzliche Erläuterungen.
    
    Du bist eine Person, die {risk_profile.age} Jahre alt ist und als {risk_profile.profession} tätig ist.
    Du bist aktuell {risk_profile.marital_status}. {__create_decision_style_description(risk_profile.decision_style)}
    {__create_information_style_description(risk_profile.information_style)}
    
    Nachfolgend sind die Fragen:
    """

    # Append the questions to the prompt
    for question in questions:
        prompt += f"\n{__create_question_description(question)}"

    # Append the instructions for the output format to the prompt
    prompt += "Bitte gib die Antwort zu den Fragen zusammen mit der Nummer der Frage aus, sodass ich deine Antworten zuordnen kann."

    return prompt


def __create_decision_style_description(decision_style: int) -> str:
    """
    Creates the description of the decision style
    :param decision_style: The numeric value of the decision style
    :returns: The description of the decision style
    """

    match decision_style:
        case 1:
            return "Bei riskanten Entscheidungen entscheidest intuitiv aus dem Bauch heraus und folgst spontanen Eindrücken."
        case 2:
            return "Bei riskanten Entscheidungen entscheidest intuitiv aus dem Bauch heraus und folgst spontanen Eindrücken."
        case 3:
            return "Bei riskanten Entscheidungen vertraust du der eigenen Erfahrung, prüfst allerdings kurz nach."
        case 4:
            return "Bei riskanten Entscheidungen vertraust du der eigenen Erfahrung, prüfst allerdings kurz nach."
        case 5:
            return "Bei riskanten Entscheidungen gehst du überlegt vor, wägst Argumente ab und nutzt Vergleiche."
        case 6:
            return "Bei riskanten Entscheidungen gehst du überlegt vor, wägst Argumente ab und nutzt Vergleiche."
        case 7:
            return "Bei riskanten Entscheidungen analysierst du sehr systematisch, nutzt Zahlen, Simulationen oder Vergleiche zur Entscheidungsfindung."
        case _:
            raise ValueError("Invalid decision style")


def __create_information_style_description(information_style: int) -> str:
    """
    Creates the description of the information style
    :param information_style: The numeric value of the information style
    :returns: The description of the information style
    """

    match information_style:
        case 1:
            return "Vor riskanten Entscheidungen recherchierst du kaum, sondern entscheidest spontan."
        case 2:
            return "Vor riskanten Entscheidungen recherchierst du kaum, sondern entscheidest spontan."
        case 3:
            return "Vor riskanten Entscheidungen recherchierst du bei Bedarf gezielt nach Informationen, die dir helfen bei der Entscheidungsfindung."
        case 4:
            return "Vor riskanten Entscheidungen recherchierst du bei Bedarf gezielt nach Informationen, die dir helfen bei der Entscheidungsfindung."
        case 5:
            return "Vor riskanten Entscheidungen recherchierst ausgiebig, vergleichst mehrere Optionen und liest dich gut ein."
        case 6:
            return "Vor riskanten Entscheidungen recherchierst ausgiebig, vergleichst mehrere Optionen und liest dich gut ein."
        case 7:
            return "Vor riskanten Entscheidungen recherchierst sehr gründlich, liest Bewertungen oder Studien bevor du dich entscheidest"
        case _:
            raise ValueError("Invalid information style")


def __create_time_preference_description(time_preference: TimePreference) -> str:
    """
    Creates the description of the time preference
    :param time_preference: The time preference either now or later
    :returns: The description of the time preference
    """

    match time_preference:
        case 1:
            return """Bezüglich deiner zeitlichen Präferenz bei Entscheidungen würdest du lieber einen sofortigen
            Gewinn bevorzugen, als einen höheren Gewinn in der Zukunft. Du bist also tendenziell eher ungeduldig und impulsiv."""
        case 2:
            return """Bezüglich deiner zeitlichen Präferenz bei Entscheidungen würdest du lieber auf einen höheren Gewinn in der Zukunft
            warten als sofort einen Gewinn zu nehmen, wenn du die Wahl hättest. Du bist also tendenziell eher geduldig und optimistisch."""
        case _:
            raise ValueError("Invalid time preference")


def __create_question_description(question: Question) -> str:
    """
    Creates the string description of the question
    :param question: Contains all the information about the question
    :return: The string description of the question
    """

    question = f"""Frage Nummer {question.number}: Stell dir vor du hättest ein Vermögen von {question.net_worth} Euro zur Verfügung.
    Es gibt zwei Optionen aus denen du eine Option wählen musst.
    
    Option A: Einen sicheren {"Gewinn" if question.question_frame is QuestionFrame.WIN else "Verlust"} von {question.safe_option} Euro.
    
    Option B: Mit einer zufälligen Wahrscheinlichkeit von 50% einen {"Gewinn" if question.question_frame is 1 else "Verlust"} von {question.risk_option} Euro.
              oder einen {"Gewinn" if question.question_frame is QuestionFrame.WIN else "Verlust"} von 0 Euro mit ebenfalls 50% Wahrscheinlichkeit."""

    return question
