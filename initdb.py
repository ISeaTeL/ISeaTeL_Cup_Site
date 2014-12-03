# -*- coding: utf-8 -*-
'''
usage:
type "python manage.py shell"
paste the code in shell
or type "execfile('initdb.py')" in shell
'''
from contest.models import *
from index.models import *

#contest init
contest1 = Contest.objects.filter(cid=1)

if not contest1:
    Contest.objects.create(cid=1,
    	title='ISeaTeL 盃 - 歡樂線上賽] 11/29 選舉當天的愚人節大賽',
    	content='''線上賽從晚上七點整開始，為期三小時，內容有十題
因為很輕鬆，所以可以邊看開票邊寫也沒關係ＸＤ
比賽方式只要連上 <a href="http://acm.cs.nthu.edu.tw/index.php">OJ</a>
點進去 “ISeaTeL 盃 - 歡樂線上賽” 即可
不用到系計中，所以我們也沒有提供食物（請期待之後的實體賽）

友善提醒：
在網頁上頭出現的所有文字都要記得留意喔

因為目前我們的 OJ 的發問功能有點問題
對題目等疑問請在這個網站上發問
我們在比賽間的公告以及回應的部分也都會在這裡噢！！！''',
    	status='<a class="btn btn-primary btn-lg" href="http://140.114.86.238/contest.php?cid=654">Ended</a>',
        problem_url='http://140.114.86.238/contest.php?cid=654', 
        scoreboard_url='http://140.114.86.238/scoreboard.php?cid=654',
        date='11/29')

#bulletin board init
Bulletin.objects.create(
content=
"""線上賽從晚上七點整開始，為期三小時，內容有十題
因為很輕鬆，所以可以邊看開票邊寫也沒關係ＸＤ
比賽方式只要連上 <a href='http://acm.cs.nthu.edu.tw/index.php'>OJ</a>
點進去 “ISeaTeL 盃 - 歡樂線上賽” 即可
不用到系計中，所以我們也沒有提供食物（請期待之後的實體賽）

友善提醒：
在網頁上頭出現的所有文字都要記得留意喔

因為目前我們的 OJ 的發問功能有點問題
對題目等疑問請在這個網站上發問
我們在比賽間的公告以及回應的部分也都會在這裡噢！！！
""",
title=
"""
[ISeaTeL 盃 - 歡樂線上賽 - 賽前通知] 11/29 選舉當天的愚人節大賽
""")


#clarification init
Clarification.objects.create(
cid=1,
asker=
"""
請留下你的 id ，或者使用"匿名"來提問。
""",
question=
"""
請留下您的問題，我們會儘快回覆。
""",
reply=
"""
No reply yet. ===> 表示我們還沒回覆。
"""
)

Clarification.objects.create(
cid=1,
asker=
"""
喔喔喔喔！！！我要搶頭相問問題
""",
question=
"""
ＹＡＹＡＹＡ問問題～～～～
""",
reply=
"""
頭香明明就是樓下
"""
)

Clarification.objects.create(
cid=1,
asker=
"""
Anonymous
""",
question=
"""
請問如果亂問問題會被砍掉嗎?
""",
reply=
"""
因為海帶人很好，所以不會。
"""
)

Clarification.objects.create(
cid=1,
asker=
"""
球狀物體
""",
question=
"""
該不會這是按照updated_time 排的吧ＸＤＤ“
""",
reply=
"""
您太聰明啦，目前已經改好。
"""
)

Clarification.objects.create(
cid=1,
asker=
"""
Anonymous
""",
question=
"""
島風 ～ Meow
""",
reply=
"""
PUSHEEN SAY MEOW~~
"""
)

Clarification.objects.create(
cid=1,
asker=
"""
Anonymous
""",
question=
"""
<script>
alert('gg')
</script>
""",
reply=
"""
我們有擋 javascript 啦ＸＤ
"""
)

Clarification.objects.create(
cid=1,
asker=
"""
copypaste
""",
question=
"""
媽 我竟然過PJ了 感謝海帶 讚嘆海帶
因為寫完PJ太開心 所以我要洗洗睡了 大家要破台啊
""",
reply=
"""
你到底是誰呀？（海帶顯示為好奇狀態）
"""
)

Clarification.objects.create(
cid=1,
asker=
"""
Presidents
""",
question=
"""
米國總統任期超亂的欸
同一任期有兩個當或是當不滿一期的怎麼辦
""",
reply=
"""
取當選的那個人。
"""
)

Clarification.objects.create(
cid=1,
asker=
"""
HYDAI
""",
question=
"""
請各位重新上傳 PD 的程式碼，來驗證說自己的程式有沒有問題。
因為剛才有人問到對任期的定義，目前已經修改有爭議的測資部分。
沒有重新上傳也沒關係，我們賽後會重新 rejudge 各位的 PD 程式碼。
""",
reply=
"""
No reply yet.
"""
)

Clarification.objects.create(
cid=1,
asker=
"""
Not Found
""",
question=
"""
講解一下奇葩的PF吧感謝(>w^)/*
""",
reply=
"""
檢視原始碼就能看到其中的奧秘。
"""
)

Clarification.objects.create(
cid=1,
asker=
"""
admin
""",
question=
"""
QAQ
""",
reply=
"""
資料庫大改，時間錯亂ＱＡＱ
"""
)