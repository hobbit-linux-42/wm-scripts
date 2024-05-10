from os import system, environ, path
from configparser import ConfigParser
config=ConfigParser()
config_path=f"{environ['HOME']}/.config/waytrans.cfg"
if not path.isfile(config_path):
    with open(config_path, 'x') as f:
        f.write("""
[trans]
#leave from_lang blank for autodetection
from_lang=
to_lang=en
window=True

[color]
selection=FF4500
text=black
background=#7B89A4

[font]
family=Mononoki Nerd Font
style=bold
size=14""")
    system(f"notify-send 'config file created in {config_path}'")
config.read(config_path)
selection_color=config.get('color', 'selection')
system(f""" grim -g "$(slurp -c {selection_color})" -t png /tmp/waytrans.png """)

from PIL import Image
from pytesseract import pytesseract as tss
from googletrans import Translator
img = Image.open("/tmp/waytrans.png")
text = tss.image_to_string(img)
try:
    trans = Translator()
    if config.get("trans", "from_lang") != "":
        translated_text = trans.translate(text, dest=config.get("trans", "to_lang"), src=config.get("trans", "from_lang"))
    else:
        translated = trans.translate(text, dest=config.get("trans", "to_lang"))
except:
    print("Translation error. It maight be your internet connection")
    exit(1)

if not bool(config.get("trans", "window")):
    system(f"notify-send {translated.text}")
    exit(0)
    
import tkinter as tk
window=tk.Tk()
bg=config.get("color", "background")
window.configure(bg=bg)
fg=config.get("color", "text")
label = tk.Button(window, 
                  text=translated.text, 
                  command=window.destroy, 
                  bg=bg,
                  fg=fg,
                  activebackground=bg,
                  activeforeground=fg,
                  font=(config.get("font", "family"), config.get("font", "size"), config.get("font", "style")))
label.grid(row=0, column=0, padx=15, pady=15)

window.resizable(False, False)
window.mainloop()
