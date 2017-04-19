#!/usr/bin/python
#encoding=utf-8
'''
聊天语聊的预处理
@author: dyx
2017年4月19日
'''
import os

def dialogs2dia(inputfile,outputfile):
    f_r = open(inputfile)
    f_w = open(outputfile, 'w')
    count = 0
    while 1:
        try:
            temp = f_r.readline()
        except:
            continue
        if not temp:
            break
        count += 1

        dialogues = temp.strip().split("\t")
        flag_p = 0
        flag_d = 0
        for i in dialogues:
            try:
                identity = i.strip(" ")[0]
            except:
                print i
            if len(i) > 4:
                if identity == "p":
                    flag_d = 0
                    flag_p += 1
                    if flag_p == 1:
                        f_w.write("\n" + i)
                    elif flag_p > 0:
                        f_w.write(i[4:])

                if identity == "d":
                    flag_p = 0
                    flag_d += 1
                    if flag_d == 1:
                        f_w.write("\t" + i)
                    elif flag_d > 1:
                        f_w.write(i[4:])

            else:
                continue

        f_w.write("\n")
