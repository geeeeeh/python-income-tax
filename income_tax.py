# 변수 선언
income = 20000  # 소득 (만원 단위 예시)
tax = 0         # 초기값

# 조건문으로 소득 수준 분류
if income >= 10000:
    tax = income * 0.3
    level = "고소득층"
elif income >= 5000:
    tax = income * 0.2
    level = "중간소득층"
else:
    tax = income * 0.1
    level = "저소득층"

# 결과 출력
print(f"소득: {income}만원")
print(f"소득 수준: {level}")
print(f"세금: {tax:.1f}만원")
