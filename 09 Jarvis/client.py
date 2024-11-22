from openai import OpenAI
client = OpenAI(api_key="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")

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Write a haiku about recursion in programming."
        }
    ]
)

print(completion.choices[0].message)
