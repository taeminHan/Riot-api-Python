import re
from tkinter import messagebox

import requests
from tkinter import*
import tkinter.messagebox


def run():
    #재검색 초기화 부분
    lv.delete(0, END)
    Tier.delete(0, END)
    Solo_Rank_Win.delete(0, END)
    Solo_Rank_lose.delete(0, END)
    Solo_Rank_Per.delete(0, END)
    F_Rank_Tier.delete(0, END)
    F_Rank_Win.delete(0, END)
    F_Rank_lose.delete(0, END)
    F_RankPer.delete(0, END)

    #구현부
    nick_name = str(one.get())
    URL_front = 'https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/'
    URL_end = '?api_key=RGAPI-fe6feda5-a105-467c-b4dd-236c37445265'
    response = requests.get(URL_front + nick_name + URL_end)

    response.status_code
    information = response.text

    # 고유아이디 추출
    info = information.split('"')

    original_id = info[3]

    # 레벨추출
    level = re.findall("\d+", info[-1])


    # 랭크 정보
    Rank_URL_front = 'https://kr.api.riotgames.com/lol/league/v4/entries/by-summoner/'
    Rank_URL_end = '?api_key=RGAPI-fe6feda5-a105-467c-b4dd-236c37445265'

    # 랭크 URL조합
    response_r = requests.get(Rank_URL_front + original_id + Rank_URL_end)

    response_r.status_code
    information_r = response_r.text

    # 정보 재배치
    solo_r = information_r.replace("\"", "").replace(":", ",")
    solo_r = solo_r.split(",")




    if (info[5] == 'Data not found - summoner not found' or info[5] == 'Forbidden'):
        messagebox.showinfo("Error", "소환사의 정보가 없습니다.")
    else:
        lv.insert(0, level[-1])
        try:
            Tier.insert(0, solo_r[5] + " " + solo_r[7] + " " +solo_r[13])
            Solo_Rank_Win.insert(0, solo_r[15])
            Solo_Rank_lose.insert(0, solo_r[17])
            result_1 = (int(solo_r[15]) / (int(solo_r[15]) + int(solo_r[17]))) * 100
            result_1 = round(result_1, 2)
            result_1 = str(result_1)
            Solo_Rank_Per.insert(0, result_1+"%")
        except IndexError:
            Tier.delete(0, END)
            Tier.insert(0, str("랭크 정보가 없습니다."))

        try:
            F_Rank_Tier.insert(0, solo_r[31] + " " + solo_r[33] + " " +solo_r[39])
            F_Rank_Win.insert(0, solo_r[41])
            F_Rank_lose.insert(0, solo_r[43])
            result_2 = (int(solo_r[41]) / (int(solo_r[41]) + int(solo_r[43]))) * 100
            result_2 = round(result_2, 2)
            result_2 = str(result_2)
            F_RankPer.insert(0, result_2+"%")
        except IndexError:
            F_Rank_Tier.insert(0, str("랭크 정보가 없습니다."))









window = Tk()

window.title("LoL Search")
#닉네임
one = Entry(window, width=15)
one.grid(row=0,column=0)

#검색 버튼
b1 = Button(window, text="Search", command=run)
b1.grid(row=0,column=1)

#레벨 엔트리
lv_title = Label(window, text="level: ", width=5)
lv_title.grid(row=0, column=2)

lv = Entry(window, width=5)
lv.grid(row=0, column=3)

#솔로랭크 엔트리

Solo_Rank_Title = Label(window, text="Solo_Rank")
Solo_Rank_Title.grid(row=1, column=0)

Tier_Title = Label(window, text="Tier", width=5)
Tier_Title.grid(row=2, column=0)

Tier = Entry(window, width=20)
Tier.grid(row=2, column=1)

Solo_Rank_WinTitle = Label(window, text="Win", width=5)
Solo_Rank_WinTitle.grid(row=2, column=2)

Solo_Rank_Win = Entry(window, width=5)
Solo_Rank_Win.grid(row=2, column=3)

Solo_Rank_loseTitle = Label(window, text="Lose", width=5)
Solo_Rank_loseTitle.grid(row=2, column=4)

Solo_Rank_lose = Entry(window, width=5)
Solo_Rank_lose.grid(row=2, column=5)

Solo_Rank_PerTitle = Label(window, text="승률", width=5)
Solo_Rank_PerTitle.grid(row=2, column=6)

Solo_Rank_Per = Entry(window, width=7)
Solo_Rank_Per.grid(row=2, column=7)

#Team_Rank
F_Rank_Title = Label(window, text="Team Rank")
F_Rank_Title.grid(row=3, column=0)

F_Rank_Tier_Title = Label(window, text="Tier", width=5)
F_Rank_Tier_Title.grid(row=4, column=0)

F_Rank_Tier = Entry(window, width=20)
F_Rank_Tier.grid(row=4, column=1)

F_Rank_Rank_WinTitle = Label(window, text="Win", width=5)
F_Rank_Rank_WinTitle.grid(row=4, column=2)

F_Rank_Win = Entry(window, width=5)
F_Rank_Win.grid(row=4, column=3)

F_Rank_loseTitle = Label(window, text="Lose", width=5)
F_Rank_loseTitle.grid(row=4, column=4)

F_Rank_lose = Entry(window, width=5)
F_Rank_lose.grid(row=4, column=5)

F_Rank_PerTitle = Label(window, text="승률", width=5)
F_Rank_PerTitle.grid(row=4, column=6)

F_RankPer = Entry(window, width=7)
F_RankPer.grid(row=4, column=7)


window.mainloop()
