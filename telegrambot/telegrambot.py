# 1. Xabarni nusxalab yuborish (Muallif nomi ko'rinmaydi)
import requests
token = '8303761346:AAGDkSwQkTmbWug4uKvfb041R4dXClduGFo'
method = 'copyMessage'
response = requests.post(
    url=f'https://api.telegram.org/bot{token}/{method}',
    data={'chat_id': 7365427359, 'from_chat_id': 7365427359, 'message_id': 8}
).json()
print(response)


# 2. Kompyuterdagi rasmni bot orqali yuborish
import requests
token = '8303761346:AAGDkSwQkTmbWug4uKvfb041R4dXClduGFo'
method = 'sendPhoto'
fayl_nomi = 'tp.jpg.png'
response = requests.post(
    url=f'https://api.telegram.org/bot{token}/{method}',
    data={'chat_id': 7365427359, 'caption': 'Bu rasm'},
    files={'photo': open(fayl_nomi, 'rb')}
).json()
print(response)


# 3. Botga kelgan yangi xabarlarni tekshirish va olish
import requests
token = '8303761346:AAGDkSwQkTmbWug4uKvfb041R4dXClduGFo'
method = 'getUpdates'
response = requests.get(url=f'https://api.telegram.org/bot{token}/{method}').json()
print(response)


# 4. Xabar ostida saytga olib boruvchi Inline tugma yuborish
import requests, json
token = '8303761346:AAGDkSwQkTmbWug4uKvfb041R4dXClduGFo'
method = 'sendMessage'
markup = {'inline_keyboard': [[{'text': 'Sayt', 'url': 'https://google.com'}]]}
response = requests.post(
    url=f'https://api.telegram.org/bot{token}/{method}',
    data={'chat_id': 7365427359, 'text': 'Tugma:', 'reply_markup': json.dumps(markup)}
).json()
print(response)


# 5. Yuborilgan xabarni message_id orqali o'chirib tashlash
import requests
token = '8303761346:AAGDkSwQkTmbWug4uKvfb041R4dXClduGFo'
method = 'deleteMessage'
response = requests.post(
    url=f'https://api.telegram.org/bot{token}/{method}',
    data={'chat_id': 7365427359, 'message_id': 8}
).json()
print(response)


# 6. Botda "typing..." (yozmoqda) holatini ko'rsatish
import requests
token = '8303761346:AAGDkSwQkTmbWug4uKvfb041R4dXClduGFo'
method = 'sendChatAction'
response = requests.post(
    url=f'https://api.telegram.org/bot{token}/{method}',
    data={'chat_id': 7365427359, 'action': 'typing'}
).json()
print(response)


# 7. Xaritadan aniq manzil (lokatsiya) yuborish
import requests
token = '8303761346:AAGDkSwQkTmbWug4uKvfb041R4dXClduGFo'
method = 'sendLocation'
response = requests.post(
    url=f'https://api.telegram.org/bot{token}/{method}',
    data={'chat_id': 7365427359, 'latitude': 41.3111, 'longitude': 69.2401}
).json()
print(response)


# 8. Istalgan turdagi faylni hujjat ko'rinishida yuborish
import requests
token = '8303761346:AAGDkSwQkTmbWug4uKvfb041R4dXClduGFo'
method = 'sendDocument'
response = requests.post(
    url=f'https://api.telegram.org/bot{token}/{method}',
    data={'chat_id': 7365427359},
    files={'document': open('sample-database.db', 'rb')}
).json()
print(response)


# 9. Xabarni boshqa chatga "Forward" (yo'naltirish) qilish
import requests
token = '8303761346:AAGDkSwQkTmbWug4uKvfb041R4dXClduGFo'
method = 'forwardMessage'
response = requests.post(
    url=f'https://api.telegram.org/bot{token}/{method}',
    data={'chat_id': 7365427359, 'from_chat_id': 7365427359, 'message_id': 22}
).json()
print(response)


# 10. Botning o'zi haqidagi ma'lumotlarni tekshirish
import requests
token = '8303761346:AAGDkSwQkTmbWug4uKvfb041R4dXClduGFo'
method = 'getMe'
response = requests.get(url=f'https://api.telegram.org/bot{token}/{method}').json()
print(response)