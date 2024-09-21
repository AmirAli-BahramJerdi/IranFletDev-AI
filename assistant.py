import os
from groq import Groq

api_key="api"

client = Groq(api_key=api_key)

class IranFletDevAI():

    def __init__(self):
        self.message = [
            {"role": "system", "content": "You are a helpful assistant."},
        ]

    def IranFletDevAIResponse(self, user_text):
        self.user_text = user_text

        while True:

            # if user says stop, then breaking the loop
            if self.user_text == "stop":
                break
            
            # storing the user question in the messages list
            self.message.append({"role": "user", "content": self.user_text})

            # getting the response from OpenAI API
            
            response = client.chat.completions.create(
                model="llama3-70b-8192",
                messages=self.message,
            )

            # appending the generated response so that AI remebers past responses
            self.message.append({"role":"assistant", "content":str(response.choices[0].message.content)})
            
            # returning the response
            #print(response['choices'][0]['message'])
            return response.choices[0].message.content