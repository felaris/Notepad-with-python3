from guizero import App, TextBox, PushButton, Box, Combo, CheckBox, Slider,MenuBar

def open_file():
    with open(file_name.value, "r") as f:
                editor.value = f.read()

def save_file():
    with open(file_name.value, "w") as f:
            f.write(editor.value)

def change_font():
    editor.font = font.value

def change_color():
    editor.font = font_color

def change_text_size():
    editor.text_size = size.value
    editor.resize(1, 1)
    editor.resize("fill", "fill")
def highlight():
    editor.bg = "light blue"

def lowlight():
    editor.bg = None
app = App(title="Felix's Notepad")

def file_function():
    print("File option")

def edit_function():
    print("Edit option")
def exit_app():
    app.destroy()



file_controls = Box(app, align="top", width="fill", border=True)






file_name = TextBox(file_controls, text="text_file.txt", width=50, align="left")



save_button = PushButton(file_controls, text="Save", command=save_file, align="right")
open_button = PushButton(file_controls, text="Open", command=open_file, align="right")
exit_button = PushButton(file_controls, text="Exit", command=exit_app, align="right")

editor = TextBox(app, multiline=True, height="fill", width="fill")



preferences_controls = Box(app, align="bottom", width="fill", border=True)
font = Combo(preferences_controls, options=["courier", "times new roman", "verdana","calibri","algerian","arial","broadway","impact","ravie","rockwell","arial black","monospace",""], align="left", command=change_font)
size = Slider(preferences_controls,  align="left", start = 11, end = 150, command=change_text_size)
font_color = Combo(preferences_controls,options=['pink','red','orange','green','black','yellow'],align='left',command=change_color)
editor.when_mouse_enters = highlight


editor.when_mouse_leaves = lowlight

editor.color= font_color

app.display()
