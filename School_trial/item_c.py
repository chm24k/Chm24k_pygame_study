from tkinter import *
from PIL import ImageTk as imk
import map

item_1 = ''
item_2 = ''
item_3 = ''
item_4 = ''
item_5 = ''
# item_1_index = 0
# item_2_index = 0
# item_3_index = 0
class ITEMCHECK:
    def __init__(self,item1):
        self.item1 = item1

        self.item_box_x = imk.PhotoImage(file = "illust/시작화면/아이템.png")
        self.item_box = Label(self.item1, image = self.item_box_x)
        self.item_box.place(x = -2, y = -2)

        # self.item_blank_x = imk.PhotoImage(file = "illust/아이템/조합용.png")
        # self.item_blank1 = Label(self.item1, image = self.item_blank_x)
        # self.item_blank1.place(x = 692, y = 62)
        #
        # self.item_blank2 = Label(self.item1, image = self.item_blank_x)
        # self.item_blank2.place(x = 851, y = 62)


        self.label = Label(self.item1, text = "보유한 아이템")
        self.label.place(x = 370, y = 200)

        okbtn = Button(self.item1, text = "사용", command = self.item_o, padx = 10, pady = 10)
        okbtn.place(x = 750, y = 180)
        Backbtn = Button(self.item1, text="돌아가기", command=self.movBack)
        Backbtn.place(x=1070, y=600)

        self.listbox = Listbox(self.item1, selectmode = "extended", height = 10, width = 60)
        self.listbox.place(x = 370, y = 230)

        for index, x in enumerate(map.Map_gone.inven):
            print(x)
            self.listbox.insert(index, x)

        # self.showyou = self.listbox.curselection()
        # if '1989년 졸업앨범' == map.Map_gone.inven[self.showyou]:
        #     self.zolup_elbum = imk.PhotoImage(file="illust/졸업앨범_구.png")
        #     self.zolup = Label(self.item1, image=self.zolup_elbum)
        #     self.zolup.place(x=-2, y=-2)
        #
        #     Backbtn = Button(self.item1, text="돌아가기", command=self.movBack)
        #     Backbtn.place(x=1070, y=600)

    #조합법1 -->

    def item_o(self):
        # global item_1, item_2, item_3, item_4, item_5
        # #global item_1_index, item_2_index, item_3_index
        # for x in self.listbox.curselection():
        #     if map.Map_gone.inven[x] == '잉크':
        #         item_1 = map.Map_gone.inven[x]
        #         #item_1_index = x
        #     if map.Map_gone.inven[x] =='빈 편지지':
        #         item_2 = map.Map_gone.inven[x]
        #         #item_2_index = x
        #     if map.Map_gone.inven[x] =='오래된 진심':
        #         item_3 = map.Map_gone.inven[x]
        #         #item_3_index = x
        #     if map.Map_gone.inven[x] =='차가운 국화':
        #         item_4 = map.Map_gone.inven[x]
        #
        #     if map.Map_gone.inven[x] == '보온병':
        #         item_5 = map.Map_gone.inven[x]


        if '잉크'and '빈 편지지' and '오래된 진심' in map.Map_gone.inven:
            map.Map_gone.inven.append('『누군가의 진심이 담긴 편지』')
            map.Map_gone.inven.remove('잉크')
            map.Map_gone.inven.remove('빈 편지지')
            map.Map_gone.inven.remove('오래된 진심')
            print(map.Map_gone.inven)
            map.Map_gone(self.item1)


        if '보온병' and '차가운 국화'  in map.Map_gone.inven:
            map.Map_gone.inven.append('『따뜻한 국화』')
            map.Map_gone.inven.remove('보온병')
            map.Map_gone.inven.remove('차가운 국화')
            print(map.Map_gone.inven)
            map.Map_gone(self.item1)

        # if item_1 == '잉크':
        #     if item_2 == '빈 편지지':
        #         if item_3 =='오래된 진심':
        #             map.Map_gone.inven.append('『누군가의 진심이 담긴 편지』')
        #             if '『누군가의 진심이 담긴 편지』' in map.Map_gone.inven:
        #
        #                 map.Map_gone.inven.remove('잉크')
        #                 map.Map_gone.inven.remove('빈 편지지')
        #                 map.Map_gone.inven.remove('오래된 진심')
        #             print(map.Map_gone.inven)
        #             print('조합완료')
        #             map.Map_gone(self.item1)

        # if item_4 =='차가운 국화':
        #     if item_5 == '보온병':
        #         map.Map_gone.inven.append('『따뜻한 국화』')
        #         if '『따뜻한 국화』' in map.Map_gone.inven:
        #             map.Map_gone.inven.remove('보온병')
        #             map.Map_gone.inven.remove('차가운 국화')
        #             map.Map_gone.inven.remove('『따뜻한 국화』')





        # print('조합완료')


        # if '『따뜻한 국화』' in map.Map_gone.inven:
        #     map.Map_gone.inven.remove('보온병')
        #     map.Map_gone.inven.remove('차가운 국화')
        #
        # if '『누군가의 진심이 담긴 편지』' in map.Map_gone.inven:
        #     map.Map_gone.inven.remove('잉크')
        #     map.Map_gone.inven.remove('빈 편지지')
        #     map.Map_gone.inven.remove('오래된 진심')
        # if '『누군가의 진심이 담긴 편지』' in map.Map_gone.inven:
        #
        #     map.Map_gone.inven.remove('잉크')
        #     map.Map_gone.inven.remove('빈 편지지')
        #     map.Map_gone.inven.remove('오래된 진심')


    def movBack(self):
        map.Map_gone(self.item1)