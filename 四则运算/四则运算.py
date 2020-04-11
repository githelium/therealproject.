import random #引入math模块
import time


today = time.strftime('%Y-%m-%d',time.localtime(time.time()))
text = './Logs/' + today + '.log'
def log(write,arg = ''):
    with open(text, 'a') as f:
        log = '<' + time.strftime('%H:%M:%S',time.localtime(time.time())) + '>' + write + arg + '\n'
        f.write(log)


title = '\n\nstarting:' + today + '\n'
with open(text, 'a') as f:
    f.write(title)


score = 0
log('[info]Set score to 0.')
log('[info]score:',str(score))


def generexp(time = 1):#定义函数
    log('[info]generite start.')
    thinglist = ['+', '-', '*', '/']
    for i in range(0,time):
        #生成算式
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
            log('>>',str(a) + thinglist[thing - 1] + str(b) + '=')
            print(str(a),thinglist[thing - 1],str(b),end = '=')
            try:
                userath = input()
                log('<<',userath)
                try:
                    truefause = int(userath) == ath#此处truefause为bool类型
                    break#跳出死循环
                except ValueError:#若转换不成功（输入非数字）
                    if userath == 'exit':
                        log('exit with code 0.')
                        exit(0)
                    else:
                        print('请输入一个数字！')
                        log('>>请输入一个数字！')
                        continue#进入下一轮循环
            except KeyboardInterrupt:
                print('退出原因：用户以关键字自行退出。')
                log('exit with code -1.')
                exit(-1)
            except EOFError:
                print('退出原因：不期望的文件尾。（Ctrl+z）')
                log('exit with code -2.')
                exit(-2)
            except:
                print('退出原因：发生了一个未捕获的错误。')
                log('[ERROR]UNKNOWN ERROR.')
                raise
        if truefause:#判断：
            #正确
            print('正确!')
            log('>>正确!')
            global score
            score = score + 1
        else:
            #错误
            print('错误！')
            log('>>错误！')
        #询问用户算式数量


print('你想要多少个算式？')
log('>>你想要多少个算式？')
while 1==1:#死循环
    try:
        inputtimes = input()
        log('<<',inputtimes)
        try:
            times = int(inputtimes)#赋值并类型转换
            log('times:',str(times))
            break#跳出死循环
        except ValueError:#若转换不成功（输入非数字）
            if inputtimes == 'exit':
                log('exit with code 0.')
                exit(0)
            else:
                print('请输入数字！')#告知用户
                continue#进入下一轮循环
    except KeyboardInterrupt:
        print('退出原因：用户以关键字自行退出。')
        time.sleep(3)
        log('exit with code -1.')
        exit(-1)
    except EOFError:
        print('退出原因：不期望的文件尾。（Ctrl+z）')
        log('exit with code -2.')
        time.sleep(3)
        exit(-2)
    except:
        print('退出原因：发生了一个未捕获的错误。')
        log('[ERROR]UNKNOWN ERROR.')
        time.sleep(3)
        raise


log(str(times))
generexp(times)#引用函数

print('分数:',str(score),'/',str(times))
log('>>分数:'+ str(score)+'/'+str(times))

if score == 0:
    print('百分制:0分')
    log('>>百分制:0分')
else:
    print('百分制:' + str(int((score / times) * 100)))
    log('>>百分制:' + str(int((score / times) * 100)))

time.sleep(3)
log('all numbers:')
log('today:' + today)
log('text:' + text)
log('score:' + str(score))
