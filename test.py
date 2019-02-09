import os,shutil
import tkinter as tk
from tkinter.filedialog import askdirectory
import getpass

def start():
    usr=getpass.getuser()
    dst="C:\\Users\\"+usr+"\\AppData\\Local\\Packages\\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\\LocalState\\Assets"
    dir=dir_path_tmp.get() #要保存的文件夹
    folder = os.path.exists(dir)
    if not folder:
        os.makedirs(dir)
    for root,dirs,files in os.walk(dst):
        for f in files:
            if (os.path.getsize(dst+"\\"+f) > 204800): #挑选出大于200KB的图片
                shutil.copyfile(dst+"\\"+f,dir+"\\"+f+".jpg")
    b.configure(text="完成",state="disable") #按钮状态修改

def dir_path_choose():
    path = askdirectory()
    dir_path_tmp.set(path)

root = tk.Tk()
root.title('Win10锁屏壁纸保存')
root.geometry('600x300')
root.resizable(width = False, height = False) #界面大小固定

dir_path_tmp = tk.StringVar()
dir_path_tmp.set("C:/Pics")
path_label = tk.Label(root, text = '请选择存储位置:', font = ('Arial',12), width = 30, height = 2)
path_label.place(x=8, y=80)
tk.Entry(root, textvariable = dir_path_tmp, show = None).place(x=300,y=92)
path_button = tk.Button(root, text = '...', width = 3, height = 1, command = dir_path_choose)
path_button.place(x=500, y=87)

b = tk.Button(root, text = '开始', width = 20, height = 2, command = start)
b.place(x = 230, y = 180)

root.mainloop()
