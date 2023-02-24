password = 'a123456'
i = 3
while True :
	p = input ('請輸入密碼:')
	if p == password:
		print ('登入成功!')
		break
	else :
		i = i - 1
		print ('密碼錯誤! 還剩' , i ,'次機會' )
		if i == 0 :
			break
			print ('無法登入')