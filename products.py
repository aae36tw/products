products = []
while True:
    name = input('請輸入商品名稱:')
    if name == 'q':  # quit
        break
    price = input('請輸入商品價格:')
    # p = []  # 建立小清單
    # p.append(name)
    # p.append(price)
    # p = [name, price] 將上述三行濃縮成一行，或是直接放在p裡面
    products.append([name, price])
print(products)

for p in products:
    print(p[0], '的價格是', p[1])
