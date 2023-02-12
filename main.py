from moviepy.editor import *
from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
import datetime
video = ""
watermark = ""


def loadVideo():
    global video
    name_video = askopenfilename()
    if name_video:
        t1.delete(0.0, END)
        t1.insert(0.0, name_video)
    video = name_video

def loadWatermark():
    global watermark
    name_logo = askopenfilename()
    if name_logo:
        t2.delete(0.0, END)
        t2.insert(0.0, name_logo)
    watermark = name_logo

def create_new_video():
    try:
        date_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        video1 = VideoFileClip(video)
        logo = (ImageClip(watermark).set_duration(video1.duration).resize(height=100).set_pos(('left', 'bottom')))
        final = CompositeVideoClip([video1, logo])
        final.write_videofile(f'video_{date_time}.mp4', audio=True)
        showinfo(title='Done', message=f'new video created with the name "video_{date_time}.mp4"')
    except:
        showerror(title='Error', message='You may have entered incorrect data')


page = Tk()
page.geometry('800x200')
l1 = Label(text='Video:')
l1.grid(row=0, column=0, padx=5)
t1 = Text(width=50, height=1)
t1.grid(row=0, column=1, padx=10)
b1 = Button(text='Open', command=loadVideo, width=40)
b1.grid(row=0, column=2, padx=20)

l2 = Label(text='Watermark:')
l2.grid(row=1, column=0, padx=5, pady=10)
t2 = Text(width=50, height=1)
t2.grid(row=1, column=1, padx=10, pady=10)
b2 = Button(text='Open', command=loadWatermark, width=40)
b2.grid(row=1, column=2, padx=20, pady=10)

b3 = Button(text='Create Video', command=create_new_video, width=50)
b3.grid(row=2, column=1, columnspan=2)


page.mainloop()