sentence = '나는 소년입니다.'
print(sentence)

sentence2 = "파이썬은 쉬워요"
print(sentence2)

sentence3 = """
나는 소년이고, 
파이썬은 쉬워요
"""

print(sentence3)

python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python", "Java"))

index = python.index("n")
print(index)
index = python.index("n", index + 1)
print(index)

print(python.find("Java"))
#print(python.index("Java"))

print(python.count("n"))


## string format
print("나는 %d살입니다." % 20) 
print("나는 %s을 좋아해요" % "파이썬")
print("Apple 은 %c로 시작해요" % "A")

# %s
print("나는 %s살입니다." % 20) 
print("나는 %s색과 %s색을 좋아해요" %("파란", "빨강"))

print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요".format("파란", "빨강"))
print("나는 {0}색과 {1}색을 좋아해요".format("파란", "빨강"))
print("나는 {1}색과 {0}색을 좋아해요".format("파란", "빨강"))

print("나는 {age}살이며, {color}색을 좋아해요".format(age = 20, color = "빨간"))
print("나는 {age}살이며, {color}색을 좋아해요".format(color = "빨간", age = 20))

# v3.6이상
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요")