import PySimpleGUI as sg

sg.theme('DarkAmber')

layout = [ [sg.Text('ここは一行目')],
           [sg.Text('ここは2行目：適当に文字を入力してください'), sg.InputText()],
           [sg.Button('OK'), sg.Button('キャンセル')]]

window = sg.Window('サンプルプログラム', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'キャンセル':
        break
    elif event == 'OK':
        print('あなたが入力した値:', values[0])

window.close()