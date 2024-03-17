import openai


def generate_code(prompt):
    openai.api_key = 'your_api_key_here'

    response = openai.Completion.create(
        engine="text-davinci-003",  # Choose the GPT-3 engine
        prompt=prompt,
        max_tokens=150,  # Maximum number of tokens in the generated output
        temperature=0.7,  # Controls the randomness of the generated text
        n=1,  # Number of completions to generate
        stop=None  # Optional stop sequence to end the generation
    )

    if response and response.choices:
        return response.choices[0].text.strip()
    else:
        return None


if __name__ == "__main__":
    # Example prompt: asking GPT-3 to generate Python code to print "hello world"
    prompt = "Write Python code to print 'hello world':"

    # Generate code based on prompt
    generated_code = generate_code(prompt)

    # Print generated code
    if generated_code:
        print("Generated code:")
        print(generated_code)
    else:
        print("Failed to generate code. Please check your API key and prompt.")
