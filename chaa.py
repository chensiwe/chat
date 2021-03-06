from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

class SimpleChat():

    def __init__(self):
        self.chatbot = ChatBot('myBot',
                               storage_adapter="chatterbot.storage.MongoDatabaseAdapter",
                               logic_adapters=[
                                   {
                                       'import_path': 'chatterbot.logic.BestMatch'
                                   },
                                   {
				'import_path': 'chatterbot.logic.LowConfidenceAdapter',
                                       'threshold': 0.6,
                                       'default_response': '正在学习中'
                                   }
                               ],
                               input_adapter="chatterbot.input.VariableInputTypeAdapter",
                               output_adapter="chatterbot.output.TerminalAdapter",
                               database_uri='mongodb://admin:admin@127.0.0.1:27017/admin?authMechanism=MONGODB-CR',
                               database='chatbot'
                               )

        self.chatbot.set_trainer(ListTrainer)
        self.chatbot.train("chatterbot.corpus.chinese")

    def get_response(self, info):
        #返回信息
        return str(self.chatbot.get_response(info))

if __name__ == '__main__':
    chat = SimpleChat()
    res = chat.get_response('你好啊')
    print(res)
