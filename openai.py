import openai

# Set up your OpenAI API key
openai.api_key = "YOUR_API_KEY"

# Craft a prompt
code_snippet = """
Your code snippet here...
"""
prompt = f"Explain the purpose of the following code:\n\n{code_snippet}"

# Make an API request
response = openai.Completion.create(
    engine="davinci-codex",  # You can choose another suitable engine
    prompt=prompt,
    max_tokens=100  # Adjust as needed
)

# Extract the generated explanation
explanation = response.choices[0].text.strip()

print("Generated Explanation:", explanation)
