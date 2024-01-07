import openai

openai.api_key "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"

completion = openai.ChatCompletion.create (model="gpt-3.5-turbo", messages=[{"role": "user": "write an essay about peguins"}])
print(completion.choices[0].message.content)