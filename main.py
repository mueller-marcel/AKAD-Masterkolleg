from openai import OpenAI

# Initialize the OpenAI client and define parameters
client = OpenAI()
MODEL = "gpt-5"
TEMPERATURE = 0.5

# Prompt templates
explanation_prompt = """Du nimmst an einem wissenschaftlichen Verhaltensexperiment teil. 
Bitte verhalte dich wie eine menschliche Versuchsperson, die Entscheidungen unter Risiko trifft.

Ablauf:
1. Zuerst erhältst du Fragen zu deinem Risikoprofil (Demografie, Entscheidungsstil, Informationsverhalten, Zeitpräferenz).
2. Danach werden dir Entscheidungsaufgaben präsentiert, bei denen du zwischen Option A (sicher) und Option B (riskant) wählen musst.

Wichtige Regeln:
- Es gibt keine richtigen oder falschen Antworten.
- Antworte jeweils so, wie du spontan entscheiden würdest.
- Handle konsistent und ohne Meta-Kommentare.
- Begründe deine Antworten nicht.
- Antworte nur direkt auf die Fragen, ohne zusätzliche Erläuterungen.

Sobald du bereit bist, schreibe: „Bereit“."""

risk_profile = {
    "Alter": 34,
    "Beruf/Tätigkeit": "Softwareentwickler",
    "Lebenssituation": "in Partnerschaft",
    "Entscheidungsstil_1_7": 5,
    "Informationsverhalten_1_7": 6,
    "Zeitpräferenz": "später"
}

def ask(prompt: str, temperature: float = TEMPERATURE) -> str:
    """
    Asks the model a question.
    :param prompt: The question to ask
    :param temperature: The temperature to use
    :return: The response of the model
    """

    response = client.responses.create(
        model=MODEL,
        input=prompt,
        temperature=temperature
    )

    return response.output_text