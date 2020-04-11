import random
import time
import tkinter as tk
window = tk.Tk()
window.title('my window')
window.geometry('500x200')
var = tk.StringVar()
l = tk.Label(window, textvariable=var,font=('Arial', 12), width=105, height=2)
l.pack()
e = tk.Entry(window,show=None)
e.pack()
ishit = False
def hit():
    global ishit
    if ishit == False:
        ishit = True
        time.sleep(0.15)
b = tk.Button(window, text='确认',width=15, height=2, command=hit)
b.pack()
def guiinput():
    global ishit
    while True:
        time.sleep(0.1)
        if ishit == True:
            ishit = False
            return e.get()
        else:# 从 True 状态变成 False 状态
            continue
        break
def log(write,arg = ''):
    with open('./log-.txt', 'a') as f:
        log = '<' + time.strftime('%H:%M:%S',time.localtime(time.time())) + '>' + write + arg + '\n'
        f.write(log)
title = '\n\nstarting:' + time.strftime('%Y-%m-%d',time.localtime(time.time())) + '\n'
with open('./log-.txt', 'a') as f:
    f.write(title)
score = 0
log('[info]Set score to 0.')
log('[info]score:',str(score))
def generexp(time = 1):#定义函数
    log('[info]generite start.')
    thinglist = ['+', '-', '*', '/']
    for i in range(0,time):
        #生成算式
        global var
        log('randoming.')
        thing = random.randint(1,4)#随机选择计算类型
        log('[info]thing:',str(thing))
        if thing == 1:#若加
            #+ 加生成a和b两个数
            a = random.randint(1,1000)
            log('[info]a:',str(a))
            b = random.randint(1,1000)
            log('[info]b:',str(b))
            ath = a + b
            log('[info]ath:',str(ath))
        elif thing == 2:#若减
            #- 减生成a和b两个数
            a = random.randint(100,1000)
            log('[info]a:',str(a))
            b = random.randint(1,a)
            log('[info]b:',str(b))
            ath = a - b
            log('[info]ath:',str(ath))
        elif thing == 3:#若乘
        #* 乘生成a和b两个数
            a = random.randint(11,100)
            log('[info]a:',str(a))
            b = random.randint(1,9)
            log('[info]b:',str(b))
            ath = a * b
            log('[info]ath:',str(ath))
        else:#若除
            #/ 除生成a和b两个数
            b = random.randint(1,9)
            log('[info]b:',str(b))
            n = random.randint(11,100)
            log('[info]n:',str(n))
            a = b * n
            log('[info]a:',str(a))
            ath = a / b
            log('[info]ath:',str(ath))
        while 1==1:#死循环
            #取得用户输入
            global var
            log('>>',str(a) + thinglist[thing - 1] + str(b) + '=')
            var.set(str(a) + thinglist[thing - 1] + str(b))
            userath = guiinput()
            log('<<',userath)
            try:
                truefause = int(userath) == ath#此处truefause为bool类型
                break#跳出死循环
            except ValueError:#若转换不成功（输入非数字）
                if userath == 'exit':
                    log('exit with code 0.')
                    exit(0)
                else:
                    var.set('请输入一个数字！')
                    log('>>请输入一个数字！')
                    continue#进入下一轮循环
        #判断：
        if truefause:
            #正确
            var.set('正确!')
            log('>>正确!')
            global score
            score = score + 1
            time.sleep(2)
        else:
            #错误
            var.set('错误！')
            log('>>错误！')
            time.sleep(2)
generexp()
