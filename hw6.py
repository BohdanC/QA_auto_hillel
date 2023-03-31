import requests

url = 'https://script.google.com/macros/s/AKfycbxwW0F_JY96DdEafbrhTXnJZZrpb0ab04HZr3PyvAGl3XWXiPPetRS0i4qy9z-OdNt-/exec'

response = requests.get(url)
our_goods = response.json()

goods = our_goods.get('goods', [])

goods_quantity = [good.get('quantity', 0) * float(good.get('price', 0)) for good in goods]
print(f'Загальна ціна всіх товарів: {round(sum(goods_quantity),2)}')
non_glut_goods_quantity = [good.get('quantity', 0) * float(good.get('price', 0)) for good in goods \
                           if good.get('gluten') == False]

print(f'Загальна ціна безглютенових товарів: {round(sum(non_glut_goods_quantity),2)}')