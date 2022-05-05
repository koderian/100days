# 
from microbit import *
import radio

radio.on()
n = 0
b = 0
c = 0
Minecraft1 = Image("00000:" "00000:" "00900:" "00000:" "00000:")

Minecraft2 = Image("00000:" "00900:" "00900:" "00000:" "00000:")

Minecraft3 = Image("00000:" "00990:" "00900:" "00000:" "00000:")

Minecraft4 = Image("00000:" "00990:" "00990:" "00000:" "00000:")

Minecraft5 = Image("00000:" "00990:" "00990:" "00090:" "00000:")

Minecraft6 = Image("00000:" "00990:" "00990:" "00990:" "00000:")

Minecraft7 = Image("00000:" "00990:" "00990:" "09990:" "00000:")

Minecraft8 = Image("00000:" "00990:" "09990:" "09990:" "00000:")

Minecraft9 = Image("00000:" "09990:" "09990:" "09990:" "00000:")

Minecraft10 = Image("00000:" "09990:" "09990:" "09990:" "00000:")

Minecraft11 = Image("09000:" "09990:" "09990:" "09990:" "00000:")

Minecraft12 = Image("09900:" "09990:" "09990:" "09990:" "00000:")

Minecraft13 = Image("09990:" "09990:" "09990:" "09990:" "00000:")

Minecraft14 = Image("09999:" "09990:" "09990:" "09990:" "00000:")

Minecraft15 = Image("09999:" "09990:" "09990:" "09990:" "00000:")

Minecraft16 = Image("09999:" "09999:" "09990:" "09990:" "00000:")

Minecraft17 = Image("09999:" "09999:" "09999:" "09990:" "00000:")

Minecraft18 = Image("09999:" "09999:" "09999:" "09999:" "00000:")

Minecraft19 = Image("09999:" "09999:" "09999:" "09999:" "00009:")

Minecraft20 = Image("09999:" "09999:" "09999:" "09999:" "00099:")

Minecraft21 = Image("09999:" "09999:" "09999:" "09999:" "00999:")

Minecraft22 = Image("09999:" "09999:" "09999:" "09999:" "09999:")

Minecraft23 = Image("09999:" "09999:" "09999:" "09999:" "99999:")

Minecraft24 = Image("09999:" "09999:" "09999:" "99999:" "99999:")

Minecraft25 = Image("09999:" "09999:" "99999:" "99999:" "99999:")

Minecraft26 = Image("09999:" "99999:" "99999:" "99999:" "99999:")

Minecraft26 = Image("99999:" "99999:" "99999:" "99999:" "99999:")
list = [
    Minecraft1,
    Minecraft2,
    Minecraft3,
    Minecraft4,
    Minecraft5,
    Minecraft6,
    Minecraft7,
    Minecraft8,
    Minecraft9,
    Minecraft10,
    Minecraft11, 
    Minecraft12,
    Minecraft13,
    Minecraft14,
    Minecraft15,
    Minecraft16,
    Minecraft17,
    Minecraft18,
    Minecraft19,
    Minecraft20,
    Minecraft21,
    Minecraft22,
    Minecraft23,
    Minecraft24,
    Minecraft25,
    Minecraft26
]
while True:
    incoming = str(radio.receive())
    if incoming != "None":
        for r in list:
            display.show(r)
            sleep(200)
        display.clear()
    if button_a.is_pressed():
        radio.send("Pono")
    if incoming == "Traver":
        n += 1
        display.scroll("Traver")
    elif incoming == "Austin":
        display.scroll("Austin")
        b += 1
    elif incoming == "Oren":
        c += 1
        display.scroll("Oren")
    if n != 0 and b != 0 and c != 0:
        display.show(Image.SMILE)
        n = 0
        b = 0
        c = 0
