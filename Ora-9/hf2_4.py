felulet = 75
vodor = [15, 4300]
festek = felulet*2
if(felulet%vodor[0]!=0):
    vodrok = festek // vodor[0] + 1
else:
    vodrok = festek // vodor[0]

print(str(vodrok*vodor[1])+"ft értékben kell festéket vásárolnia.")

festo=[13, 2100]

ido = felulet*festo[0]/60
netto=ido*festo[1]
brutto=netto*1.27
print(str(netto) + "ft a nettó és "+str(brutto)+"ft a bruttó összeg.")
