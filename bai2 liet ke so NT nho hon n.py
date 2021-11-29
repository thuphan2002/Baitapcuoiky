def check_prime_number(n):
    # flag = 0 => không phải số nguyên tố
    # flag = 1 => số nguyên tố
    flag = 1;
    if (n < 2):
        flag = 0
        return flag

    for p in range(2, n):
        if n % p == 0:
            flag = 0
            break
    return flag


n = int(input("Nhap mot so n: "))
for i in range(n):
    check = check_prime_number(i)
    if (check == 1):
        print(i)