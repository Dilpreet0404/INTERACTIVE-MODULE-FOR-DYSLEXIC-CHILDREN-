""" main screen of the project 
voice module is added and completed
permutation and input by user is done
font size increses on clicking
google pic api is left
frnt screen if possible n feasible  """


# import kivy  # we generally dont import kivy
#kivy.require("1.9.0")   # just to confirm the version kivy app. can run witout this

import sys
from kivy.app import App    # to create a app
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout  # one of 5,6 layouts
from kivy.uix.textinput import TextInput # for taking input in kivy
from kivy.uix.button import Button
import os
import pyttsx
import time
import itertools


"""
f = open('yo.txt')
content = [f.strip('\n') for f in f.readlines()]
contents = [b.strip('\r') for b in content]

main =[]
entered_alphabets=raw_input("enter alphabets\n\n")
n = len(entered_alphabets)
print ("\npossible outcomes\n")
for a in itertools.permutations(entered_alphabets,n):
	if "".join(a) in contents:
		main.append("".join(a))

mains = set(main)
main_list = list(mains)
"""

main_list = ['cat']

"""login screen class
   add_widget will add a widget according to the position
   for every widget we need to pass the type of the widget"""


class LoginScreen(GridLayout):
	def __init__(self, **kwargs):
		super(LoginScreen,self).__init__(**kwargs) # for inheriting every object of gridlayout

		self.cols = 3
		def callback1(instance):
			engine = pyttsx.init()
			engine.setProperty('rate', 50)
			engine.say(btn2.text)
			engine.runAndWait()
			engine.stop()


		def callback2(instance):
			engine = pyttsx.init()
			engine.setProperty('rate', 50)
			engine.say(btn5.text)
			engine.runAndWait()
			engine.stop()		
		

		def callback3(instance):
			engine = pyttsx.init()
			engine.setProperty('rate', 50)
			engine.say(btn8.text)
			engine.runAndWait()
			engine.stop()	



		def callback4(instance):
			engine = pyttsx.init()
			engine.setProperty('rate', 50)
			engine.say(btn11.text)
			engine.runAndWait()
			engine.stop()	


		if (len(main_list)==1):
			btn1 = Button(text = "IMAGE",)
			btn2 = Button(text = main_list[0],on_press=self.on_press)
			btn3 = Button(text = "VOICE")
			btn3.bind(on_press = callback1)
			#btn2.bind(state = callback)
			self.add_widget(btn1)
			self.add_widget(btn2)
			self.add_widget(btn3)

		elif (len(main_list)==2):
			btn1 = Button(text = "IMAGE",)
			btn2 = Button(text = main_list[0],on_press=self.on_press)
			btn3 = Button(text = "VOICE")
			btn3.bind(on_press = callback1)
			btn4 = Button(text = "IMAGE",)
			btn5 = Button(text = main_list[1],on_press=self.on_press)
			btn6 = Button(text = "VOICE")
			btn6.bind(on_press = callback2)
			#btn2.bind(state = callback)
			self.add_widget(btn1)
			self.add_widget(btn2)
			self.add_widget(btn3)			
			self.add_widget(btn4)
			self.add_widget(btn5)
			self.add_widget(btn6)

		elif (len(main_list)==3):
			btn1 = Button(text = "IMAGE",)
			btn2 = Button(text = main_list[0],on_press=self.on_press)
			btn3 = Button(text = "VOICE")
			btn3.bind(on_press = callback1)
			btn4 = Button(text = "IMAGE",)
			btn5 = Button(text = main_list[1],on_press=self.on_press)
			btn6 = Button(text = "VOICE")
			btn6.bind(on_press = callback2)
			btn7 = Button(text = "IMAGE",)
			btn8 = Button(text = main_list[2],on_press=self.on_press)
			btn9 = Button(text = "VOICE")
			btn9.bind(on_press = callback3)
			#btn2.bind(state = callback)
			self.add_widget(btn1)
			self.add_widget(btn2)
			self.add_widget(btn3)			
			self.add_widget(btn4)
			self.add_widget(btn5)
			self.add_widget(btn6)
			self.add_widget(btn7)
			self.add_widget(btn8)
			self.add_widget(btn9)

		elif (len(main_list)==4):
			btn1 = Button(text = "IMAGE",)
			btn2 = Button(text = main_list[0],on_press=self.on_press)
			btn3 = Button(text = "VOICE")
			btn3.bind(on_press = callback1)
			btn4 = Button(text = "IMAGE",)
			btn5 = Button(text = main_list[1],on_press=self.on_press)
			btn6 = Button(text = "VOICE")
			btn6.bind(on_press = callback2)
			btn7 = Button(text = "IMAGE",)
			btn8 = Button(text = main_list[2],on_press=self.on_press)
			btn9 = Button(text = "VOICE")
			btn9.bind(on_press = callback3)
			btn10 = Button(text = "IMAGE",)
			btn11 = Button(text = main_list[3],on_press=self.on_press)
			btn12 = Button(text = "VOICE")
			btn12.bind(on_press = callback4)
			#btn2.bind(state = callback)
			self.add_widget(btn1)
			self.add_widget(btn2)
			self.add_widget(btn3)			
			self.add_widget(btn4)
			self.add_widget(btn5)
			self.add_widget(btn6)
			self.add_widget(btn7)
			self.add_widget(btn8)
			self.add_widget(btn9)
			self.add_widget(btn10)
			self.add_widget(btn11)
			self.add_widget(btn12)

		else:
			self.add_widget(Button(text = "out"))
			self.add_widget(Button(text = "of"))
			self.add_widget(Button(text = "range"))

    # to change the property of button when clicked 'event' is the keyword

	def on_press(self,event):
		if event.font_size == 40:
			event.font_size = 80
		else:
			event.font_size =40

""" 
basic class inheriting App Class 
SimpleKivy is the app name"""


class SimpleKivy(App):
	def build(self):
		return LoginScreen()

if __name__ == "__main__":
	#n = int(sys.stdin.readline())
	SimpleKivy() .run()