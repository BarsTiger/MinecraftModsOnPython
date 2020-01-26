toDoFile = open("toDoFile.txt", "w", encoding="utf-8")

mnogoZapominaushihKotikov = ""

odinKotik = input("Введите описание дела(vot tak), котики его запомнят:   ")

while odinKotik != "zxc":
    mnogoZapominaushihKotikov = mnogoZapominaushihKotikov + odinKotik + "\n"
    odinKotik = input("Введите описание дела(vot tak)(или zxc для выхода)(после поставьте пробел и нажмите ENTER), котики его запомнят:   ")

toDoFile.write(mnogoZapominaushihKotikov)
toDoFile.close(),


