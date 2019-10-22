import socket
from concurrent.futures import ThreadPoolExecutor
from tkinter import *
import tkinter.font as tkFont

root = Tk()
root.title('PortScan')
root.geometry('700x400')
root.iconbitmap('.\scan72.ico')
ft1 = tkFont.Font(size=10, weight=tkFont.BOLD)
ft2 = tkFont.Font(family='Fixdsys', size=15, weight=tkFont.BOLD)
ft3 = tkFont.Font(family='Fixdsys', size=30, weight=tkFont.BOLD)


def ftp_theadpool(func, ip, fn, mixport, maxport):
    pool = ThreadPoolExecutor(200)
    for port in range(int(mixport), int(maxport) + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        pool.submit(func, ip, port, s, fn)
    pool.shutdown()


def jiance(ip, port, s, fn):
    try:
        s.settimeout(2)
        s.connect((ip, port))
        fn.write('port %s: OPEN\n' % port)
        print('port %s: OPEN' % port)
    except:
        fn.write('port %s: CLOSE\n' % port)
        print('port %s: CLOSE' % port)


def start():
    ip = hostip.get()
    mixport = s_port.get()
    maxport = e_port.get()
    try:
        a = '-' * 60
        b = '%s端口扫描结果' % ip
        c = '-' * 60
        fn = open('./端口扫描结果.txt', 'w+', encoding='utf-8')
        fn.write(a + '\n' + b + '\n' + c + '\n')
        ftp_theadpool(jiance, ip, fn, mixport, maxport)
        info['text'] = '扫描成功'
    except:
        info['text'] = '请检测输入内容'


def dele():
    hostip.delete(0, END)
    s_port.delete(0, END)
    e_port.delete(0, END)
    info['text'] = ''

message = Label(root, text='端口扫描工具端口（1-65535）', font=ft1).grid()
message2 = Label(root, text='请在英文输入法下进行输入', font=ft1).grid()
ip = Label(root, text='IP地址：', font=ft3)
ip.grid(row=2, sticky=W)
hostip = Entry(root, font=ft3)
hostip.grid(row=2, column=1, sticky=W)
message3 = Label(root, text='', font=ft1).grid()
start_port = Label(root, text='开始端口：', font=ft3)
start_port.grid(row=4, sticky=W)
s_port = Entry(root, font=ft3)
s_port.grid(row=4, column=1, sticky=E)
message4 = Label(root, text='', font=ft1).grid()
end_port = Label(root, text='结束端口：', font=ft3)
end_port.grid(row=6, sticky=W)
e_port = Entry(root, font=ft3)
e_port.grid(row=6, column=1, sticky=E)
message5 = Label(root, text='', font=ft1).grid()
theButton1 = Button(root, text="开始扫描", width=10, command=start, font=ft2)
theButton2 = Button(root, text="清除", width=10, command=dele, font=ft2)
theButton1.grid(row=8, column=0, padx=10, pady=5)
theButton2.grid(row=8, column=1, sticky=E, padx=10, pady=5)
message6 = Label(root, text='', font=ft1).grid()
info = Label(root, text='', font=ft1)
info.grid(row=10, column=0,)

root.mainloop()
