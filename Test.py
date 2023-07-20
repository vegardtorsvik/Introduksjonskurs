import os
import openai

# Load environment variables

openai.api_key = os.getenv("OPENAI_API_KEY")

# Define two texts
text1 = 'We are clean, we are green'
text2 = 'YOUR_SECOND_TEXT_HERE'

# Define a prompt to evaluate the level of greenwashing
prompt_template = 'Given the following text, please rate its level of greenwashing on a scale from 1 (no greenwashing) to 5 (extreme greenwashing). Also, provide a brief explanation of your rating. The text is: "{}"'

# Define a function to evaluate greenwashing
def evaluate_greenwashing(text):
    prompt = prompt_template.format(text)
    response = openai.Completion.create(
      engine="text-davinci-004",
      prompt=prompt,
      temperature=0.5,
      max_tokens=200
    )
    return response.choices[0].text.strip()

# Evaluate greenwashing for both texts
rating_text1 = evaluate_greenwashing(text1)
rating_text2 = evaluate_greenwashing(text2)

print(f"Text 1 Greenwashing Evaluation: {rating_text1}")
print(f"Text 2 Greenwashing Evaluation: {rating_text2}")