password = 'a123456'
i = 3 # 剩下機會
while True :
    word = input('請輸入密碼: ')
    if word == password:
        print('登入成功!')
        break # 不再發問
    else :
        i = i - 1
        print('密碼錯誤!還有' , i, '次機會')
        if i == 0 :
        	break
