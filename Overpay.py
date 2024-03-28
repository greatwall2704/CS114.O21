import re
def take_percentage_lower(text):
    match_lower = re.search(r"\d+\.?\d*% lower than in-store", text)
    if match_lower:
        return float(match_lower.group().strip("% lower than in-store"))
    return 0
def take_percentage_higher(text):
    match_higher = re.search(r"\d+\.?\d*% higher than in-store", text)
    if match_higher:
        return float(match_higher.group().strip("% higher than in-store"))
    return 0

def can_buy_all(prices, notices, money):
    in_store_price = 0
    online_price = 0
    for i in range(len(notices)):
        if 'lower than in-store' in notices[i]:
            percentage = take_percentage_lower(notices[i])
            online_price += prices[i] - (prices[i] / 100 * percentage)
        if 'higher than in-store' in notices[i]:
            percentage = take_percentage_higher(notices[i])
            online_price += prices[i] + (prices[i] / 100 * percentage)
        in_store_price += prices[i]
        if money >= online_price or money >= in_store_price:
            continue
        else:
            return False
    return True

notices = []
prices = list(map(int, input().split()))
n = int(len(prices))

for _ in range(n):
    notices.append(input())

money = int(input())

result = can_buy_all(prices, notices, money)

if result:
    print("true")
else:
    print("false")