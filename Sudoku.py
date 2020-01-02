from tkinter import *
import time
import tkinter.messagebox as tmsg
root = Tk()

starttime = int(0)
g = []

def grid():
	for i in range(0,9):
		for j in range(0,9):
			print(g[i][j],end=" ")
		print("")

def check(para, r, c):
	for i in range(0,9):
		if i != c:
			if g[r][i]==para:
				return False
		if i != r:
			if g[i][c]==para:
				return False
	R,C = 0,0
	if r <= 2:
		R=0
	elif r <= 5:
		R=3
	elif r <= 8:
		R=6
	if c <= 2:
		C=0
	elif c <= 5:
		C=3
	elif c <= 8:
		C=6
	for i in range(R,R+3):
		for j in range(C,C+3):
			if i != r or j != c:
				if g[i][j]==para:
					return False
	return True

def enter():
	for i in range(0,9):
		g.append(list(map(int,input().split())))

def spacefinder():
	if time.time() - starttime > 4:
		return False
	for i in range(0,9):
		for j in range(0,9):
			if g[i][j] == 0:
				for k in range(1,10):
					if check(k,i,j):
						g[i][j]=k
						if not spacefinder():
							if k==9:
								g[i][j]=0
								return False
						else:
							return True
					elif k == 9:
						g[i][j]=0
						return False
			elif i==8 and j==8:
				return True

def solvable():
	for i in range(0,9):
		for j in range(0,9):
			if 0 < g[i][j] <= 9:
				if not check(g[i][j],i,j):
					return False
			elif g[i][j] == 0:
				pass
			else:
				return False
	return True

def setnewvar():
	aone.set(g[0][0])
	atwo.set(g[0][1])
	athree.set(g[0][2])
	bone.set(g[0][3])
	btwo.set(g[0][4])
	bthree.set(g[0][5])
	cone.set(g[0][6])
	ctwo.set(g[0][7])
	cthree.set(g[0][8])
	afour.set(g[1][0])
	afive.set(g[1][1])
	asix.set(g[1][2])
	bfour.set(g[1][3])
	bfive.set(g[1][4])
	bsix.set(g[1][5])
	cfour.set(g[1][6])
	cfive.set(g[1][7])
	csix.set(g[1][8])
	aseven.set(g[2][0])
	aeight.set(g[2][1])
	anine.set(g[2][2])
	bseven.set(g[2][3])
	beight.set(g[2][4])
	bnine.set(g[2][5])
	cseven.set(g[2][6])
	ceight.set(g[2][7])
	cnine.set(g[2][8])
	done.set(g[3][0])
	dtwo.set(g[3][1])
	dthree.set(g[3][2])
	eone.set(g[3][3])
	etwo.set(g[3][4])
	ethree.set(g[3][5])
	fone.set(g[3][6])
	ftwo.set(g[3][7])
	fthree.set(g[3][8])
	dfour.set(g[4][0])
	dfive.set(g[4][1])
	dsix.set(g[4][2])
	efour.set(g[4][3])
	efive.set(g[4][4])
	esix.set(g[4][5])
	ffour.set(g[4][6])
	ffive.set(g[4][7])
	fsix.set(g[4][8])
	dseven.set(g[5][0])
	deight.set(g[5][1])
	dnine.set(g[5][2])
	eseven.set(g[5][3])
	eeight.set(g[5][4])
	enine.set(g[5][5])
	fseven.set(g[5][6])
	feight.set(g[5][7])
	fnine.set(g[5][8])
	gone.set(g[6][0])
	gtwo.set(g[6][1])
	gthree.set(g[6][2])
	hone.set(g[6][3])
	htwo.set(g[6][4])
	hthree.set(g[6][5])
	ione.set(g[6][6])
	itwo.set(g[6][7])
	ithree.set(g[6][8])
	gfour.set(g[7][0])
	gfive.set(g[7][1])
	gsix.set(g[7][2])
	hfour.set(g[7][3])
	hfive.set(g[7][4])
	hsix.set(g[7][5])
	ifour.set(g[7][6])
	ifive.set(g[7][7])
	isix.set(g[7][8])
	gseven.set(g[8][0])
	geight.set(g[8][1])
	gnine.set(g[8][2])
	hseven.set(g[8][3])
	height.set(g[8][4])
	hnine.set(g[8][5])
	iseven.set(g[8][6])
	ieight.set(g[8][7])
	inine.set(g[8][8])

def fillAllEmpty():
	if aone.get() == '':
		aone.set(int(0))
	if atwo.get() == '':
		atwo.set(int(0))
	if athree.get() == '':
		athree.set(int(0))
	if bone.get() == '':
		bone.set(int(0))
	if btwo.get() == '':
		btwo.set(int(0))
	if bthree.get() == '':
		bthree.set(int(0))
	if cone.get() == '':
		cone.set(int(0))
	if ctwo.get() == '':
		ctwo.set(int(0))
	if cthree.get() == '':
		cthree.set(int(0))
	if afour.get() == '':
		afour.set(int(0))
	if afive.get() == '':
		afive.set(int(0))
	if asix.get() == '':
		asix.set(int(0))
	if bfour.get() == '':
		bfour.set(int(0))
	if bfive.get() == '':
		bfive.set(int(0))
	if bsix.get() == '':
		bsix.set(int(0))
	if cfour.get() == '':
		cfour.set(int(0))
	if cfive.get() == '':
		cfive.set(int(0))
	if csix.get() == '':
		csix.set(int(0))
	if aseven.get() == '':
		aseven.set(int(0))
	if aeight.get() == '':
		aeight.set(int(0))
	if anine.get() == '':
		anine.set(int(0))
	if bseven.get() == '':
		bseven.set(int(0))
	if beight.get() == '':
		beight.set(int(0))
	if bnine.get() == '':
		bnine.set(int(0))
	if cseven.get() == '':
		cseven.set(int(0))
	if ceight.get() == '':
		ceight.set(int(0))
	if cnine.get() == '':
		cnine.set(int(0))
	if done.get() == '':
		done.set(int(0))
	if dtwo.get() == '':
		dtwo.set(int(0))
	if dthree.get() == '':
		dthree.set(int(0))
	if eone.get() == '':
		eone.set(int(0))
	if etwo.get() == '':
		etwo.set(int(0))
	if ethree.get() == '':
		ethree.set(int(0))
	if fone.get() == '':
		fone.set(int(0))
	if ftwo.get() == '':
		ftwo.set(int(0))
	if fthree.get() == '':
		fthree.set(int(0))
	if dfour.get() == '':
		dfour.set(int(0))
	if dfive.get() == '':
		dfive.set(int(0))
	if dsix.get() == '':
		dsix.set(int(0))
	if efour.get() == '':
		efour.set(int(0))
	if efive.get() == '':
		efive.set(int(0))
	if esix.get() == '':
		esix.set(int(0))
	if ffour.get() == '':
		ffour.set(int(0))
	if ffive.get() == '':
		ffive.set(int(0))
	if fsix.get() == '':
		fsix.set(int(0))
	if dseven.get() == '':
		dseven.set(int(0))
	if deight.get() == '':
		deight.set(int(0))
	if dnine.get() == '':
		dnine.set(int(0))
	if eseven.get() == '':
		eseven.set(int(0))
	if eeight.get() == '':
		eeight.set(int(0))
	if enine.get() == '':
		enine.set(int(0))
	if fseven.get() == '':
		fseven.set(int(0))
	if feight.get() == '':
		feight.set(int(0))
	if fnine.get() == '':
		fnine.set(int(0))
	if gone.get() == '':
		gone.set(int(0))
	if gtwo.get() == '':
		gtwo.set(int(0))
	if gthree.get() == '':
		gthree.set(int(0))
	if hone.get() == '':
		hone.set(int(0))
	if htwo.get() == '':
		htwo.set(int(0))
	if hthree.get() == '':
		hthree.set(int(0))
	if ione.get() == '':
		ione.set(int(0))
	if itwo.get() == '':
		itwo.set(int(0))
	if ithree.get() == '':
		ithree.set(int(0))
	if gfour.get() == '':
		gfour.set(int(0))
	if gfive.get() == '':
		gfive.set(int(0))
	if gsix.get() == '':
		gsix.set(int(0))
	if hfour.get() == '':
		hfour.set(int(0))
	if hfive.get() == '':
		hfive.set(int(0))
	if hsix.get() == '':
		hsix.set(int(0))
	if ifour.get() == '':
		ifour.set(int(0))
	if ifive.get() == '':
		ifive.set(int(0))
	if isix.get() == '':
		isix.set(int(0))
	if gseven.get() == '':
		gseven.set(int(0))
	if geight.get() == '':
		geight.set(int(0))
	if gnine.get() == '':
		gnine.set(int(0))
	if hseven.get() == '':
		hseven.set(int(0))
	if height.get() == '':
		height.set(int(0))
	if hnine.get() == '':
		hnine.set(int(0))
	if iseven.get() == '':
		iseven.set(int(0))
	if ieight.get() == '':
		ieight.set(int(0))
	if inine.get() == '':
		inine.set(int(0))

def clearAllInputs():
	aone.set('')
	atwo.set('')
	athree.set('')
	bone.set('')
	btwo.set('')
	bthree.set('')
	cone.set('')
	ctwo.set('')
	cthree.set('')
	afour.set('')
	afive.set('')
	asix.set('')
	bfour.set('')
	bfive.set('')
	bsix.set('')
	cfour.set('')
	cfive.set('')
	csix.set('')
	aseven.set('')
	aeight.set('')
	anine.set('')
	bseven.set('')
	beight.set('')
	bnine.set('')
	cseven.set('')
	ceight.set('')
	cnine.set('')
	done.set('')
	dtwo.set('')
	dthree.set('')
	eone.set('')
	etwo.set('')
	ethree.set('')
	fone.set('')
	ftwo.set('')
	fthree.set('')
	dfour.set('')
	dfive.set('')
	dsix.set('')
	efour.set('')
	efive.set('')
	esix.set('')
	ffour.set('')
	ffive.set('')
	fsix.set('')
	dseven.set('')
	deight.set('')
	dnine.set('')
	eseven.set('')
	eeight.set('')
	enine.set('')
	fseven.set('')
	feight.set('')
	fnine.set('')
	gone.set('')
	gtwo.set('')
	gthree.set('')
	hone.set('')
	htwo.set('')
	hthree.set('')
	ione.set('')
	itwo.set('')
	ithree.set('')
	gfour.set('')
	gfive.set('')
	gsix.set('')
	hfour.set('')
	hfive.set('')
	hsix.set('')
	ifour.set('')
	ifive.set('')
	isix.set('')
	gseven.set('')
	geight.set('')
	gnine.set('')
	hseven.set('')
	height.set('')
	hnine.set('')
	iseven.set('')
	ieight.set('')
	inine.set('')

def appendInXAndCheckIfInputsAreOkay():
	x = []
	x.append([(aone.get()), (atwo.get()), (athree.get()), (bone.get()), (btwo.get()), (bthree.get()), (cone.get()), (ctwo.get()), (cthree.get())])
	x.append([(afour.get()), (afive.get()), (asix.get()), (bfour.get()), (bfive.get()), (bsix.get()), (cfour.get()), (cfive.get()), (csix.get())])
	x.append([(aseven.get()), (aeight.get()), (anine.get()), (bseven.get()), (beight.get()), (bnine.get()),(cseven.get()), (ceight.get()), (cnine.get())])
	x.append([(done.get()), (dtwo.get()), (dthree.get()), (eone.get()), (etwo.get()), (ethree.get()), (fone.get()), (ftwo.get()), (fthree.get())])
	x.append([(dfour.get()), (dfive.get()), (dsix.get()), (efour.get()), (efive.get()), (esix.get()), (ffour.get()), (ffive.get()), (fsix.get())])
	x.append([(dseven.get()), (deight.get()), (dnine.get()), (eseven.get()), (eeight.get()), (enine.get()), (fseven.get()), (feight.get()), (fnine.get())])
	x.append([(gone.get()), (gtwo.get()), (gthree.get()), (hone.get()), (htwo.get()), (hthree.get()), (ione.get()), (itwo.get()), (ithree.get())])
	x.append([(gfour.get()), (gfive.get()), (gsix.get()), (hfour.get()), (hfive.get()), (hsix.get()), (ifour.get()), (ifive.get()), (isix.get())])
	x.append([(gseven.get()), (geight.get()), (gnine.get()), (hseven.get()), (height.get()), (hnine.get()), (iseven.get()), (ieight.get()), (inine.get())])
	for i in range(0,9):
		for j in range(0,9):
			if not x[i][j].isdigit():
				return False
			else:
				if 0 < int(x[i][j]) > 9:
					return False
	return True

def quitcheck():
	val = tmsg.askyesno("Confirmation","Are you sure you want to quit?")
	if val == True:
		sys.exit()

def solve():
	global starttime
	g.clear()
	fillAllEmpty()
	print(g)
	if appendInXAndCheckIfInputsAreOkay():
		g.append([int(aone.get()), int(atwo.get()), int(athree.get()), int(bone.get()), int(btwo.get()), int(bthree.get()), int(cone.get()), int(ctwo.get()),int(cthree.get())])
		g.append([int(afour.get()), int(afive.get()), int(asix.get()), int(bfour.get()), int(bfive.get()), int(bsix.get()), int(cfour.get()), int(cfive.get()), int(csix.get())])
		g.append([int(aseven.get()), int(aeight.get()), int(anine.get()), int(bseven.get()), int(beight.get()), int(bnine.get()), int(cseven.get()), int(ceight.get()), int(cnine.get())])
		g.append([int(done.get()), int(dtwo.get()), int(dthree.get()), int(eone.get()), int(etwo.get()), int(ethree.get()), int(fone.get()), int(ftwo.get()),int(fthree.get())])
		g.append([int(dfour.get()), int(dfive.get()), int(dsix.get()), int(efour.get()), int(efive.get()), int(esix.get()), int(ffour.get()), int(ffive.get()), int(fsix.get())])
		g.append([int(dseven.get()), int(deight.get()), int(dnine.get()), int(eseven.get()), int(eeight.get()), int(enine.get()), int(fseven.get()), int(feight.get()), int(fnine.get())])
		g.append([int(gone.get()), int(gtwo.get()), int(gthree.get()), int(hone.get()), int(htwo.get()), int(hthree.get()), int(ione.get()), int(itwo.get()),int(ithree.get())])
		g.append([int(gfour.get()), int(gfive.get()), int(gsix.get()), int(hfour.get()), int(hfive.get()), int(hsix.get()), int(ifour.get()), int(ifive.get()), int(isix.get())])
		g.append([int(gseven.get()), int(geight.get()), int(gnine.get()), int(hseven.get()), int(height.get()), int(hnine.get()), int(iseven.get()), int(ieight.get()), int(inine.get())])
		starttime = time.time()
		if spacefinder():
			grid()
			setnewvar()
			tmsg.showinfo("Yippee!!","Sudoku Solved Successfully")
		else:
			clearAllInputs()
			tmsg.showerror("Error", "This Sudoku is not Solvable")
	else:
		print("Illegal Input")
		clearAllInputs()
		tmsg.showerror("Error", "Illegal Input")

root.geometry("444x333")
root.minsize(444,333)
root.maxsize(444,333)
root.title("Sudoku Solved - V 1.0")


Label(text = "---------------", bg = "light blue", font = "timesnewroman 15 bold").grid(row = 0, column = 4)
Label(text = "---------------", bg = "light green", font = "timesnewroman 15 bold").grid(row = 0, column = 0)
Label(text = "---------------", bg = "light green", font = "timesnewroman 15 bold").grid(row = 4, column = 4)
Label(text = "---------------", bg = "light blue", font = "timesnewroman 15 bold").grid(row = 4, column = 0)

heading = Label(text = "Sudoku Solver", font = "courier 20 bold", bg = "yellow", relief = FLAT)
heading.grid(row  = 0, column = 1, columnspan = 3)

# Frame(root,width = 160,height = 100).grid(row = 0)
# Frame(root).grid(ro)
aone =  StringVar()
atwo =  StringVar()
athree =  StringVar()
afour =  StringVar()
afive =  StringVar()
asix =  StringVar()
aseven =  StringVar()
aeight =  StringVar()
anine =  StringVar()

bone =  StringVar()
btwo =  StringVar()
bthree =  StringVar()
bfour =  StringVar()
bfive =  StringVar()
bsix =  StringVar()
bseven =  StringVar()
beight =  StringVar()
bnine =  StringVar()

cone =  StringVar()
ctwo =  StringVar()
cthree =  StringVar()
cfour =  StringVar()
cfive =  StringVar()
csix =  StringVar()
cseven =  StringVar()
ceight =  StringVar()
cnine =  StringVar()

done =  StringVar()
dtwo =  StringVar()
dthree =  StringVar()
dfour =  StringVar()
dfive =  StringVar()
dsix =  StringVar()
dseven =  StringVar()
deight =  StringVar()
dnine =  StringVar()

eone =  StringVar()
etwo =  StringVar()
ethree =  StringVar()
efour =  StringVar()
efive =  StringVar()
esix =  StringVar()
eseven =  StringVar()
eeight =  StringVar()
enine =  StringVar()

fone =  StringVar()
ftwo =  StringVar()
fthree =  StringVar()
ffour =  StringVar()
ffive =  StringVar()
fsix =  StringVar()
fseven =  StringVar()
feight =  StringVar()
fnine =  StringVar()

gone =  StringVar()
gtwo =  StringVar()
gthree =  StringVar()
gfour =  StringVar()
gfive =  StringVar()
gsix =  StringVar()
gseven =  StringVar()
geight =  StringVar()
gnine =  StringVar()

hone =  StringVar()
htwo =  StringVar()
hthree =  StringVar()
hfour =  StringVar()
hfive =  StringVar()
hsix =  StringVar()
hseven =  StringVar()
height =  StringVar()
hnine =  StringVar()

ione =  StringVar()
itwo =  StringVar()
ithree =  StringVar()
ifour =  StringVar()
ifive =  StringVar()
isix =  StringVar()
iseven =  StringVar()
ieight =  StringVar()
inine =  StringVar()

f1 = Frame(root, bg = "orange", borderwidth = 4)
f1.grid(row = 1, column = 1)
Entry(f1, width = 3, textvariable = aone).grid(row = 0, column = 0)
Entry(f1, width = 3, textvariable = atwo).grid(row = 0, column = 1)
Entry(f1, width = 3, textvariable = athree).grid(row = 0, column = 2)
Entry(f1, width = 3, textvariable = afour).grid(row = 1, column = 0)
Entry(f1, width = 3, textvariable = afive).grid(row = 1, column = 1)
Entry(f1, width = 3, textvariable = asix).grid(row = 1, column = 2)
Entry(f1, width = 3, textvariable = aseven).grid(row = 2, column = 0)
Entry(f1, width = 3, textvariable = aeight).grid(row = 2, column = 1)
Entry(f1, width = 3, textvariable = anine).grid(row = 2, column = 2)
# print(g)

f2 = Frame(root, bg = "orange", borderwidth = 4)
f2.grid(row = 1, column = 2)
Entry(f2, width = 3, textvariable = bone).grid(row = 0, column = 0)
Entry(f2, width = 3, textvariable = btwo).grid(row = 0, column = 1)
Entry(f2, width = 3, textvariable = bthree).grid(row = 0, column = 2)
Entry(f2, width = 3, textvariable = bfour).grid(row = 1, column = 0)
Entry(f2, width = 3, textvariable = bfive).grid(row = 1, column = 1)
Entry(f2, width = 3, textvariable = bsix).grid(row = 1, column = 2)
Entry(f2, width = 3, textvariable = bseven).grid(row = 2, column = 0)
Entry(f2, width = 3, textvariable = beight).grid(row = 2, column = 1)
Entry(f2, width = 3, textvariable = bnine).grid(row = 2, column = 2)
# print(g)

f3 = Frame(root, bg = "orange", borderwidth = 4)
f3.grid(row = 1, column = 3)
Entry(f3, width = 3, textvariable = cone).grid(row = 0, column = 0)
Entry(f3, width = 3, textvariable = ctwo).grid(row = 0, column = 1)
Entry(f3, width = 3, textvariable = cthree).grid(row = 0, column = 2)
Entry(f3, width = 3, textvariable = cfour).grid(row = 1, column = 0)
Entry(f3, width = 3, textvariable = cfive).grid(row = 1, column = 1)
Entry(f3, width = 3, textvariable = csix).grid(row = 1, column = 2)
Entry(f3, width = 3, textvariable = cseven).grid(row = 2, column = 0)
Entry(f3, width = 3, textvariable = ceight).grid(row = 2, column = 1)
Entry(f3, width = 3, textvariable = cnine).grid(row = 2, column = 2)
# print(g)

f4 = Frame(root, bg = "orange", borderwidth = 4)
f4.grid(row = 2, column = 1)
Entry(f4, width = 3, textvariable = done).grid(row = 0, column = 0)
Entry(f4, width = 3, textvariable = dtwo).grid(row = 0, column = 1)
Entry(f4, width = 3, textvariable = dthree).grid(row = 0, column = 2)
Entry(f4, width = 3, textvariable = dfour).grid(row = 1, column = 0)
Entry(f4, width = 3, textvariable = dfive).grid(row = 1, column = 1)
Entry(f4, width = 3, textvariable = dsix).grid(row = 1, column = 2)
Entry(f4, width = 3, textvariable = dseven).grid(row = 2, column = 0)
Entry(f4, width = 3, textvariable = deight).grid(row = 2, column = 1)
Entry(f4, width = 3, textvariable = dnine).grid(row = 2, column = 2)
# print(g)

f5 = Frame(root, bg = "orange", borderwidth = 4)
f5.grid(row = 2, column = 2)
Entry(f5, width = 3, textvariable = eone).grid(row = 0, column = 0)
Entry(f5, width = 3, textvariable = etwo).grid(row = 0, column = 1)
Entry(f5, width = 3, textvariable = ethree).grid(row = 0, column = 2)
Entry(f5, width = 3, textvariable = efour).grid(row = 1, column = 0)
Entry(f5, width = 3, textvariable = efive).grid(row = 1, column = 1)
Entry(f5, width = 3, textvariable = esix).grid(row = 1, column = 2)
Entry(f5, width = 3, textvariable = eseven).grid(row = 2, column = 0)
Entry(f5, width = 3, textvariable = eeight).grid(row = 2, column = 1)
Entry(f5, width = 3, textvariable = enine).grid(row = 2, column = 2)
# print(g)

f6 = Frame(root, bg = "orange", borderwidth = 4)
f6.grid(row = 2, column = 3)
Entry(f6, width = 3, textvariable = fone).grid(row = 0, column = 0)
Entry(f6, width = 3, textvariable = ftwo).grid(row = 0, column = 1)
Entry(f6, width = 3, textvariable = fthree).grid(row = 0, column = 2)
Entry(f6, width = 3, textvariable = ffour).grid(row = 1, column = 0)
Entry(f6, width = 3, textvariable = ffive).grid(row = 1, column = 1)
Entry(f6, width = 3, textvariable = fsix).grid(row = 1, column = 2)
Entry(f6, width = 3, textvariable = fseven).grid(row = 2, column = 0)
Entry(f6, width = 3, textvariable = feight).grid(row = 2, column = 1)
Entry(f6, width = 3, textvariable = fnine).grid(row = 2, column = 2)
# print(g)

f7 = Frame(root, bg = "orange", borderwidth = 4)
f7.grid(row = 3, column = 1)
Entry(f7, width = 3, textvariable = gone).grid(row = 0, column = 0)
Entry(f7, width = 3, textvariable = gtwo).grid(row = 0, column = 1)
Entry(f7, width = 3, textvariable = gthree).grid(row = 0, column = 2)
Entry(f7, width = 3, textvariable = gfour).grid(row = 1, column = 0)
Entry(f7, width = 3, textvariable = gfive).grid(row = 1, column = 1)
Entry(f7, width = 3, textvariable = gsix).grid(row = 1, column = 2)
Entry(f7, width = 3, textvariable = gseven).grid(row = 2, column = 0)
Entry(f7, width = 3, textvariable = geight).grid(row = 2, column = 1)
Entry(f7, width = 3, textvariable = gnine).grid(row = 2, column = 2)
# print(g)

f8 = Frame(root, bg = "orange", borderwidth = 4)
f8.grid(row = 3, column = 2)
Entry(f8, width = 3, textvariable = hone).grid(row = 0, column = 0)
Entry(f8, width = 3, textvariable = htwo).grid(row = 0, column = 1)
Entry(f8, width = 3, textvariable = hthree).grid(row = 0, column = 2)
Entry(f8, width = 3, textvariable = hfour).grid(row = 1, column = 0)
Entry(f8, width = 3, textvariable = hfive).grid(row = 1, column = 1)
Entry(f8, width = 3, textvariable = hsix).grid(row = 1, column = 2)
Entry(f8, width = 3, textvariable = hseven).grid(row = 2, column = 0)
Entry(f8, width = 3, textvariable = height).grid(row = 2, column = 1)
Entry(f8, width = 3, textvariable = hnine).grid(row = 2, column = 2)
# print(g)

f9 = Frame(root, bg = "orange", borderwidth = 4)
f9.grid(row = 3, column = 3)
Entry(f9, width = 3, textvariable = ione).grid(row = 0, column = 0)
Entry(f9, width = 3, textvariable = itwo).grid(row = 0, column = 1)
Entry(f9, width = 3, textvariable = ithree).grid(row = 0, column = 2)
Entry(f9, width = 3, textvariable = ifour).grid(row = 1, column = 0)
Entry(f9, width = 3, textvariable = ifive).grid(row = 1, column = 1)
Entry(f9, width = 3, textvariable = isix).grid(row = 1, column = 2)
Entry(f9, width = 3, textvariable = iseven).grid(row = 2, column = 0)
Entry(f9, width = 3, textvariable = ieight).grid(row = 2, column = 1)
Entry(f9, width = 3, textvariable = inine).grid(row = 2, column = 2)
# print(g)

b1 = Button(text = "SOLVE", command = solve)
b1.grid(row = 5, column = 2)
b2 = Button(text = "CLOSE", command = quitcheck)
b2.grid(row = 5, column = 3)
b3 = Button(text = "CLEAR ALL", command = clearAllInputs)
b3.grid(row = 5, column = 1)

mainmenu = Menu(root)
file = Menu(mainmenu, tearoff = 0)
file.add_command(label = "Solve", command = solve)
file.add_separator()
file.add_command(label = "Exit", command = quitcheck)
mainmenu.add_cascade(label = "File", menu = file)
edit = Menu(mainmenu, tearoff = 0)
edit.add_command(label = "Clear All", command = clearAllInputs)
mainmenu.add_cascade(label = "Edit", menu = edit)
root.config(menu = mainmenu)

root.mainloop()