import openai

# set my openAI key
openai.api_key = "sk-proj-hhcZnC2C74tGqBNQZ7grT3BlbkFJXvi1vrQsVgpJgBtly7tl"


def create_quote(prompt):
    # create a prompt for the openAI API
    api_prompt = f"Give me a famous quote and the author related to {prompt}."

    try:
        #Get the reponse from the OpenAI API
        response = openai.Completion.create(
            engine = "text-davinci-004",
            prompt=api_prompt,
            max_token=50,
            temperature=0.7,
            top_p=1.0
        )

        # extract the text from the response
        quote = response.choices[0].text.strip()
        return quote
    except Exception as e:
        return f"An error occured: {e}"
    
# Example usage
if __name__ == "__main__":
    user

