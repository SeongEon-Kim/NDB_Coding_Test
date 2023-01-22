n = 1260
count = 0

# 큰 단위의 화폐부터 차례대로 확인하기
coin_types = [500, 100, 50, 10]

for coin in coin_types: 
    # count += n // coin # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기, 할당 연산자 표현
    # a / b : 일반 나누기
    # a // b : 몫
    # a % b : 나머지 
    
    # 화폐의 종류 K라면 시간 복잡도는 O(K)이다
    count = count + n // coin 
    n %= coin

print(count)
 