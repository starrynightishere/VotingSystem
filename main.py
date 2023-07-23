from tkinter import *

from tkinter import messagebox

import tkinter
from PIL import ImageTk, Image

root = Tk()

root.title("CVM for FUN")
c1votes = 0
c2votes = 0
c3votes = 0
c4votes = 0
c5votes = 0
c6votes = 0
nota_votes = 0


def candi1voted():
    tkinter.messagebox.showinfo("VVPAT", "You voted for Oggy and the Cockroaches")
    global c1votes
    c1votes = c1votes+1


def candi2voted():
    tkinter.messagebox.showinfo("VVPAT", "You voted for Pokemon")
    global c2votes
    c2votes = c2votes + 1


def candi3voted():
    tkinter.messagebox.showinfo("VVPAT", "You voted for Chhota Bheem")
    global c3votes
    c3votes = c3votes + 1


def candi4voted():
    tkinter.messagebox.showinfo("VVPAT", "You voted for Mr. Bean")
    global c4votes
    c4votes = c4votes + 1


def candi5voted():
    tkinter.messagebox.showinfo("VVPAT", "You voted for Doremon")
    global c5votes
    c5votes = c5votes + 1


def candi6voted():
    tkinter.messagebox.showinfo("VVPAT", "You voted for Ninja Hatthori")
    global c6votes
    c6votes = c6votes + 1


def notavoted():
    tkinter.messagebox.showinfo("VVPAT", "You voted for NOTA")
    global nota_votes
    nota_votes = nota_votes + 1


def progress():
    nwin = tkinter.Toplevel()
    nwin.title("Results")
    titlelabel = tkinter.Label(nwin, text="Candidate wise Voting Figures are: ").pack(padx=10)
    c1rlabel = tkinter.Label(nwin, text="Oggy and the Cockroaches has " + str(c1votes) + " votes").pack(pady=5)
    c2rlabel = tkinter.Label(nwin, text="Pokemon " + str(c2votes) + " votes").pack(pady=5)
    c3rlabel = tkinter.Label(nwin, text="Chhota Bheem has " + str(c3votes) + " votes").pack(pady=5)
    c4rlabel = tkinter.Label(nwin, text="Mr. Bean has " + str(c4votes) + " votes").pack(pady=5)
    c5rlabel = tkinter.Label(nwin, text="Doremon has " + str(c5votes) + " votes").pack(pady=5)
    c6rlabel = tkinter.Label(nwin, text="Ninja Hatthori has " + str(c6votes) + " votes").pack(pady=5)
    notalabel = tkinter.Label(nwin, text="NOTA has " + str(nota_votes) + " votes").pack(pady=5)
    conclbutton = tkinter.Button(nwin, text="Conclude Elections", command=lambda: conclude()).pack()

    def conclude():
        def c1win():
            return "Oggy and the Cockroaches"

        def c2win():
            return "Pokemon"

        def c3win():
            return "Chhota Bheem"

        def c4win():
            return "Mr. Bean"

        def c5win():
            return "Doremon"

        def c6win():
            return "Ninja Hatthori"

        def notawin():
            return "NOTA"

        def default():
            return "NOBODY"

        switcher = {
            c1votes: c1win,
            c2votes: c2win,
            c3votes: c3win,
            c4votes: c4win,
            c5votes: c5win,
            c6votes: c6win,
            nota_votes: notawin,
        }

        def switch(cnames):
            return switcher.get(cnames, default)()

        winner = max(c1votes, c2votes, c3votes, c4votes, c5votes, c6votes, nota_votes)
        tkinter.messagebox.showinfo("Winner", str(switch(winner).upper())+" IS THE WINNER!!!")
        reslabel = tkinter.Label(nwin, text="Election process has been concluded").pack(pady=5)


HideButton = tkinter.Button(root, text="It is for fun", command=progress)
HideButton.grid(row=0, column=1, columnspan=5)
Label1 = tkinter.Label(root, text="Best Cartoon Representative Elections").grid(row=1, column=2)
Candi1Image = ImageTk.PhotoImage(Image.open("images/c1.png"))
Candi2Image = ImageTk.PhotoImage(Image.open("images/c2.png"))
Candi3Image = ImageTk.PhotoImage(Image.open("images/c3.png"))
Candi4Image = ImageTk.PhotoImage(Image.open("images/c4.png"))
Candi5Image = ImageTk.PhotoImage(Image.open("images/c5.png"))
Candi6Image = ImageTk.PhotoImage(Image.open("images/c6.png"))
Candi1ImageLabel = tkinter.Label(root, image=Candi1Image).grid(row=2, column=1, pady=20, padx=20)
Candi2ImageLabel = tkinter.Label(root, image=Candi2Image).grid(row=2, column=2, padx=20)
Candi3ImageLabel = tkinter.Label(root, image=Candi3Image).grid(row=2, column=3, padx=20)
Candi4ImageLabel = tkinter.Label(root, image=Candi4Image).grid(row=5, column=1, pady=20)
Candi5ImageLabel = tkinter.Label(root, image=Candi5Image).grid(row=5, column=2)
Candi6ImageLabel = tkinter.Label(root, image=Candi6Image).grid(row=5, column=3)
Candi1Label = tkinter.Label(root, text="Oggy and the Cockroaches").grid(row=3, column=1)
Candi2Label = tkinter.Label(root, text="Pokemon").grid(row=3, column=2)
Candi3Label = tkinter.Label(root, text="Chhota Bheem").grid(row=3, column=3)
Candi4Label = tkinter.Label(root, text="Mr. Bean").grid(row=6, column=1)
Candi5Label = tkinter.Label(root, text="Doremon",).grid(row=6, column=2)
Candi6Label = tkinter.Label(root, text="Ninja Hatthori",).grid(row=6, column=3)
Candi1Button = tkinter.Button(root, text="Vote", command=candi1voted).grid(row=4, column=1, ipadx=30)
Candi2Button = tkinter.Button(root, text="Vote", command=candi2voted).grid(row=4, column=2, ipadx=30)
Candi3Button = tkinter.Button(root, text="Vote", command=candi3voted).grid(row=4, column=3, ipadx=30)
Candi4Button = tkinter.Button(root, text="Vote", command=candi4voted).grid(row=7, column=1, ipadx=30)
Candi5Button = tkinter.Button(root, text="Vote", command=candi5voted).grid(row=7, column=2, ipadx=30)
Candi6Button = tkinter.Button(root, text="Vote", command=candi6voted).grid(row=7, column=3, ipadx=30)
NOTAButton = tkinter.Button(root, text="Vote for NOTA", command=notavoted)
NOTAButton.grid(row=10, column=2, ipadx=30, pady=10)
root.mainloop()







