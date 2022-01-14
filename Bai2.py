# Bai 2
def totalDigitsOfNumber(n):
    total = 0
    while (n > 0):
        total = total + n % 10
        n = int(n / 10)
    return total

# Câu a
input("Nhập tên đệm và tên của mình: ")

# Câu b
n = int(input("Nhập n bằng độ dài tên của mình và tên đệm: n = "))
print("Tổng các chữ số của", n, "là","=" , totalDigitsOfNumber(n))
