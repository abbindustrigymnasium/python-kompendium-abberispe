registrerade =[" Anna ", " Eva ", " Erik ", " Lars ", " Karl "]
avanmälningar =[" Anna ", " Erik ", " Karl "]

for name in avanmälningar: # tittar på alla items i avanmälningar
    if name in registrerade: # tittar om namnet finns i registrerade
        registrerade.remove(name) # tar bort namnet från registrerade

print(registrerade)