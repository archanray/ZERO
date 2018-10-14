from Tkinter import *

user_filename = ''

user_fields = ['House number', 'House address', 'Country', 'State', 'City', 'PIN']
text_box11 = text_box12 = text_box13 = text_box14 = text_box15 = text_box16 = None
row11 = row12 = row13 = row14 = row15 = row16 = None
lab11 = lab12 = lab13 = lab14 = lab15 = lab16 = None
device_fields = ['Name', 'Day', 'Time slots', 'Duration', 'Interruptable']
text_box21 = text_box22 = text_box23 = text_box24 = text_box25 = None


modeint = None

def fetch(entries):
	if modeint.get() == 1:
		for i in range(0,6):
			print entries[i][1].get()
			if entries[i][1].get() == '':
				print 'Can\'t have a blank field'
				return
			if i == 0:
				user_filename += entries[i][1].get()
			elif i == 5:
				user_filename += entries[i][1].get()
			else:
				user_filename += entries[i][1].get()[0:2]
		print user_filename+'.npy'

	if modeint.get() == 2:
		pass

	if modeint.get() == 3:
		pass

	return
'''
def fetch(entries):
	global device_list
	filename = ''
	for entry in entries:
		user_info[entry[0]] = entry[1].get() 
		if entry[0] == 'House number':
			filename += entry[1].get()
		elif entry[0] == 'PIN':
			filename += entry[1].get()
		else:
			filename += entry[1].get()[0:2]
	filename = filename+'.npy'
	#device_list = np.load(filename)
	return filename
'''

def makeform(root, fields):
	entries = []
	for field in fields:
		row = Frame(root)
		lab = Label(row, width=15, text=field, anchor='w')
		ent = Entry(row)
		row.pack(side=TOP, fill=X, padx=5, pady=5)
		lab.pack(side=LEFT)
		ent.pack(side=RIGHT, expand=YES, fill=X)
		entries.append((field, ent))
	return entries

def enter_user_data():
	global user_fields
	row11 = Frame(root)
	text_box11 = Entry(row11)
	row11.pack(side=TOP, fill=X, padx=5, pady=5)
	text_box11.pack(side = RIGHT, expand=YES, fill=X)
	lab11 = Label(row11, width=15, text=user_fields[0], anchor='w')
	lab11.pack(side=LEFT)

	row12 = Frame(root)
	text_box12 = Entry(row12)
	row12.pack(side=TOP, fill=X, padx=5, pady=5)
	text_box12.pack(side = RIGHT, expand=YES, fill=X)
	lab12 = Label(row12, width=15, text=user_fields[1], anchor='w')
	lab12.pack(side=LEFT)

	row13 = Frame(root)
	text_box13 = Entry(row13)
	row13.pack(side=TOP, fill=X, padx=5, pady=5)
	text_box13.pack(side = RIGHT, expand=YES, fill=X)
	lab13 = Label(row13, width=15, text=user_fields[2], anchor='w')
	lab13.pack(side=LEFT)

	row14 = Frame(root)
	text_box14 = Entry(row14)
	row14.pack(side=TOP, fill=X, padx=5, pady=5)
	text_box14.pack(side = RIGHT, expand=YES, fill=X)
	lab14 = Label(row14, width=15, text=user_fields[3], anchor='w')
	lab14.pack(side=LEFT)

	row15 = Frame(root)
	text_box15 = Entry(row15)
	row15.pack(side=TOP, fill=X, padx=5, pady=5)
	text_box15.pack(side = RIGHT, expand=YES, fill=X)
	lab15 = Label(row15, width=15, text=user_fields[4], anchor='w')
	lab15.pack(side=LEFT)

	row16 = Frame(root)
	text_box16 = Entry(row16)
	row16.pack(side=TOP, fill=X, padx=5, pady=5)
	text_box16.pack(side = RIGHT, expand=YES, fill=X)
	lab16 = Label(row16, width=15, text=user_fields[5], anchor='w')
	lab16.pack(side=LEFT)

	ent = [row11, row12, row13, row14, row15, row16]
	b3 = Button(root, text='Enter info',
		  command=(lambda e=ent: fetch(e)))
	b3.pack()
	pass

def enter_appl_data():

	# build new boxes
	text_box21 = Entry(root)
	text_box21.pack()
	text_box22 = Entry(root)
	text_box22.pack()
	text_box23 = Entry(root)
	text_box23.pack()
	text_box24 = Entry(root)
	text_box24.pack()
	text_box25 = Entry(root)
	text_box25.pack()
	pass

def edit_appl_data():
	text_box21 = Entry(root)
	text_box21.pack()
	text_box22 = Entry(root)
	text_box22.pack()
	text_box23 = Entry(root)
	text_box23.pack()
	text_box24 = Entry(root)
	text_box24.pack()
	text_box25 = Entry(root)
	text_box25.pack()
	pass

if __name__ == '__main__':
	
	root = Tk()
	'''
	ents = makeform(root, fields)
	#root.bind('<Return>', (lambda event, e=ents: fetch(e)))   
	b1 = Button(root, text='Enter info',
		  command=(lambda e=ents: fetch(e)))
	b1.pack(side=LEFT, padx=5, pady=5)
	b2 = Button(root, text='Quit', command=root.quit)
	b2.pack(side=LEFT, padx=5, pady=5)

	ents2 = makeform(root, device_fields)
	b3 = Button(root, text='Enter info',
		  command=(lambda e=ents: fetch(e)))
	b3.pack(side=LEFT, padx=5, pady=5)
	b4 = Button(root, text='Quit', command=root.quit)
	b4.pack(side=LEFT, padx=5, pady=5)

	root.mainloop()
	'''
	# radio button
	modeint = IntVar()
	modeint.set(1)

	Radiobutton(root, text="Enter user data", variable=modeint, value=1,
		command=enter_user_data).pack(anchor=N)
	Radiobutton(root, text="Enter appliance data", variable=modeint, value=2,
		command=enter_appl_data).pack(anchor=N)
	Radiobutton(root, text="Update appliance data", variable=modeint, value=3,
		command=edit_appl_data).pack(anchor=N)

	frame = Frame(root, relief=SUNKEN)
	b1 = frame.button1 = Button(root, text='Quit', command=root.quit)
	b1.pack(padx=5, pady=5)
	frame.pack(fill=BOTH,expand=1)
	root.mainloop()