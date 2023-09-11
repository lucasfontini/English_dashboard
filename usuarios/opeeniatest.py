import os
import openai
import json

openai.api_key = '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'



# response = openai.Completion.create(
#   model="text-davinci-003",
#   prompt="um exemplo",
#   temperature=0.9,
#   max_tokens=150,
#   top_p=1,
#   frequency_penalty=0.0,
#   presence_penalty=0.6,
#   stop=[" Human:", " AI:"]
# )

# message = response.choices[0].text
# print(message)

response = openai.Image.create(
  prompt="pato de sapato",
  n=1,
  size="1024x1024"
)
print(response)