import random
import time
print("THIS IS NOT AN OSINT TOOL. THIS IS A FUN TOOL, SO USE IT PROPERLY!")
time.sleep(5)
colors = ["\033[91m", "\033[94m", "\033[96m", "\033[93m", "\033[95m", "\033[35m"]
color = random.choice(colors)
huge_text = """
░█▀▀█ ░█─░█ ░█▀▀▀█ ░█▄─░█ ░█▀▀▀ ░█▀▀▀ ░█▀▀█ ▄█─ ░█▀▀▀█ ▀▄░▄▀ 
░█▄▄█ ░█▀▀█ ░█──░█ ░█░█░█ ░█▀▀▀ ░█▀▀▀ ░█▄▄▀ ─█─ ─▄▄▄▀▀ ─░█── 
░█─── ░█─░█ ░█▄▄▄█ ░█──▀█ ░█▄▄▄ ░█─── ░█─░█ ▄█▄ ░█▄▄▄█ ▄▀░▀▄
                        My tiktok: @fr1zxxpython
                        My telegram: @Fr1zxX
                        My github: https://github.com/Fr1zx
"""
print(color + huge_text)
print("Write full number with + for example: (+380111111)")
time.sleep(3)
phone_number = input("Target phone number: ")
print("The search has begun....")
time.sleep(5)
cleaned_phone_number = ''.join(filter(str.isdigit, phone_number))
if cleaned_phone_number.startswith("370"):
    country = "Lithuania"
elif cleaned_phone_number.startswith("371"):
 country = "Latvia"
elif cleaned_phone_number.startswith("82"):
 country = "South Korea"
elif cleaned_phone_number.startswith("91"):
 country = "India"
elif cleaned_phone_number.startswith("86"):
 country = "China"
elif cleaned_phone_number.startswith("374"):
 country = "Armenia"
elif cleaned_phone_number.startswith("49"):
 country = "Germany"
elif cleaned_phone_number.startswith("48"):
 country = "Poland"
if cleaned_phone_number.startswith("380"):
 country = "Ukraine"
elif cleaned_phone_number.startswith("7"):
 country = "Russia"
elif cleaned_phone_number.startswith("375"):
 country = "Belarus"
elif cleaned_phone_number.startswith("7"):
 country = "Kazakhstan"
elif cleaned_phone_number.startswith("1"):
 country = "America"
else:
 country = "Unknown country"
viber_link = "viber://chat?number=+" + cleaned_phone_number
print(f"Associated with a phone number {cleaned_phone_number} {country}!")
print("Link to Viber: ", viber_link)
time.sleep(2)
print(f"Link to WhatsApp:https://web.whatsapp.com/send?phone={phone_number}") 
time.sleep(2)
print(f"Link to Vk: https://vk.com/im?sel={phone_number}")
time.sleep(2)
print(f"Link to Telegram: https://t.me/{phone_number}")
time.sleep(2)
print("Thanks for using!")
