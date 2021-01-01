#猜數字遊戲

#產生一個隨機整數 1~100(不要印出來)
#讓使用者重複輸入去猜
#猜對的話 印出 "終於猜對了"
#猜錯的話 要告訴他 答案的大或小


import random #把ramdon這個模組 載入近來我的程式
r = random . randint(1,100)#才能使用這個模組 產生隨機整數(randint)範圍1-100

count = 0 #計數為0 連一次都還沒猜(希望程式一邊猜一邊猜第幾次)
while True: #重複用while (無限走 直到猜對就離開black)
	count = count + 1 #每猜一次 計數+1    也可寫 count += 1 (簡潔法)
	num = input('請輸入數字') #input 一定都是字串喔 設num為變數(使用者輸入)
	num = int(num) #型別轉換-把num原本的字串 轉換成整數 再存回num
	if num == r:#如果使用者的數字跟答案一樣
		print('你猜中了')#猜中就印出
		print('這是你猜的', count, '次')#為了猜中 也要顯示出來
		break #猜中就逃出迴圈 不用再猜了
	elif num > r:#另外如果 num大於正確答案
		print('比答案大')#就印出
	elif num < r:#另外如果 num小於正確答案
		print('比答案小')#就印出
	print('這是你猜的', count, '次') #就印出 此行故意寫在if架構的下一行 不然重複性太高
	    




