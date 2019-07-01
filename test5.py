import telegram

chii_tojen = '123456789:ABCDEFGHIJKLMNOPQRST'
chii = telegram.Bot(token = chii_token)
updates = chii .getUpdates()
for u in updates:
    print(u.message)