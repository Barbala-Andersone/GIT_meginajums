import PySimpleGUI as sg
import matplotlib as plt

#izveidojam logam elementus un iegulšanas zonu (atrašanās vietu) 

dalas= [
    #vārdnīca = datu kopa, kur var iekļūt tikai ar atslēgvārdu
    [sg.Text("Ievadiet grafika nosaukumu: ", sg.InputText(key="-TITLE-"))]

    #atslēga ir tas pats, ka JavaScriptā ID

    [sg.Canvas(key="-CANVAS-")]
    [sg.Button("Izveidot grafiku"), sg.Button("Iziet")]
]

logs=sg.Window("Grafikas izveide", dalas, finalize=True)

# Galvenais izpildes cikls (lai logs rādītos visu laiku, nevis tikai uz īsu mirkli)
while True:
    notikums, vertiba=logs.read()

    if notikums==sg.WINDOW_CLOSED or notikums=="Iziet":
        break



logs.Close()