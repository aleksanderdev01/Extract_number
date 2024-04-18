#Tekst zawierający liczbę Pi
text = "Pi-Number:  3.1415"
#Szuka wartości po danym symbolu
sp = text.find(':')
#Dociera do wartości
p = text[sp+1:]
#Wczytuje wartość jako liczbę zmiennoprzecinkową
end = float(p)
#drukuje liczbę
print(end)