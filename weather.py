# =================================================
#           ライブラリインポート
# =================================================
import PySimpleGUI as gui
import requests as req
from modules.area import Area

# 地域コード取得モジュール読み込み
arean = Area()

# 値を受け取って、画面を更新する関数
def whether(which):
    # 鹿児島と北海道だけなぜか、コードが取れない。。。
    if(which[0:2] == "46"):
        which = "460100"
    if(which[0:2] == "47"):
        which = "471000"
    # APIを投げるURLを指定
    url = 'https://www.jma.go.jp/bosai/forecast/data/forecast/' + which + '.json'
    # APIを投げる
    response = req.get(url)
    # 今からの天気を取得する
    try:
        weathers = response.json()[0]["timeSeries"][0]["areas"][0]["weathers"]
    except:
        weathers = response.json()[0]["srf"]["timeSeries"][0]["areas"]["weathers"]
    # 画面を更新する
    window['now'].update("今からの天気："+weathers[0])

# =================================================
#           ウィンドウレイアウト
# =================================================
layout = [
   # 最初に表示するもの
   [gui.Text('どこの天気が知りたいですか？')],
   # ここにキーを持たせることで、ボタンを押したときに値を取得できる
   [gui.InputText("",key='input1')],
   # ボタンのイベントを取得するために、キーを設定
   [gui.Submit(button_text='OK',key='button1')],
   # 今からの天気の値を「更新」する
   [gui.Text('今からの天気：',key='now')]
]

# =================================================
#           ウィンドウ処理
# =================================================
# ウィンドウオブジェクトの作成
window = gui.Window('PySimpleGUI', layout, size=(400, 200))

# イベントのループ
while True:
    # イベントの読み込み
    event, values = window.read()
    # ウィンドウの×ボタンが押されれば終了
    if event == gui.WIN_CLOSED:
       break
    # ボタンが押されたら処理を行う
    if event == "button1":
        # 実行させたい処理
        input1 = values['input1']
        # お天気を取得する
        value = arean.search(input1)
        # 画面上の天気の値を更新する
        whether(value)

# ウィンドウ終了処理
window.close()

