male = [
" Erik ",
" Lars ",
" Karl ",
" Anders ",
" Johan "
]
female = [
" Maria ",
" Anna ",
" Margareta ",
" Elisabeth ",
" Eva "
]

del male[3] # del funktionen tar bort item vid index
del male[3]

del female[0]

femalelastindex = len(female) - 1

print(male[0], female[2], female[femalelastindex], male[2])