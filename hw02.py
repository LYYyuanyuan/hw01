import re

from date import area
 
def idcard(ID):
    if (re.match(r"\d{17}",ID)):

        if ID[:6] in area.keys():
            print("出生地区:" + area[ID[:6]]) 
        
        else:
            print("非法地区")
        
        #检验地区

        if (int (ID[6:10]) % 4 == 0  or(int (ID[6:10]) % 100 == 0  and int (ID[6:10]) % 4 == 0 )):

            pattern = re.compile('[1-9][0-9]{5}19[0-9]{2}((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1])|(04|06|09|11)(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|[1-2][0-9]))[0-9]{3}[0-9Xx]$')                    
        #闰年
        else:
            
            pattern = re.compile('[1-9][0-9]{5}19[0-9]{2}((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1])|(04|06|09|11)(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|1[0-9]|2[0-8]))[0-9]{3}[0-9Xx]$')  
        #平年

        if(re.match(pattern,ID)):

            print ("出生日期:" + ID[6:10] +"年" +ID[10:12] + "月"+ ID[12:14]+ "日") 

        else:

            print("非法日期")
        #验证并识别出生日期
      
        if  int(ID[14:16]) % 2 == 1:

            print("性别：男")      
        else:
            print("性别：女")
        #验证并识别男女
    last = ID[17]
    print("最后一位: ", last)
      
    QZ = [7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
    JYM = ['1','0','X','9','8','7','6','5','4','3','2']
    sum = 0
    m = 1
    for i in range(0,17) :
        if m < 18:
                sum += int(ID[i])* QZ[i] 
                m +=1
    y = sum % 11
    print("余数:",y)

    if JYM[y] == last :
        print("校验码正确")
    else:
        print("校验码错误")
    #检验身份证最后一位是否合法        
def ID():
    ID = input('请输入十八位身份证号码: ')
    if len(ID) == 18:
        print("你的身份证号码是 " +ID)
    else:
        print("错误的身份证号码")
    
    idcard(ID)
#检验身份证号是否为18位  
      



