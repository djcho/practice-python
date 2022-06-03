cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3])
print(cabinet[100])

#print(cabinet[5]) # 인덱스 참조는 값이 없을 경우 Exception 발생!
# print(cabinet.get(5)) #get 함수를 사용하면 메시지 출력되고 Exception 발생하지 않음, 메지시 변경하고 싶을경우 두번째 파라미터로 설정 가능

cabinet = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

# 새 손님
print(cabinet)
cabinet["A-3"] = "김종국"
cabinet["C-20"] = "조세호"
print(cabinet)

#간 손님
del cabinet["A-3"]
print(cabinet)

# key 들만 출력
print(cabinet.keys())

# value 들만 출력
print(cabinet.values())

# key, value 쌍으로 출력
print(cabinet.items())

# 목욕탕 폐점
cabinet.clear()
print(cabinet)