# Bai 3

def SoThuanNghich(n):
    str1 = str(n)
    str2 = str1[::-1]
    if (str1 == str2):
        return True # số thuận nghịch
    else:
        return False # không là số thuận nghịch

# Cau a
input('Nhập đầy đủ họ tên của mình: ')

# Cau b
n = int(input("Nhập n bằng số lượng họ ,tên đệm ,tên của mình: n = "))
print("Tổng các chữ số của", n, "là","=", SoThuanNghich(n))
