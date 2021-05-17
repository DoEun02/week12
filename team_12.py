from selenium import webdriver
import matplotlib.pyplot as plt

print("궁금한 이름들을 작성하십시오.(,로 구분해주세요.)")
print("ex : 민준, 서윤, 서준, 서연")

string=input(">> : ")
list=string.split(",")

name_list = []
for i in list:
    s = i.strip()
    name_list.append(s)

x_list = range(len(list))

URL = 'https://baby-name.kr/search/%EC%9D%B4%EB%A6%84/'
driver = webdriver.Chrome(executable_path='./chromedriver.exe')#, options=options)
driver.get(url=URL)
name_number = []

for name in name_list:
    search_box = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/div[1]/div/input')
    search_box.clear()

    search_box = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/div[1]/div/input')
    search_box.send_keys(name)

    search_btn = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/div[1]/div/div')
    search_btn.click()

    result = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/div[2]/em[2]').text
    if len(result) == 6:
        result = int(result[0]) * 1000 + int(result[2:5])
    elif len(result) == 4:
        result = int(result[0:3])
    elif len(result) == 7:
        result = int(result[0:2]) * 1000 + int(result[3:6])
    elif len(result) == 3:
        result = int(result[0:2])
    elif len(result) == 2:
        result = int(result[0:1])

    man = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/div[2]/em[3]').text
    woman = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/div[2]/em[4]').text

    name_number.append(result)
    print(name)
    print('->' + '남자 : ' + man + ' ' + '여자 : ' + woman)

driver.close()

plt.rc('font', family='Malgun Gothic')
plt.bar(x_list,name_number)
plt.title('같은 이름을 가진 사람 수')
plt.ylabel('사람 수')
plt.xlabel('이름')
plt.xticks(x_list,name_list)
plt.show()