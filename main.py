from openai import OpenAI
from openai.types.chat import ChatCompletionSystemMessageParam, ChatCompletionUserMessageParam
from PromptCreator import create_explanation_prompt, create_question_prompt
from models.Question import Question
from models.QuestionFrame import QuestionFrame
from models.RiskProfile import RiskProfile
from models.TimePreference import TimePreference

# Initialize the OpenAI client and define parameters
client = OpenAI()
MODEL = "gpt-5"
TEMPERATURE = 0.5

# Define the risk profile
risk_profile = RiskProfile(
    age=27,
    profession="Programmierer",
    marital_status="verheiratet",
    decision_style=1,
    information_style=1,
    time_preference=TimePreference.LATER,
)

# Define the questions
questions = [
    Question(
        number="G1",
        net_worth= 50000,
        safe_option= 30000,
        risk_option= 60000,
        question_frame=QuestionFrame.WIN,
    ),
    Question(
        number="G2",
        net_worth=300000,
        safe_option=40000,
        risk_option=80000,
        question_frame=QuestionFrame.WIN,
    ),
    Question(
        number="G3",
        net_worth=75000,
        safe_option=30000,
        risk_option=60000,
        question_frame=QuestionFrame.WIN,
    ),
    Question(
        number="G4",
        net_worth=200000,
        safe_option=50000,
        risk_option=100000,
        question_frame=QuestionFrame.WIN,
    ),
    Question(
        number="V1",
        net_worth=50000,
        safe_option=30000,
        risk_option=60000,
        question_frame=QuestionFrame.LOSS,
    ),
    Question(
        number="V2",
        net_worth=300000,
        safe_option=40000,
        risk_option=80000,
        question_frame=QuestionFrame.LOSS,
    ),
    Question(
        number="V3",
        net_worth=75000,
        safe_option=30000,
        risk_option=60000,
        question_frame=QuestionFrame.LOSS,
    ),
    Question(
        number="V4",
        net_worth=200000,
        safe_option=50000,
        risk_option=100000,
        question_frame=QuestionFrame.LOSS,
    ),
]

# Create the prompt to set up the model behavior
explanation_prompt = create_explanation_prompt()

# Create the prompt for the question
question_prompt = create_question_prompt(
    risk_profile=risk_profile,
    questions=questions,
)

# Create the chat history using the explanation prompt as a system message and the questions as a user message
messages = [
    ChatCompletionSystemMessageParam(role="system", content=explanation_prompt),
    ChatCompletionUserMessageParam(role="user", content=question_prompt),
]

# Send the question to the model
response = client.chat.completions.create(
    model=MODEL,
    messages=messages,
    seed=42,
    temperature=TEMPERATURE,
)

print(response.choices[0].message.content)