from kivymd.app import MDApp
from kivymd.theming import ThemeManager
from kivy.lang import Builder
import Jurecom
import pandas as pd
import numpy as np
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel
from kivymd.utils.fitimage import FitImage
from kivy.uix.image import Image
from kivymd.uix.imagelist import SmartTileWithLabel
from kivymd.toast.kivytoast import toast
from kivymd.uix.chip import MDChip
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard
from kivy.clock import Clock
import association
import webbrowser
aaa = Jurecom.sulrecom()
sulsort = aaa.method_recom(Jurecom.tak)
lol = pd.read_csv('키워드모음.csv')

KV1 = '''
<Manager>:
    id:screen_manager
<MDChip>:
    check:True
    color:(0,0,0,0.3)
    icon:''
    radius:dp(10)

<mainscreen>:
    sulname:sulname
    kwd:kwd
    chatcont : chatcont
    chatbot:chatbot
    MDBoxLayout:
        orientation:'vertical'
        pos_hint:{"center_x": .5, "center_y": .5}
        spacing:dp(10)
        MDToolbar:
            title:"주여!"
            anchor_title:'center'
            md_bg_color: (1,1,1,1)
            specific_text_color: (0,0,0,1)
            remove_shadow:
        MDBottomNavigation:
            padding:dp(20)
            MDBottomNavigationItem:
                text:"검색"
                name:"main"
                icon:"bottle-wine"
                MDBoxLayout:
                    orientation:'vertical'
                    MDBoxLayout:
                        id:gumsack
                        orientation:'vertical'
                        adaptive_height : True
                        MDTextField:
                            id:sulname
                            hint_text:"술이름 검색"
                            helper_text:"술 이름을 입력해주세요"
                            helper_text_mode:"on_focus" # "on_focus"
                            icon_right: "magnify"
                            required:True
                            helper_text_mode: "on_error"
                            helper_text: "텍스트를 입력해주세요"
                            on_text_validate:root.recsul()
                    MDLabel:
                        text:'자주 찾는 키워드'
                        font_size:dp(16)
                        size_hint_y : None
                        height : dp(24)
                    ScrollView:
                        size_hint_y : 0.2
                        MDBoxLayout:
                            id:kwd
                            orientation:'horizontal'
                            adaptive_width : True
                            spacing:dp(5)
                    MDSeparator:
                        height: "1dp"
                    MDLabel:
                        text:'전통주갤러리 - 이달의 시음주'
                        font_size:dp(25)
                        size_hint_y : 0.3
                    MDBoxLayout:
                        orientation:'vertical'
                        ScrollView:
                            MDBoxLayout:
                                orientation:'vertical'
                                adaptive_height:True
                                spacing:dp(5)
                                MDCard:
                                    orientation: "vertical"
                                    padding: "8dp"
                                    size_hint: None, None
                                    size: dp(320),dp(180)
                                    pos_hint: {"center_x": .5, "center_y": .5}
                                    on_press:root.recsul2('금정산성막걸리')
                                    MDLabel:
                                        text: "금정산성막걸리"
                                        theme_text_color: "Secondary"
                                        size_hint_y: None
                                        height: self.texture_size[1]
                                        MDSeparator:
                                            height: "1dp"
                                    Image:
                                        source:'image/금정산성막걸리.png'
                                        size_hint_y:1
                                MDCard:
                                    orientation: "vertical"
                                    padding: "8dp"
                                    size_hint: None, None
                                    size: dp(320),dp(180)
                                    pos_hint: {"center_x": .5, "center_y": .5}
                                    on_press:root.recsul2('복순도가 탁주')
                                    MDLabel:
                                        text: "복순도가 탁주"
                                        theme_text_color: "Secondary"
                                        size_hint_y: None
                                        height: self.texture_size[1]
                                        MDSeparator:
                                            height: "1dp"
                                    Image:
                                        source:'image/복순도가 탁주.png'
                                        size_hint_y:1
                                MDCard:
                                    orientation: "vertical"
                                    padding: "8dp"
                                    size_hint: None, None
                                    size: dp(320),dp(180)
                                    pos_hint: {"center_x": .5, "center_y": .5}
                                    on_press:root.recsul2('장생도라지 진주 프리미엄')
                                    MDLabel:
                                        text: "장생도라지 진주 프리미엄"
                                        theme_text_color: "Secondary"
                                        size_hint_y: None
                                        height: self.texture_size[1]
                                        MDSeparator:
                                            height: "1dp"
                                    Image:
                                        source:'image/장생도라지 진주 프리미엄.png'
                                        size_hint_y:1
                                MDCard:
                                    orientation: "vertical"
                                    padding: "8dp"
                                    size_hint: None, None
                                    size: dp(320),dp(180)
                                    pos_hint: {"center_x": .5, "center_y": .5}
                                    on_press:root.recsul2('산애딸기 스위트')
                                    MDLabel:
                                        text: "산애딸기 스위트"
                                        theme_text_color: "Secondary"
                                        size_hint_y: None
                                        height: self.texture_size[1]
                                        MDSeparator:
                                            height: "1dp"
                                    Image:
                                        source:'image/산애딸기 스위트.png'
                                        size_hint_y:1
                                MDCard:
                                    orientation: "vertical"
                                    padding: "8dp"
                                    size_hint: None, None
                                    size: dp(320),dp(180)
                                    pos_hint: {"center_x": .5, "center_y": .5}
                                    on_press:root.recsul2('담솔')
                                    MDLabel:
                                        text: "담솔"
                                        theme_text_color: "Secondary"
                                        size_hint_y: None
                                        height: self.texture_size[1]
                                        MDSeparator:
                                            height: "1dp"
                                    Image:
                                        source:'image/담솔.png'
                                        size_hint_y:1
                        
            MDBottomNavigationItem:
                text:"챗봇"
                name:"Chatbot"
                icon:"chat"
                MDBoxLayout:
                    padding:(10,0)
                    orientation:'vertical'
                    ScrollView:
                        MDBoxLayout:
                            orientation : 'vertical'
                            MDBoxLayout:
                                spacing : dp(10)
                                orientation:'horizontal'
                                adaptive_height : True
                                MDFillRoundFlatIconButton:
                                    text:'날씨'
                                    bold : True
                                    icon: "weather-cloudy"
                                    on_press : root.pressbtn(self.text)
                                MDFillRoundFlatIconButton:
                                    text:'상황'
                                    bold : True
                                    icon: "account"
                                    on_press : root.pressbtn(self.text)
                                MDFillRoundFlatIconButton:
                                    text:'안주'
                                    bold : True
                                    icon: "silverware-fork-knife"
                                    on_press : root.pressbtn(self.text)
                            MDBoxLayout:
                                orientation : 'vertical'
                                spacing : dp(10)
                                id : chatcont
                    MDTextField:
                        id:chatbot
                        hint_text:"대답을 입력해주세요"
                        helper_text:"대답을 입력해주세요"
                        helper_text_mode:"on_focus" # "on_focus"
                        icon_right: "chat"
                        required:True
                        helper_text_mode: "on_error"
                        helper_text: "텍스트를 입력해주세요"
                        on_text_validate : root.chatbot1(self.text)
            MDBottomNavigationItem:
                text:"라벨인식"
                name:"Labelshot"
                icon:"camera"
                BoxLayout:
                    Camera:
                        id: camera
                        resolution: (600,500)
                        play: True
            MDBottomNavigationItem:
                text:"외부링크"
                name:"link"
                icon:"link-variant"
                MDBoxLayout:
                    orientation:'vertical'
                    padding:(10,10,10,10)
                    MDLabel:
                        text:'지역별 양조장 정보'
                        font_size : dp(25)
                        size_hint_y : None
                        height : dp(35)
                    Button:
                        background_normal: 'jido.png'
                        on_press: root.jidolink()
                    MDLabel:
                        text:'주류 통계자료'
                        font_size : dp(25)
                        size_hint_y : None
                        height : dp(35)
                    Button:
                        background_normal: 'graph.png'
                        on_press: root.graphlink()   
<listscreen>:
    result:result
    BoxLayout:
        orientation:'vertical'
        spacing:dp(10)
        MDToolbar: 
            title:'이 술을 찾으시나요?'
            remove_shadow:
            font_size:dp(30)
            left_action_items: [["arrow-left-bold-circle-outline", lambda x: root.goback()]]
            md_bg_color: (1,1,1,1)
            specific_text_color: (0,0,0,1)
        ScrollView:
            MDBoxLayout:
                id:result
                orientation:'vertical'
                adaptive_height:True
                halign:'center'
                padding:dp(20)
                spacing:dp(20)
<findsul>:
    img:img
    label1:label1
    label2:label2
    orientation: "horizontal" 
    size_hint: None, None
    size: dp(320),dp(100)
    pos_hint:{"center_x": .5, "center_y": .5}
    Image:
        id:img
        size_hint_x : 0.4
    MDBoxLayout:
        id:text_box
        orientation: "vertical"
        MDLabel:
            id:label1
            theme_text_color: "Primary"
            font_style: "H6"
            bold: True
            adaptive_height : True
        MDLabel:
            id:label2
            valign:'top'
            theme_text_color: "Secondary"
            font_style:'Caption'
            
            

<infoscreen>:
    toolbar:toolbar
    testimage:testimage
    infolayer:infolayer
    imglist:imglist
    keyword:keyword
    anju:anju
    award:award
    BoxLayout:
        orientation:'vertical'
        MDToolbar:
            id:toolbar
            remove_shadow:
            left_action_items: [["arrow-left-bold-circle-outline", lambda x: root.goback()]]
            md_bg_color: (1,1,1,1)
            specific_text_color: (0,0,0,1)
        ScrollView:
            MDGridLayout:
                cols:1
                adaptive_height:True
                spacing:dp(30)
                padding:dp(20)
                MDBoxLayout:
                    orientation:'horizontal'
                    size_hint_y : None
                    height:dp(250)
                    Image:
                        id:testimage
                        size_hint_x : 0.5
                        size_hint_y : 1
                    MDGridLayout:
                        cols:2
                        spacing:dp(5)
                        padding:dp(20)
                        id:infolayer
                MDSeparator:
                    height:dp(2) 
                MDLabel:
                    text:'키워드'
                    font_size:dp(25)
                    size_hint_y : None
                    height:dp(35)
                    padding:dp(0),dp(60)
                    bold:True
                    valign:'center'
                MDLabel:
                    id:keyword
                    font_size:dp(20)
                    size_hint_y : None
                    padding:dp(20),dp(20)
                    height:dp(80)
                MDSeparator:
                    height:dp(2)
                MDLabel:
                    text:'수상내역'
                    font_size:dp(25)
                    size_hint_y : None
                    height:dp(35)
                    padding:dp(0),dp(80)
                    bold:True
                    valign:'center'
                MDLabel:
                    id:award
                    font_size:dp(20)
                    padding:dp(20),dp(20)
                    size_hint_y : None
                    height:self.height
                    size: self.texture_size
                MDSeparator:
                    height:dp(2)
                MDLabel:
                    text:'어울리는 안주'
                    font_size:dp(25)
                    size_hint_y : None
                    height:dp(35)
                    padding:dp(0),dp(60)
                    bold:True
                    valign:'center'
                MDLabel:
                    id:anju
                    font_size:dp(20)
                    size_hint_y : None
                    padding:dp(20),dp(20)
                    height:dp(80)
                MDSeparator:
                    height:dp(2)
                MDLabel:
                    text:'유사한 전통주'
                    font_size:dp(25)
                    size_hint_y:None
                    height:dp(35)
                    padding:dp(0),dp(40)
                    bold:True
                    valign:'center'
                MDBoxLayout:
                    spacing: dp(10)
                    id:imglist
                    orientation:'vertical'
                    adaptive_height:True
<introscreen>:
    Image:
        source:'Juyeo.jpg'
        size_hint:0.7,0.7
        pos_hint:{"center_x": .5, "center_y": .5}
            
        

'''

class findsul(MDCard):
    pass

class listscreen(MDScreen):
    def __init__(self,suls, **kwargs):
        super(listscreen, self).__init__(**kwargs)
        for i in range(len(suls)):
            self.sulpick = findsul()
            self.sulpick.img.source = 'image/'+suls.iloc[i]['ALCOHOL_NAME']+'.png'
            self.sulpick.label1.text = suls.iloc[i]['ALCOHOL_NAME']
            self.sulpick.label2.text = '#'+suls.iloc[i]['KEYWORD']
            self.sulpick.bind(on_press=self.recsul)
            self.result.add_widget(self.sulpick)
    def goback(self):
        presc = self.manager.previous()
        self.manager.current = presc
        self.manager.remove_widget(self)
    def recsul(self,instance):
        sulname = instance.label1.text
        sul = Jurecom.find_sim_ju(Jurecom.tak,sulsort,sulname,4)
        self.manager.add_widget(infoscreen(sul,sulname,name='info')) 
        self.manager.current = 'info'
    

class infoscreen(MDScreen):
    def __init__(self,sul,sulname, **kwargs):
        super(infoscreen, self).__init__(**kwargs)
        pickedsul = sul.loc[sul['ALCOHOL_NAME']==sulname]
        pickedsul = pickedsul.iloc[0]
        self.toolbar.title = pickedsul['ALCOHOL_NAME']
        self.testimage.source = 'image/'+pickedsul['ALCOHOL_NAME']+'.png'
        self.infolayer.add_widget(MDLabel(text='종류',size_hint_x = 0.6,size_hint_y=0.3,bold=True))
        self.infolayer.add_widget(MDLabel(text=pickedsul['KIND'],size_hint_y=0.3))
        self.infolayer.add_widget(MDLabel(text='도수',size_hint_x = 0.6,size_hint_y=0.3,bold=True))
        self.infolayer.add_widget(MDLabel(text=pickedsul['ALCOHOL_BY_VOLUME'],size_hint_y=0.3))
        self.infolayer.add_widget(MDLabel(text='용량',size_hint_x = 0.6,size_hint_y=0.3,bold=True))
        self.infolayer.add_widget(MDLabel(text=pickedsul['ALCOHOL_AMOUNT'],size_hint_y=0.3))
        self.keyword.text = '#'+pickedsul['KEYWORD']
        self.award.text = pickedsul['AWARD_LIST']
        self.anju.text = pickedsul['MATFOOD']

        self.suldrop = sul
        self.suldx = self.suldrop[self.suldrop['ALCOHOL_NAME']==sulname].index
        self.suldrop = self.suldrop.drop(self.suldx)
        print(self.suldrop)

        for i in range(0,4):
            self.sulpick = findsul()
            self.sulpick.img.source = 'image/'+self.suldrop.iloc[i]['ALCOHOL_NAME']+'.png'
            self.sulpick.label1.text = self.suldrop.iloc[i]['ALCOHOL_NAME']
            self.sulpick.label2.text = '#'+self.suldrop.iloc[i]['KEYWORD']
            self.sulpick.bind(on_press=self.SCloop)
            self.imglist.add_widget(self.sulpick)
    def SCloop(self,instance):
        sulname = instance.label1.text
        sul = Jurecom.find_sim_ju(Jurecom.tak,sulsort,sulname,4)
        if type(sul) == str:
            print('에러에러에러')
        else :
            self.manager.switch_to(infoscreen(sul,sulname,name='info'))
    def goback(self):
        presc = self.manager.previous()
        self.manager.current = presc
        self.manager.remove_widget(self)

class mainscreen(MDScreen):
    var = 0
    press = ''
    def __init__(self, **kwargs):
        super(mainscreen, self).__init__(**kwargs)
        kword = Jurecom.kwd
        for i in range(15):
            self.kwd.add_widget(MDChip(label = kword.iloc[i]['KEYWORD'],callback = self.check1))
        
    def pressbtn(self,tex):
        self.var = 1
        self.press = tex
        self.chatcont.add_widget(MDLabel(text = '당신의 성별은 무엇입니까?',halign = 'left'))
    
    def chatbot1(self,inputs):
        print(self.var)
        self.var += 1
        self.chatbot.text = ''
        if self.var == 2 :
            if (inputs =='남자' or inputs =='여자'):
                self.chatcont.add_widget(MDLabel(text = inputs ,halign = 'right'))
                self.chatcont.add_widget(MDLabel(text = '당신의 성별은 ' + inputs + '이군요',halign = 'left'))
                self.chatcont.add_widget(MDLabel(text = '당신의 나이를 입력해주세요',halign = 'left'))
                self.var +=1
            else : 
                self.var -=1
        if self.var == 4 :
            if (inputs.isdigit()):
                self.chatcont.add_widget(MDLabel(text = inputs ,halign = 'right'))
                self.chatcont.add_widget(MDLabel(text = '당신의 나이는 ' + inputs + '살 이군요',halign = 'left'))
                self.chatcont.add_widget(MDLabel(text = '어떤'+self.press+'입니까?',halign = 'left'))
                self.var +=1
            else:
                self.var -=1
        if self.var == 6 :
            self.chatcont.add_widget(MDLabel(text = inputs ,halign = 'right'))
            reply = association.chatbot(self.press,inputs)
            self.chatcont.add_widget(MDLabel(text = reply+' 전통주를 추천드립니다' ,halign = 'left'))
            self.sulpick = findsul()
            self.sulpick.img.source = 'image/'+reply+'.png'
            self.sulpick.label1.text = reply
            self.sulpick.bind(on_press=self.recsul3)
            self.chatcont.add_widget(self.sulpick)
            self.var = 0


    def recsul(self):
        if self.sulname.text[0] == '/':
            kwdtak = aaa.yoursul(self.sulname.text[1:])
            sulsort1 = aaa.method_recom(kwdtak)
            sul = Jurecom.find_sim_ju1(kwdtak,sulsort1,'당신의 술',5)
            self.manager.add_widget(listscreen(sul,name='sullist')) 
            self.manager.current = 'sullist'
        else:
            sulname = self.sulname.text
            print(sulname)
            sul = Jurecom.sulgle(Jurecom.tak,sulname)
            self.manager.add_widget(listscreen(sul,name='sullist')) 
            self.manager.current = 'sullist'

    def recsul2(self,sulpick):
        sulname = sulpick
        print(sulname)
        sul = Jurecom.find_sim_ju(Jurecom.tak,sulsort,sulname,4)
        if type(sul) == str:
            print('에러에러에러')
        else :
            self.manager.add_widget(infoscreen(sul,sulname,name='info')) 
            self.manager.current = 'info'
    def recsul3(self,instance):
        sulname = instance.label1.text
        print(sulname)
        sul = Jurecom.find_sim_ju(Jurecom.tak,sulsort,sulname,4)
        if type(sul) == str:
            print('에러에러에러')
        else :
            self.manager.add_widget(infoscreen(sul,sulname,name='info')) 
            self.manager.current = 'info'

    def jidolink(self):
        webbrowser.open("https://map-page.shinyapps.io/map2/")
    
    def graphlink(self):
        webbrowser.open("https://lsw6600.shinyapps.io/ggplot/")
    
    def check1(self,instance,value):
        if value in self.sulname.text:
            print(self.sulname.text)
            self.sulname.text = self.sulname.text.replace('/'+value,'')
        else:
            print(self.sulname.text)
            self.sulname.text = self.sulname.text+'/'+value

        
class Introscreen(MDScreen):
    def gogo(self,dt):
        self.manager.switch_to(mainscreen(name='main')) 

    def __init__(self, **kwargs):
        super(Introscreen, self).__init__(**kwargs)
        Clock.schedule_once(self.gogo, 6)

      
        
class Manager(ScreenManager):
    def __init__(self, **kwargs):
        super(Manager, self).__init__(**kwargs)
        self.add_widget(Introscreen(name='intro'))
        self.current = 'intro'

class atinapp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Indigo"
        self.root = Builder.load_string(KV1)
        return Manager()

    

atinapp().run()
