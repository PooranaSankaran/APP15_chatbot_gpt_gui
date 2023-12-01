#graphical user interface bulid using PYQ6
# And we need gpt api thorugh web
from PYQt6.QtWidgets import (QMainWindow, QTestEdit, QApplication,
                             QlineEdit,QPushButton)
import sys
from backend import Chatbot
import threading

class ChatbotWindow(QMainWindow): #parent class is QMainWindow beacause QMainWindow has it's own __init__ funtion
    def __inti__(self):
        super().__inti__() #partent class to asscess child class

        # send the user query to the chatbot in backend so, impot it
        self.chatbot = Chatbot()

        self.setMinimumSize(700, 500) #size of out app

        #Add chat area widget
        self.chat_area = QTestEdit(self) #see the entered chat in ui QTestEdit is used
        self.chat_area.setGeometry(10, 10 , 480, 320) #set size for the chat area
        # 10, 10 is start from right and above and 480, 320 is width and height
        self.chat_area.serReadOnly(True) # user can't edit in chat area just view it.


        #Add input field widget
        self.input_field = QlineEdit(self) #to add edit line QlineEdit used
        self.input_field.setGeometry(10, 340, 480, 320) # 340 is where to place from top to below 340 place it will place
        self.input_field.returnPressed.connect(self.send_message)


        #Add the button to execute
        self.button =  QPushButton('send',self) # to add button QPushButton used
        self.button.setGeometry(500, 340, 100, 40) # adjust it according to your ui have to place it
        self.button.clicked.connect(self.send_message) # when user click send button the message is save here and activate send message funtion


        self.show() # To show the outcome

    def send_message(self):
        user_input = self.input_field.text().strip()
        self.chat_area.append(f"<p style='color:#333333>'Me: {user_input}</p>")
        self.input_field.clear() # clearing the input s0, user can write new

        #send the user query to the chatbot in backend so, impot it

        # show user input in ui what he entered
        thread  = threading.Thread(target=self.get_bot_response, args=(user_input,))

    def get_bot_response(self):
        response = self.chatbot.get_response(user_input)  # step 2 the it go to backend then come here and store in response
        # we need to show the response in the chatbox ui to user to see it
        self.chat_area.append(f'Bot: {response}')





app = QApplication(sys.argv) #use to bulid app
main_window = ChatbotWindow()
sys.exit(app.exec()) #executing the operation to exit





































