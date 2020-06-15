import requests
import re
from tkinter import*

class Search:
    def __init__(self, nick_name):
        self.nick_name = nick_name

    def Base(self):

        URL_front = 'https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/'
        URL_end = '?api_key=RGAPI-3ade29dc-1676-4003-9b2d-441089386cda'

        response = requests.get(URL_front + self.nick_name + URL_end)
        response.status_code
        information = response.text

        # 고유아이디 추출
        info = information.split('"')

        original_id = info[3]

        # 레벨추출
        global level
        level = re.findall("\d+", info[-1])



    def Rank(self):
        URL_front = 'https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/'
        URL_end = '?api_key=RGAPI-3ade29dc-1676-4003-9b2d-441089386cda'

        response = requests.get(URL_front + self.nick_name + URL_end)
        response.status_code
        information = response.text

        # 고유아이디 추출
        global info
        info = information.split('"')

        original_id = info[3]
        # 랭크 정보
        Rank_URL_front = 'https://kr.api.riotgames.com/lol/league/v4/entries/by-summoner/'
        Rank_URL_end = '?api_key=RGAPI-3ade29dc-1676-4003-9b2d-441089386cda'

        # 랭크 URL조합
        response_r = requests.get(Rank_URL_front + original_id + Rank_URL_end)

        response_r.status_code
        information_r = response_r.text

        # 정보 재배치
        global solo_r
        solo_r = information_r.replace("\"", "").replace(":", ",")
        solo_r = solo_r.split(",")

    def Show_info(self):


        if (info[5] == 'Data not found - summoner not found'):
            print("소환사의 정보가 없습니다.")
        else:
            print("\n소환사 레벨: " + level[-1])
            print("=" * 30)
            try:
                print("솔로랭크: " + solo_r[5] + " " + solo_r[7] + " " + solo_r[13])
                win = solo_r[15]
                lose = solo_r[17]
                result_1 = (int(win) / (int(win) + int(lose))) * 100
                print("승률: %.2f%%" % result_1)
                print("솔로랭크 승리: " + solo_r[15])
                print("솔로랭크 패배: " + solo_r[17])
                print("=" * 30)
            except IndexError:
                print("==솔로 랭크 정보가 없습니다.==")
            try:
                print("자유랭크: " + solo_r[31] + " " + solo_r[33] + " " + solo_r[39])
                win_2 = solo_r[41]
                lose_2 = solo_r[43]
                result_2 = (int(win_2) / (int(win_2) + int(lose_2))) * 100
                print("승률: %.2f%%" % result_2)
                print("자유랭크 승리: " + solo_r[41])
                print("자유랭크 패배: " + solo_r[43])
            except IndexError:
                print("==자유 랭크 정보가 없습니다.==")



input_Data = input("닉네임을 입력해 주세요")

user = Search(input_Data)
user.Base()
user.Rank()
user.Show_info()






