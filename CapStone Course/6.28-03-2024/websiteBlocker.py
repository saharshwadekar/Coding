import tkinter as t

HOST: str = "./blocker.txt"
IPADDRESS: str = "127.0.0.1"


window = t.Tk()
window.geometry("650x400")
window.minsize(650, 400)
window.maxsize(650, 400)
window.title("Mine Blocker")

heading = t.Label(window, text="Website Blocker!", font="arial")
heading.pack()

label1 = t.Label(window, text="Enter Website :", font="arial 13 bold")
label1.place(x=5, y=60)
enterWebsite = t.Text(window, font="arial", height=2, width=40)
enterWebsite.place(x=140, y=60)


def blocker():
    websiteList = enterWebsite.get(1.0, t.END)
    website = list(websiteList.split(","))
    with open(HOST, "r+") as host:
        innerfile = host.read()
        for web in website:
            if web in innerfile:
                display = t.Label(window, text="Already Blocked", font="arial")
                display.place(x=200, y=200)
                pass
            else:
                host.write(IPADDRESS + " " + web + "\n")
                t.Label(window, text="Blocked", font="arial").place(x=230, y=200)


def unblock():
    websiteList = enterWebsite.get(1.0, t.END)
    website = list(websiteList.split(","))
    with open(HOST, "r+") as host_file:
        file = host_file.readlines()
    for web in website:
        if web in websiteList:
            with open(HOST, "r+") as f:
                for line in file:
                    if line.strip(",") != websiteList:
                        f.write(line)
                        t.Label(window, text="UnBlocked", font="arial").place(
                            x=350, y=200
                        )
                        pass
                    else:
                        display = t.Label(
                            window, text="Already UnBlocked", font="arial"
                        )
                        display.place(x=350, y=200)


block_button = t.Button(
    window,
    text="Block",
    font="arial",
    pady=5,
    command=blocker,
    width=6,
    bg="royal blue1",
    activebackground="grey",
)
block_button.place(x=230, y=150)
unblock_button = t.Button(
    window,
    text="UnBlock",
    font="arial",
    pady=5,
    command=unblock,
    width=6,
    bg="royal blue",
    activebackground="grey",
)
unblock_button.place(x=350, y=150)

window.mainloop()
