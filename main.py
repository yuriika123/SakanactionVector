import arrr
from pyscript import document
import math

import csv
with open("SakanactionVectorCSV.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    song_data = list(reader)
            
def button(event):
    input_text = document.querySelector("#search")
    search_song = input_text.value
    
    search_song_data = []

    for row in song_data:
        if (row[0] == search_song): # リストからsearch_songの行を取得
            print("リストから項目が見つかりました")
            search_song_data = row
            break

    if search_song_data:
        print(search_song_data)
    else:
        print("リストから曲が見つかりませんでした")
    

    # テンポをノーマライズ
    tempo_list = []
    for i in range(1, 103):
        tempo_list.append(float(song_data[i][4]))
    print(tempo_list)
    max_tempo = max(tempo_list)
    min_tempo = min(tempo_list)
    normalized_tempo_list = []
    for i in range(102):
        normalized_tempo_list.append((tempo_list[i] - min_tempo) / (max_tempo - min_tempo)*10)
    print(normalized_tempo_list)


    distanceTempo = []
    for i in range(1, 103):
        distanceTempo.append((float(search_song_data[4]) - min_tempo) / (max_tempo - min_tempo) * 10 - normalized_tempo_list[i-1])
    print("ノーマライズしたテンポの差")
    print(distanceTempo)

    distanceBright = []
    for i in range(1, 103):
        distanceBright.append(float(search_song_data[5]) - float(song_data[i][5]))
    print("明るさの差")
    print(distanceBright)

    distanceSynth = []
    for i in range(1, 103):
        distanceSynth.append(float(search_song_data[6]) - float(song_data[i][6]))
    print("シンセ度の差")
    print(distanceSynth)

    distanceSmart = []
    for i in range(1, 103):
        distanceSmart.append(float(search_song_data[7]) - float(song_data[i][7]))
    print("かっこよさの差")
    print(distanceSmart)

    distance = []
    for i in range(102):
        distance.append(math.sqrt(distanceTempo[i]**2 + distanceBright[i]**2 + distanceSynth[i]**2 + distanceSmart[i]**2))
    print("距離リスト")
    print(distance)

    info = []
    for i in range(102):
        info_row = []
        for j in range(0, 4):
            info_row.append(song_data[i+1][j])
        info_row.append(distance[i])
        info.append(info_row)

    sorted_info = sorted(info, key = lambda row: row[-1])

    print("距離が近い順に並べ替えました")
    print(sorted_info)

    results_list = document.querySelector("#results-list")

    results_list.innerHTML = ""

    for row in sorted_info[1:]:
        li = document.createElement("li")
        
        # <li> タグの中に入れるテキストを設定する
        # row[0] には曲名が入っているね
        # f-string を使うと、アルバム名とかも一緒に入れられて便利だよ
        li.innerText = f"{row[0]}（{round(row[4], 2)}）"
        # li.innerText = f"{row[0]}"
        
        # 出来上がった <li> を <ol> の中に追加する
        results_list.append(li)