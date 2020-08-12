from tkinter import *
from EONetwork import *
fields = 'Source Island', 'Destination Island'

def fetch(entries):
    for entry in entries:
        field = entry[0]
        text  = entry[1].get()
        print('%s: "%s"' % (field, text))

def makeform(root, fields, islands):
    entries = []
    for field in fields:
        row = Frame(root)
        lab = Label(row, width=15, text=field, anchor='w')

        variable = StringVar(root)
        #variable.set(islands[0]) # default value
        w = OptionMenu(root, variable, *islands)

        row.pack(side=TOP, fill=X, padx=5, pady=5)
        lab.pack(side=LEFT)
        w.pack(side=RIGHT, expand=YES, fill=X)
        entries.append((field, w))
    return entries

if __name__ == '__main__':
    root = Tk()
    EOGraph = make_network('/home/malcyan/Documents/Logs/Emerald Ocean Network.xlsx')
    islands = sorted(EOGraph.nodes())
    ents = makeform(root, fields, islands)
    root.bind('<Return>', (lambda event, e=ents: fetch(e)))
    b1 = Button(root, text='Show', command=(lambda e=ents: fetch(e)))
    b1.pack(side=LEFT, padx=5, pady=5)
    b2 = Button(root, text='Quit', command=root.quit)
    b2.pack(side=LEFT, padx=5, pady=5)
    root.mainloop()
