'''
MAJOR PROJECT  CSE-1  2013-2017 Batch
Guru Tegh Bahadur Institute of Technology
Guru Gobind Singh Indraprastha University
Submitted by:
Alisha (03/CSE1/2017)
Avneet Singh Malhotra (20/CSE1/2017)
Sanjot Kaur (22/CSE1/2017)
Tavleen Kaur (23/CSE1/2017)
Project Guide:
Mrs. Jasleen Kaur Sethi
Project Coordinators:
Mrs. Amandeep Kaur
Mrs. Geetika Bhatia
'''

from apiclient.discovery import build 
from apiclient.errors import HttpError 
import pandas as pd
from tkinter import *
import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np
#import sys
import webbrowser
from sklearn.cluster import KMeans
from urllib.request import urlopen
from bs4 import BeautifulSoup
from sklearn.cluster import AgglomerativeClustering
from PIL import ImageTk, Image

#Main Frame

root=Tk()

non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)         ##unicode error

w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
MainFrame=Frame(root)
fs1=Frame(root)
fs2=Frame(root)
fs3=Frame(root)
fs4=Frame(root)
fs5=Frame(root)
fs6=Frame(root)


root.configure(background='azure')

def raise_frame(frame):
    frame.tkraise()

f=[MainFrame,fs1,fs2,fs3,fs4,fs5,fs6]

for frame in f:
     frame.grid(row=0,column=0,sticky='news')
     frame.configure(background='azure')
     
raise_frame(MainFrame)

labelM1=Label(MainFrame,text="INFOTUBE",font=("Helvetica", 50),bg="FireBrick",fg="Black").grid(row=1,column=3,rowspan=2,columnspan=2,padx=100,pady=20)

img5 = PhotoImage(file="infotube.png")
imglabel5 = Label(MainFrame, image=img5).grid(row=3, column=3,rowspan=2,columnspan=2)

img1 = PhotoImage(file="download.gif")
imglabel = Label(MainFrame, image=img1).grid(row=2, column=2)

buttonM1=Button(MainFrame,text='Search',width=10,font=("Helvetica", 30),bg="FireBrick",fg="Black",command=lambda:raise_frame(fs1)).grid(row=2,column=1,padx=20,pady=20)
buttonM2=Button(MainFrame,text="Trending",width=10,font=("Helvetica", 30),bg="FireBrick",fg="Black",command=lambda:raise_frame(fs2)).grid(row=2,column=6,padx=20,pady=20)



buttonM3=Button(MainFrame,text='Compare',width=10,font=("Helvetica", 30),bg="FireBrick",fg="Black",command=lambda:raise_frame(fs3)).grid(row=5,column=1,padx=20,pady=20)
buttonM4=Button(MainFrame,text="Analysis",width=10,font=("Helvetica", 30),bg="FireBrick",fg="Black",command=lambda:raise_frame(fs4)).grid(row=5,column=6,padx=20,pady=20)

img2 = PhotoImage(file="tech6.png")
imglabel2 = Label(MainFrame, image=img2).grid(row=2, column=5)

img3 = PhotoImage(file="tech7.png")
imglabel3 = Label(MainFrame, image=img3).grid(row=5, column=5)



img4 = PhotoImage(file="tech8.png")
imglabel4 = Label(MainFrame, image=img4).grid(row=5, column=2)


DEVELOPER_KEY = "AIzaSyAvAaiUGhdsXNOx5azQyH_AP6-39x8PyRc" 
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

try:
    #Search by Keyword Frame - fs1

    labelF11=Label(fs1,text="Enter keyword : " ,font=("Helvetica", 20),bg="FireBrick",fg="Black")
    labelF11.grid(row=2,column=2,padx=50,pady=50)

    vkeyF1 = StringVar()
    entryF11=Entry(fs1,textvariable=vkeyF1,bd=5).grid(row=2,column=3,padx=50,pady=50)

    labelF12=Label(fs1,text="Enter number of results : " ,font=("Helvetica", 20),bg="FireBrick",fg="Black")
    labelF12.grid(row=2,column=4,padx=50,pady=50)

    vmaxF1 = IntVar()
    entryF12=Entry(fs1,textvariable=vmaxF1,bd=5).grid(row=2,column=5,padx=50,pady=50)

    lOrder=["relevance","rating","viewCount","date"]
    lLength=["any","short","medium","long"]
    lType=["any","movie","episode"]
    lDefinition=["any","high","standard"]
    xlpy=1



    def callback(event):
        webbrowser.open_new(event.widget.cget("text"))

    def click():
        if(xlpy==1):
            print(v1.get(),v2.get(),v3.get(),v4.get())
            vOrder=lOrder[v1.get()]
            vLength=lLength[v2.get()]
            vType=lType[v3.get()]
            vDefinition=lDefinition[v4.get()]
            
            raise_frame(fs5)
            qval=vkeyF1.get()
            maxval=vmaxF1.get()
            print(qval,maxval)
            search_response = youtube.search().list(q=qval,part="id,snippet",maxResults=maxval,order=vOrder,
                                                    videoType=vType,videoDefinition=vDefinition,
                                                    videoDuration=vLength,type="video").execute()
            videos = {}
            res=[]
            vres=StringVar()
            res2=[]
            res4=[]

            for search_result in search_response.get("items", []):
                if search_result["id"]["kind"] == "youtube#video":
                    videos[search_result["id"]["videoId"]] = search_result["snippet"]["title"]

            video_ids_list = ','.join(videos.keys())

            video_list_stats = youtube.videos().list(id=video_ids_list,part='id,statistics').execute()

            i=0
            
            for keys,values in videos.items():
                try:
                    res.extend(((str(i+1)+str(". Title : "+values)).translate(non_bmp_map),str("Likes : "+video_list_stats['items'][i]['statistics']['likeCount'])
                           ,str("Dislikes : "+video_list_stats['items'][i]['statistics']['dislikeCount']),
                            str("Views : "+video_list_stats['items'][i]['statistics']['viewCount'])))
                    

                except:
                    res.extend(((str(i+1)+str(". Title : "+values)).translate(non_bmp_map),str("Likes : 0")
                           ,str("Dislikes : 0"),
                            str("Views : "+video_list_stats['items'][i]['statistics']['viewCount'])))
                
                finally:
                    i=i+1
                
                
            scroll1=Scrollbar(fs5)
            scroll1.grid(row=0,column=0,padx=2,pady=2)

            listing1=Listbox(fs5,yscrollcommand=scroll1.set,width=60,height=45,fg="green")

            for i in range(0,len(res)):
                listing1.insert(END,res[i])
                    
            listing1.grid(row=0,column=0,padx=2,pady=2)
            scroll1.config(command=listing1.yview)

           
            
            df1=[]

            i=0
            categ1=[]

            for keys,values in videos.items():
                categ1.append(keys)
                try:
                    df1.append([values,
                           int(video_list_stats['items'][i]['statistics']['likeCount']),
                           int(video_list_stats['items'][i]['statistics']['viewCount']),
                           int(video_list_stats['items'][i]['statistics']['dislikeCount'])])
                except:
                    df1.append([values,0,int(video_list_stats['items'][i]['statistics']['viewCount']),0])

                i=i+1

            labels=['Title','Likes','Views','Dislikes']

            df=pd.DataFrame.from_records(df1,columns=labels)

            mean1=df['Views'].mean()
            print(mean1)
            mean2=df['Likes'].mean()
            mean3=df['Dislikes'].mean()
            median1=df['Views'].median()
            median2=df['Likes'].median()
            median3=df['Dislikes'].median()

            res3=[]
            res3.append("Mean views : "+str(mean1))
            res3.append("Mean likes : "+str(mean2))
            res3.append("Mean dislikes : "+str(mean3))
            res3.append("Median of views : "+str(median1))
            res3.append("Median of likes : "+str(median2))
            res3.append("Median of dislikes : "+str(median3))

            res4='\n'.join(res3)

            vres2=StringVar()

            MsgF52=Message(fs5,textvariable=vres2,fg="red",relief=RAISED)
            MsgF52.config()
            vres2.set(str(res4))
            print(vres2)
            MsgF52.grid(row=0,column=1,padx=2,pady=2)

            bF13=Button(fs5,text="Main Frame" ,font=("Helvetica", 10),bg="black",fg="white",command=lambda:raise_frame(MainFrame)).place(x=400,y=10)

            labelgui=[]
            textgui=[]

            if(maxval>25):
                for i in range(0,maxval):
                    textgui.append(tk.Label(fs5,bg="azure",text=str(i+1)+". "+str(df['Title'][i]).translate(non_bmp_map),font=("Helvetica",8),fg="black"))
                    textgui[i].place(x=550,y=14*i)
                    labelgui.append(tk.Label(fs5,bg="azure",text="https://www.youtube.com/watch?v="+str(categ1[i]).translate(non_bmp_map),font=("Helvetica",8),fg="blue",cursor="hand2"))
                    labelgui[i].place(x=1000,y=14*i)
                    labelgui[i].bind("<Button-1>", callback)

            else:
                for i in range(0,maxval):
                    textgui.append(tk.Label(fs5,bg="azure",text=str(i+1)+". "+str(df['Title'][i]).translate(non_bmp_map),font=("Helvetica",9),fg="black"))
                    textgui[i].place(x=550,y=25*i)
                    labelgui.append(tk.Label(fs5,bg="azure",text="https://www.youtube.com/watch?v="+str(categ1[i]).translate(non_bmp_map),font=("Helvetica",9),fg="blue",cursor="hand2"))
                    labelgui[i].place(x=1000,y=25*i)
                    labelgui[i].bind("<Button-1>", callback)
    
        #except:
        #    raise_frame(MainFrame)
       



    v1=IntVar()
    v2=IntVar()
    v3=IntVar()
    v4=IntVar()

    labelF13=Label(fs1,text="Retrieve : " ,font=("Helvetica", 20),bg="FireBrick",fg="Black").place(x=200,y=250)
    labelF14=Label(fs1,text="Duration : " ,font=("Helvetica", 20),bg="FireBrick",fg="Black").place(x=400,y=250)
    labelF15=Label(fs1,text="Type : " ,font=("Helvetica", 20),bg="FireBrick",fg="Black").place(x=600,y=250)
    labelF16=Label(fs1,text="Definition : " ,font=("Helvetica", 20),bg="FireBrick",fg="Black").place(x=800,y=250)


    radioF1_1=Radiobutton(fs1,text="By Relevance",bg="azure",font=("Helvetica", 12),variable=v1,value=0,fg="FireBrick").place(x=200,y=300)
    radioF1_2=Radiobutton(fs1,text="By Rating",bg="azure",font=("Helvetica", 12),variable=v1,value=1,fg="FireBrick").place(x=200,y=350)
    radioF1_3=Radiobutton(fs1,text="By View Count",bg="azure",font=("Helvetica", 12),variable=v1,value=2,fg="FireBrick").place(x=200,y=400)
    radioF1_4=Radiobutton(fs1,text="By Date",bg="azure",font=("Helvetica", 12),variable=v1,value=3,fg="FireBrick").place(x=200,y=450)
    radioF1_5=Radiobutton(fs1,text="Any",bg="azure",font=("Helvetica", 12),variable=v2,value=0,fg="FireBrick").place(x=400,y=300)
    radioF1_6=Radiobutton(fs1,text="Short",bg="azure",font=("Helvetica", 12),variable=v2,value=1,fg="FireBrick").place(x=400,y=350)
    radioF1_7=Radiobutton(fs1,text="Medium",bg="azure",font=("Helvetica", 12),variable=v2,value=2,fg="FireBrick").place(x=400,y=400)
    radioF1_8=Radiobutton(fs1,text="Long",bg="azure",font=("Helvetica", 12),variable=v2,value=3,fg="FireBrick").place(x=400,y=450)
    radioF1_9=Radiobutton(fs1,text="Any",bg="azure",font=("Helvetica", 12),variable=v3,value=0,fg="FireBrick").place(x=600,y=300)
    radioF1_10=Radiobutton(fs1,text="Episode",bg="azure",font=("Helvetica", 12),variable=v3,value=1,fg="FireBrick").place(x=600,y=350)
    radioF1_11=Radiobutton(fs1,text="Movie",bg="azure",font=("Helvetica", 12),variable=v3,value=2,fg="FireBrick").place(x=600,y=400)
    radioF1_12=Radiobutton(fs1,text="Any",bg="azure",font=("Helvetica", 12),variable=v4,value=0,fg="FireBrick").place(x=800,y=300)
    radioF1_13=Radiobutton(fs1,text="High",bg="azure",font=("Helvetica", 12),variable=v4,value=1,fg="FireBrick").place(x=800,y=350)
    radioF1_14=Radiobutton(fs1,text="Standard",bg="azure",font=("Helvetica", 12),variable=v4,value=2,fg="FireBrick").place(x=800,y=400)

    bF11=Button(fs1,text="Show" ,font=("Helvetica", 20),bg="FireBrick",fg="Black",command=click).place(x=1000,y=350)
    bF12=Button(fs1,text="Main Frame" ,font=("Helvetica", 10),bg="black",fg="white",command=lambda:raise_frame(MainFrame)).place(x=1000,y=430)



    #Trending videos search frame - fs2
    
    labelF21=Label(fs2,text=" TRENDING VIDEOS\n ON YOUTUBE " ,font=("Helvetica", 40),bg="FireBrick",fg="Black")
    labelF21.grid(row=1,column=3,padx=10,pady=30)
    
    img10 =PhotoImage(file="info2.gif")
    imglabel10 = Label(fs2, image=img10).grid(row=1,column=2,padx=10,pady=30)

    labelF21=Label(fs2,text="Enter number of results : " ,font=("Helvetica", 20),bg="FireBrick",fg="Black")
    labelF21.grid(row=3,column=2,padx=30,pady=30)

    vmaxF2 = IntVar()
    entryF12=Entry(fs2,textvariable=vmaxF2,bd=5).grid(row=3,column=3,padx=10,pady=30)
 

    def clickshow():
        try:
            raise_frame(fs6)
            maxval=vmaxF2.get()
            print(maxval)
            search_response = youtube.search().list(part="id,snippet",maxResults=maxval).execute()
            videos = {}
            res=[]
            vres=StringVar()
            res2=[]
            res4=[]

            for search_result in search_response.get("items", []):
                if search_result["id"]["kind"] == "youtube#video":
                    videos[search_result["id"]["videoId"]] = search_result["snippet"]["title"]

            video_ids_list = ','.join(videos.keys())

            video_list_stats = youtube.videos().list(id=video_ids_list,part='id,statistics').execute()

            categ1=[]

            i=0
            for keys,values in videos.items():
                try:
                    res.extend(((str(i+1)+str(". Title : "+values)).translate(non_bmp_map),str("Likes : "+video_list_stats['items'][i]['statistics']['likeCount'])
                           ,str("Dislikes : "+video_list_stats['items'][i]['statistics']['dislikeCount']),
                            str("Views : "+video_list_stats['items'][i]['statistics']['viewCount'])))
                    

                except:
                    res.extend(((str(i+1)+str(". Title : "+values)).translate(non_bmp_map),str("Likes : 0")
                           ,str("Dislikes : 0"),
                            str("Views : "+video_list_stats['items'][i]['statistics']['viewCount'])))
                
                finally:
                    i=i+1

            
            scroll2=Scrollbar(fs6)
            scroll2.grid(row=0,column=0,padx=2,pady=2)

            listing2=Listbox(fs6,yscrollcommand=scroll2.set,width=60,height=45,fg="green")

            for i in range(0,len(res)):
                listing2.insert(END,res[i])
                    
            listing2.grid(row=0,column=0,padx=2,pady=2)
            scroll2.config(command=listing2.yview)

            df1=[]

            i=0

            for keys,values in videos.items():
                categ1.append(keys)
                try:
                    df1.append([values,
                           int(video_list_stats['items'][i]['statistics']['likeCount']),
                           int(video_list_stats['items'][i]['statistics']['viewCount']),
                           int(video_list_stats['items'][i]['statistics']['dislikeCount'])])
                except:
                    df1.append([values,0,int(video_list_stats['items'][i]['statistics']['viewCount']),0])

                i=i+1

            labels=['Title','Likes','Views','Dislikes']

            df=pd.DataFrame.from_records(df1,columns=labels)

            mean1=df['Views'].mean()
            print(mean1)
            mean2=df['Likes'].mean()
            mean3=df['Dislikes'].mean()
            median1=df['Views'].median()
            median2=df['Likes'].median()
            median3=df['Dislikes'].median()

            res3=[]
            res3.append("Mean views : "+str(mean1))
            res3.append("Mean likes : "+str(mean2))
            res3.append("Mean dislikes : "+str(mean3))
            res3.append("Median of views : "+str(median1))
            res3.append("Median of likes : "+str(median2))
            res3.append("Median of dislikes : "+str(median3))

            res4='\n'.join(res3)

            vres2=StringVar()

            MsgF62=Message(fs6,textvariable=vres2,fg="red",relief=RAISED)
            MsgF62.config()
            vres2.set(str(res4))
            print(vres2)
            MsgF62.grid(row=0,column=1,padx=2,pady=2)

            bF23=Button(fs6,text="Main Frame" ,font=("Helvetica", 10),bg="black",fg="white",command=lambda:raise_frame(MainFrame)).place(x=400,y=10)

            labelgui=[]
            textgui=[]

            if(maxval>25):
                for i in range(0,maxval):
                    textgui.append(tk.Label(fs6,bg="azure",text=str(i+1)+". "+str(df['Title'][i]).translate(non_bmp_map),font=("Helvetica",8),fg="black"))
                    textgui[i].place(x=550,y=14*i)
                    labelgui.append(tk.Label(fs6,bg="azure",text="https://www.youtube.com/watch?v="+str(categ1[i]).translate(non_bmp_map),font=("Helvetica",8),fg="blue",cursor="hand2"))
                    labelgui[i].place(x=1000,y=14*i)
                    labelgui[i].bind("<Button-1>", callback)

            else:
                for i in range(0,maxval):
                    textgui.append(tk.Label(fs6,bg="azure",text=str(i+1)+". "+str(df['Title'][i]).translate(non_bmp_map),font=("Helvetica",9),fg="black"))
                    textgui[i].place(x=550,y=25*i)
                    labelgui.append(tk.Label(fs6,bg="azure",text="https://www.youtube.com/watch?v="+str(categ1[i]).translate(non_bmp_map),font=("Helvetica",9),fg="blue",cursor="hand2"))
                    labelgui[i].place(x=1000,y=25*i)
                    labelgui[i].bind("<Button-1>", callback)
    
        except:
            raise_frame(MainFrame) 



    bF21=Button(fs2,text="Show" ,font=("Helvetica", 20),bg="FireBrick",fg="Black",command=clickshow)
    bF21.place(x=400,y=400)
    bF22=Button(fs2,text="Main Frame" ,font=("Helvetica", 10),bg="black",fg="white",command=lambda:raise_frame(MainFrame)).place(x=400,y=500)

    #Compare keywords frame - fs3

    labelF31=Label(fs3,text="Enter first keyword : " ,font=("Helvetica", 20),bg="FireBrick",fg="Black")
    labelF31.grid(row=2,column=2,padx=50,pady=50)

    vkeyF31 = StringVar()
    entryF31=Entry(fs3,textvariable=vkeyF31,bd=5).grid(row=2,column=3,padx=50,pady=50)

    labelF32=Label(fs3,text="Enter second keyword : " ,font=("Helvetica", 20),bg="FireBrick",fg="Black")
    labelF32.grid(row=3,column=2,padx=50,pady=50)

    vkeyF32 = StringVar()
    entryF32=Entry(fs3,textvariable=vkeyF32,bd=5).grid(row=3,column=3,padx=50,pady=50)

    labelF32=Label(fs3,text="Enter number of results : " ,font=("Helvetica", 20),bg="FireBrick",fg="Black")
    labelF32.grid(row=4,column=2,padx=50,pady=50)

    vmaxF3 = IntVar()
    entryF33=Entry(fs3,textvariable=vmaxF3,bd=5).grid(row=4,column=3,padx=50,pady=50)

    
    def compare():
        try:
            youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)
            qval1=vkeyF31.get()
            qval2=vkeyF32.get()
            maxvalc=vmaxF3.get()

            search_response1 = youtube.search().list(q=qval1,part="id,snippet",maxResults=maxvalc).execute()

            videos1 = {}

            for search_result in search_response1.get("items", []):
                if search_result["id"]["kind"] == "youtube#video":
                    videos1[search_result["id"]["videoId"]] = search_result["snippet"]["title"]  

            video_ids_list1 = ','.join(videos1.keys())

            video_list_stats1 = youtube.videos().list(id=video_ids_list1,part='id,statistics').execute()

            df1 = []

            for item in video_list_stats1['items']:
                video_dict1 = dict(video_id = item['id'], video_title = videos1[item['id']])
                video_dict1.update(item['statistics'])
                df1.append(video_dict1)

            df1 = pd.DataFrame.from_dict(df1)


            df1['video_title']=df1['video_title'].astype(str)                               ##code to remove
            non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)         ##unicode error
            df1['video_title']=df1['video_title'].str.translate(non_bmp_map)                ##

            df1['viewCount'].fillna(0, inplace=True)
            df1['likeCount'].fillna(0, inplace=True)
            df1['dislikeCount'].fillna(0, inplace=True)


            df1['viewCount']=df1['viewCount'].astype(int)
            df1['likeCount']=df1['likeCount'].astype(int)
            df1['dislikeCount']=df1['dislikeCount'].astype(int)


            df3=pd.DataFrame({'Mean viewCount': df1['viewCount'].mean(),
                          'Mean likeCount': df1['likeCount'].mean(),
                          'Mean dislikeCount': df1['dislikeCount'].mean()},
                           index=[0])

            search_response2 = youtube.search().list(q=qval2,part="id,snippet",maxResults=maxvalc).execute()

            videos2 = {}

            for search_result in search_response2.get("items", []):
                if search_result["id"]["kind"] == "youtube#video":
                    videos2[search_result["id"]["videoId"]] = search_result["snippet"]["title"]  

            video_ids_list2 = ','.join(videos2.keys())

            video_list_stats2 = youtube.videos().list(id=video_ids_list2,part='id,statistics').execute()


            df2 = []

            for item in video_list_stats2['items']:
                video_dict2 = dict(video_id = item['id'], video_title = videos2[item['id']])
                video_dict2.update(item['statistics'])
                df2.append(video_dict2)

            df2 = pd.DataFrame.from_dict(df2)

            df2['video_title']=df2['video_title'].astype(str)                       ##code to remove
            df2['video_title']=df2['video_title'].str.translate(non_bmp_map)        ##unicode error

            df2['viewCount'].fillna(0, inplace=True)
            df2['likeCount'].fillna(0, inplace=True)
            df2['dislikeCount'].fillna(0, inplace=True)
           
            df2['viewCount']=df2['viewCount'].astype(int)
            df2['likeCount']=df2['likeCount'].astype(int)
            df2['dislikeCount']=df2['dislikeCount'].astype(int)
            
            df4=pd.DataFrame({'Mean viewCount': df2['viewCount'].mean(),
                          'Mean likeCount': df2['likeCount'].mean(),
                          'Mean dislikeCount': df2['dislikeCount'].mean()}, index=[0])

            df3['key']=qval1
            df4['key']=qval2
            df5 = pd.concat([df3,df4],keys=[qval1,qval2])
            compareMeanLikesDislikes=df5[['Mean likeCount','Mean dislikeCount']].plot.bar()
            compareMeanLikesDislikes.set_ylabel('Count')
            compareMeanLikesDislikes.set_title('Comparison of Mean likes and dislikes')
            plt.show()

        except:
            raise_frame(MainFrame)
    bF31=Button(fs3,text="Compare" ,font=("Helvetica", 20),bg="FireBrick",fg="Black",command=compare)
    bF31.place(x=700,y=200)
    bF32=Button(fs3,text="Main Frame" ,font=("Helvetica", 10),bg="black",fg="white",command=lambda:raise_frame(MainFrame)).place(x=720,y=300)


    #Analysis frame-fs4

    def find_category():
        try:
            search_response = youtube.search().list(maxResults=50,part="id,snippet").execute()

            videos = {}

            for search_result in search_response.get("items", []):
                if search_result["id"]["kind"] == "youtube#video":
                    videos[search_result["id"]["videoId"]] = search_result["snippet"]["title"]

            video_ids_list = ','.join(videos.keys())

            categ1=[]
            i=0
            categ2=[]

            for keys,values in videos.items():
                categ1.append(keys)
                i=i+1

            print(categ1)


            x=[None]*50

            for i in range(0,len(categ1)):
                url=urlopen("https://www.youtube.com/watch?v="+categ1[i])
                soup=BeautifulSoup(url,"html.parser")    

                for m in ((soup.find_all(class_="watch-meta-item yt-uix-expander-body")) or (soup.find_all(class_="watch-meta-item"))):
                    for n in m.find_all(class_="title"):
                        #print(n.get_text().strip())
                        if (n.get_text().strip() == "Category"):
                           
                           for k in m.find_all(class_="g-hovercard yt-uix-sessionlink spf-link "):
                               x[i]=k.get_text()
                


            print(x)

            dict1 = {i:x.count(i) for i in x}

            labels=[]
            sizes=[]

            for key,val in dict1.items():
                labels.append(key)
                sizes.append(val)
                if(val == max(dict1.values())):
                        print(key)



            print(labels)
            print(sizes)

            plt.pie(sizes, labels=labels, 
                    autopct='%1.1f%%', shadow=True, startangle=140)
             
            plt.axis('equal')
            plt.title("Categories")
            plt.show()

        except:
            raise_frame(MainFrame)


    def perform_kmeans_clustering():
        try:
            search_response = youtube.search().list(maxResults=50,part="id,snippet").execute()

            videos = {}

            for search_result in search_response.get("items", []):
                if search_result["id"]["kind"] == "youtube#video":
                    videos[search_result["id"]["videoId"]] = search_result["snippet"]["title"]

            video_ids_list = ','.join(videos.keys())

            video_list_stats = youtube.videos().list(id=video_ids_list,part='id,statistics').execute()

            i=0

            df1=[]

            for keys,values in videos.items():
                try:
                    df1.append([values,
                               int(video_list_stats['items'][i]['statistics']['likeCount']),
                               int(video_list_stats['items'][i]['statistics']['viewCount']),
                               int(video_list_stats['items'][i]['statistics']['dislikeCount'])])
                except:
                    df1.append([values,0,int(video_list_stats['items'][i]['statistics']['viewCount']),0])
                               
                i=i+1

            labels=['Title','Likes','Views','Dislikes']


            df=pd.DataFrame.from_records(df1,columns=labels)

            f1=df['Views'].values
            f2=df['Likes'].values
            f3=df['Dislikes'].values

            X=np.matrix(list(zip(f1,f2)))
            kmeans = KMeans(n_clusters=10).fit(X)
            a1=kmeans.labels_

            res1=np.array(['blue','darkviolet','gold','limegreen','black','magenta','cyan','orangered','pink','slategrey'])

            plt.scatter(f1,f2,c=res1[a1],s=50)
            plt.xlabel('Views')
            plt.ylabel('Likes')
            plt.title('Clustering')
            plt.show()

        except:
            raise_frame(MainFrame)
                

    def perform_agglo_clustering():
        try:
            search_response = youtube.search().list(maxResults=50,
            part="id,snippet").execute()

            videos = {}

            for search_result in search_response.get("items", []):
                if search_result["id"]["kind"] == "youtube#video":
                    videos[search_result["id"]["videoId"]] = search_result["snippet"]["title"]

            video_ids_list = ','.join(videos.keys())

            video_list_stats = youtube.videos().list(id=video_ids_list,
                 part='id,statistics').execute()

            i=0

            df1=[]

            for keys,values in videos.items():
                try:
                    df1.append([values,
                              int(video_list_stats['items'][i]['statistics']['likeCount']),
                               int(video_list_stats['items'][i]['statistics']['viewCount']),
                               int(video_list_stats['items'][i]['statistics']['dislikeCount'])])
                               #int(video_list_stats['items'][i]['statistics']['commentCount'])])
                except:
                    df1.append([values,0,int(video_list_stats['items'][i]['statistics']['viewCount']),0])

                i=i+1



            labels=['Title','Likes','Views','Dislikes']
                
            df=pd.DataFrame.from_records(df1,columns=labels)

            f1=df['Views'].values
            f2=df['Likes'].values


            X=np.matrix(list(zip(f1,f2)))
            Hclustering = AgglomerativeClustering(n_clusters=10,affinity='euclidean', linkage='average')
            Hclustering.fit(X)

            a2=Hclustering.labels_

            res1=np.array(['chartreuse','red','yellow','green','black','deeppink','cyan','darkgoldenrod','m','navy'])

            plt.scatter(f1,f2,c=res1[a2],s=50)
            plt.xlabel('Views')
            plt.ylabel('Likes')
            plt.title('Clustering agglomerative')
            plt.show()

        except:
            raise_frame(MainFrame)

except:
    raise_frame(MainFrame)




bF4_1=Button(fs4,text="Kmeans Clustering",width=20,font=("Helvetica", 30),bg="FireBrick",fg="Black",command=perform_kmeans_clustering)
bF4_1.place(x=400,y=50)

bF4_2=Button(fs4,text="Agglomerative Clustering",width=20,font=("Helvetica", 30),bg="FireBrick",fg="Black",command=perform_agglo_clustering)
bF4_2.place(x=400,y=150)

bF4_3=Button(fs4,text="Trending Categories",width=20,font=("Helvetica", 30),bg="FireBrick",fg="Black",command=find_category)
bF4_3.place(x=400,y=250)

bF4_4=Button(fs4,text="Main Frame" ,font=("Helvetica", 10),bg="black",fg="white",command=lambda:raise_frame(MainFrame)).place(x=570,y=350)


root.mainloop()

