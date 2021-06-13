class Dessert:
    # 생성자
    def __init__ (self, name, price):
        self.name = name
        self.price = price

    # 메서드
    def eat(self):
        print("맛있게 드세요!")

    def eat2(self):
        print("오늘도 냠냠")

dessert1 = Dessert("브라우니","4500")
dessert2 = Dessert("크로플", "6500")


# 필드 값 출력
print(dessert1.name+"의 가격은", dessert1.price+"원 입니다.")
dessert1.eat()

print(dessert2.name+"의 가격은", dessert2.price+"원 입니다.")
dessert2.eat2()

# 문자열 길이를 나타내는 내장함수 len사용
print("dessert1의 필드 name 길이 :",len(dessert1.name))
print("dessert2의 필드 name 길이 :",len(dessert2.name))