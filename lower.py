ticker = "BTC_KRW"
newticker = ticker.lower()

print(newticker)

string = "hello"

newstring = string.capitalize()
print(newstring)

file_name = "보고서.xlsx"
#문자열이 지정 문자열로 끝나는지 체크. 
#범위 정해 문자열 중간 부분 체크 가능.
#대소문자 체크.
#ex) string.endswith(value, start, end)
newfile_name = file_name.endswith('xlsx')
print(newfile_name)

file_name2 = "2020_보고서.xlsx"
newfile_name2 = file_name2.startswith('2020')
print(newfile_name2)