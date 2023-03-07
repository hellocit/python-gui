import PySimpleGUI as sg
import os
import pandas as pd
import tabula

def readTableFromPDF(filePath, isLattice, targetPages):
    '''
    指定されたfilePathのPDFファイルから表を読み込みDataFramleに変換する
    '''
    dfs = tabula.read_pdf(filePath, lattice=isLattice, pages=targetPages)

    # 変換したDataFrameを表示
    for index, df in enumerate(dfs):
        print("----------表"+str(index+1)+"----------")
        print(df.head())

    return dfs

# ステップ2. デザインテーマの設定
sg.theme('DarkTeal7')

# ステップ3. ウィンドウの部品とレイアウト
layout = [
    [sg.Text('読み取り対象のファイルとページを指定してください')],
    [sg.Text('ファイル', size=(10, 1)), sg.Input(), sg.FileBrowse('ファイルを選択', key='inputFilePath')],
    [sg.Text('ページ', size=(10, 1)), sg.InputText('', size=(10, 1), key='pages'), sg.Text('複数ページのときは\n3-10 のように指定してください', size=(30, 2))],
    [sg.Text('表の罫線', size=(10, 1)),sg.Combo(('あり', 'なし'), default_value="あり",size=(10, 1), key='lattice')],
    [sg.Button('読み取り', key='read'), sg.Button('csvに保存', key='save')],
    [sg.Output(size=(80,20))]
]