메뉴이름 = ["팥붕어빵", "슈크림붕어빵", "초코붕어빵", "피자붕어빵"]
가격 = [800, 1000, 1000, 1500]
재고 = [5, 5, 5, 5]

def menu():
    print("\n🍞 메뉴 🍞")
    for i in range(len(메뉴이름)):
        print(f"{i+1}. {메뉴이름[i]} ({가격[i]}원) - 재고: {재고[i]}개")
        
def order():
    menu()
    주문내역 = []
    총금액 = 0
    
    while True:
        try:
            번호 = int(input("\n주문할 메뉴 번호 (종료는 0): "))
            if 번호 == 0:
                break
            번호 -= 1
            if 번호 < 0 or 번호 >= len(메뉴이름):
                print("❌ 없는 번호예요.")
                continue
            수량 = int(input(f"{메뉴이름[번호]} 몇 개 주문하시겠습니까?: "))
            if 수량 > 재고[번호]:
                print(f"❌ 재고가 부족합니다! {재고[번호]}개 남았습니다.")
                continue
            금액 = 수량 * 가격[번호]
            재고[번호] -= 수량
            총금액 += 금액
            주문내역.append((메뉴이름[번호], 수량, 금액))
            print(f"✅ {메뉴이름[번호]} {수량}개 주문 완료되었습니다.")
        except:
            print("❌ 숫자만 입력해주세요.")
            
    if 주문내역:
        print("\n🧾 고객 영수증")
        for 이름, 수량, 금액 in 주문내역:
            print(f"-{이름} x {수량} = {금액}원")
        print(f"총 합계: {총금액}원")
        
        print("\n📦 가게 재고 현황")
        for i in range(len(메뉴이름)):
            print(f"{메뉴이름[i]}: {재고[i]}개 남음")
    else:
        print("주문이 없습니다.")    
        
def restock():
    menu()
    try:
        번호 = int(input("\n추가할 메뉴 번호: ")) - 1
        수량 = int(input("몇 개 추가할까요?: "))
        재고[번호] += 수량
        print(f"✅ {메뉴이름[번호]} 재고: {재고[번호]}개")
    except:
        print("❌ 숫자만 입력하세요.")

def start():
    print("🧇 붕어빵 키오스크 🧇")
    while True:
        print("\n[1] 주문 [2] 재고채우기 [3] 종료")
        선택 = input("번호 입력: ")
        if 선택 == "1":
            order()
        elif 선택 == "2":
            restock()
        elif 선택 == "3":
            print("👋 종료합니다.")
            break
        else:
            print("❌ 잘못된 선택입니다!")
                      
start()