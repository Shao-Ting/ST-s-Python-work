# coding: utf-8
words='''
人生長至一世、短如一瞬
寰宇浩瀚無際，此生飄渺無歸
旅途上，我們將會遇到許多
或許喜悅、或許傷悲、或許歡喧、或許靜寧
請記得哭過、笑過，要繼續活下去
真正重要的到底是什麼
我們似乎都在追求著什麼
最後才發現
握緊手心，裡面什麼都沒有
一呼一吸
花開花落
追日、探月、索星、尋夢、逐塵
無論他人怎麼說，我們都是獨一無二的我們
紛紛擾擾的一生中
或許只有自己明白
或許自己也不明白'''
words.split('\n')
phrase=words.split('\n')
p=randint(2,7)
for i in range(p):
    pp=randint(1,3)
    egg=(choice(phrase,pp))
    ham=','.join(egg)
    print(ham)
