import openai

# Set your OpenAI GPT-3 API key
openai.api_key = 'YOUR_API_KEY'

def generate_text(prompt):
    # Example prompt engineering: Include user context
    full_prompt = f"User context: {prompt}"
    
    # Generate text using GPT-3
    response = openai.Completion.create(
        engine="text-davinci-003",  # You can choose a different engine based on your requirements
        prompt=full_prompt,
        temperature=0.7,
        max_tokens=100,
        n=1,
        stop=None
    )
    
    generated_text = response['choices'][0]['text'].strip()
    return generated_text

# Example usage
user_prompt = "Can you provide information about artificial intelligence?"
generated_response = generate_text(user_prompt)

print("User Prompt:", user_prompt)
print("Generated Response:", generated_response)
