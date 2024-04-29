import tkinter as tk
from os import system

window = tk.Tk()
window.geometry("243x115")
window.resizable(False, False)

shutdown_img = tk.PhotoImage(file="./icons/shutdown.png").subsample(3, 3)
reboot_image = tk.PhotoImage(file="./icons/reboot.png").subsample(3, 3)
logout_image = tk.PhotoImage(file="./icons/logout.png").subsample(3, 3)

def reboot():
    system("reboot")

def shutdown():
    system("shutdown -h now")

def logout():

    top = tk.Toplevel(window)
    top.geometry("100x70")
    top.resizable(False, False)
    tk.Label(top, text="super user").place(x=15, y=0)
    password_input = tk.Entry(top, width=12, show="*")
    password_input.place(x=5, y=15)
    def enter():
        password = password_input.get()
        system(f"echo {password} | sudo -S killall lightdm")
    tk.Button(top, text="OK", command=enter).place(x=3, y=40)
    tk.Button(top, text="NO", command=top.destroy).place(x=53, y=40)

ShutdownBT = tk.Button(window, image=shutdown_img, command=shutdown)
RebootBT = tk.Button(window, image=reboot_image, command=reboot)
LogoutBT = tk.Button(window, image=logout_image, command=logout)
CancelBT = tk.Button(window, text="Annulla", command=window.destroy)

ShutdownBT.grid(row=0, column=0)
RebootBT.grid(row=0, column=1)
LogoutBT.grid(row=0, column=2)
CancelBT.grid(row=1, column=1)

if __name__ == "__main__":
    window.mainloop()
