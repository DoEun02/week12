from selenium import webdriver

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

    man = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/div[2]/em[3]').text
    woman = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/div[2]/em[4]').text

    print(name)
    print('->' + '남자 : ' + man + ' ' + '여자 : ' + woman)