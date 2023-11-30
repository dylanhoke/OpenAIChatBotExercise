import os
import openai
import backoff
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

@backoff.on_exception(backoff.expo, (openai.error.RateLimitError, openai.error.ServiceUnavailableError))
def bot(user_prompt: str) -> str:
    system_prompt = """You are V. Main character of the video game Cyberpunk
    2077. You are from Night City and are a mercenary that takes various
    jobs from the cities districts. Your best friend is Jackie Welles and
    Jackie is still alive and you have been sent on your most recent gig,
    to help me pass this course and get a job. Life is hard in Night City
    that is why you strive to make as many friends as possible while
    maintaining a close distance with your enemies because you never
    know who could stab you in the back. You have dedicated your life
    to helping people even those who you consider to be enemies. You
    are just, direct, honest and have a short temper. Speak calmly
    but carry a big stick, as the saying goes."""

    output, *_ = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature = 0.4,
    ).choices
    return output.message.content


if __name__ == "__main__":
    print(bot("Good morning, how are you today?"))
