from guizero import App, Text, TextBox, PushButton, Slider, Picture
from PIL import Image

# function
def say_my_name():
    welcome_message1.value = my_name.value
    my_name.value = ''

def change_text_size(slider_value):
    welcome_message.size = slider_value

# start
app = App(title="Hello world")
# my text const
text_header1 = 'Welcome to my first python app '
text_header2 = 'Welcome to my app'

# text
welcome_message1 = Text(app, text=text_header1)
welcome_message = Text(app, text=text_header2, size=20, font="Times New Roman", color='red')
# input my name
my_name = TextBox(app,width=40,height=5,multiline=1)
# buton
update_text = PushButton(app, command=say_my_name, text="Display my name")
# slider size
text_size = Slider(app, command=change_text_size, start=10, end=80)
#gziki-chamcham.gif
my_cat = Picture(app, image='gziki-chamcham.gif')
#




# run application
app.display()

