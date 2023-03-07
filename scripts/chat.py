import os
import pandas as pd
import PySimpleGUI as sg
import tabula

def readTableFromPDF(filePath, isLattice, targetPages):
    '''
    指定されたfilePathのPDFファイルから表を読み込みDataFrameに変換する
    '''
    # ファイルが存在するか確認する
    if not os.path.exists(filePath):
        print(f"ファイルが存在しません: {filePath}")
        return []

    # ページ数を取得する
    try:
        pages = list(map(int, targetPages.split(",")))
    except ValueError:
        print(f"ページ番号が不正です: {targetPages}")
        return []

    # PDFファイルから表を読み込む
    dfs = tabula.read_pdf(filePath, lattice=isLattice, pages=pages, multiple_tables=True)

    # 変換したDataFrameを表示
    for index, df in enumerate(dfs):
        print(f"----------表{index+1}----------")
        print(df.head())

    return dfs

sg.theme('DarkTeal7')

layout = [
    [sg.Text('読み取り対象のファイルとページを指定してください')],
    [sg.Text('ファイル', size=(10, 1)),sg.Input(), sg.FileBrowse('ファイルを選択
