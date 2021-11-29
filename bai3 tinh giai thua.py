x = int(input("Nhập số cần tính giai thừa:"))
def giaithua(x):
    if (x < 0):
        x = int(input("Nhập lại, x là số dương:"))
    if x == 0:
        return 1
    return x * giaithua(x - 1)
print ("Giai thua la", giaithua(x))