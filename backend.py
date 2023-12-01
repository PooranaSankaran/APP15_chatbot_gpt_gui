#openai used to inteact throught api
import openai
#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

class Chatbot:
    def __inti__(self):
        openai.api_key = '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'

    def get_response(self, user_input):
        response = openai.Completion.create(
            engine = 'text-davinci-003',
            prompt= user_input,
            max_tokens = 4000,# longer answer from the bot
            temperate = 0.5 # lower the temp ans will be more similar
        ).choices[0].text
        return response

if __name__ = '__main__':
    chatbot = Chatbot()
    response = chatbot.get_response('write a joke about birds')
    print(response)