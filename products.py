import os  # operating system

# 讀取檔案,用splict切割檔案(結果為清單),strip拿掉換行符號


def read_file(filename):
    products = []
    with open(filename, 'r') as f:
        for line in f:
            if '商品,價格' in line:
                # continue和break只能寫在迴圈，continue是跳到下一迴的意思
                continue  # 繼續
            name, price = line.strip().split(',')
            products.append([name, price])
    return products

# 讓使用者輸入


def user_input(products):
    while True:
        name = input('請輸入商品名稱:')
        if name == 'q':  # quit
            break
        price = input('請輸入商品價格:')
        price = int(price)
        # p = []  # 建立小清單
        # p.append(name)
        # p.append(price)
        # p = [name, price] 將上述三行濃縮成一行，或是直接放在p裡面
        products.append([name, price])
    print(products)
    return products

# 印出所有購買紀錄


def print_products(products):
    for p in products:
        print(p[0], '的價格是', p[1])

# 寫入檔案
# read(r)為讀取模式，write(w)為寫入模式


def write_file(filename, products):

    with open(filename, 'w') as f:
        f.write('商品,價格\n')
        for p in products:
            f.write(p[0] + ',' + str(p[1]) + '\n')


def main():
    filename = 'products.csv'
    if os.path.isfile(filename):  # 檢查檔案是否存在
        print('Yes，找到檔案')
        products = read_file(filename)
    else:
        print('No,找不到檔案')

    products = user_input(products)
    print_products(products)
    write_file('products.csv', products)


main()
