import os
import time
from dotenv import load_dotenv
from sms import *
from temp import *
from call import *
degree_sign = u'\N{DEGREE SIGN}'

load_dotenv()

min_temp_f = float(os.getenv('TEMP_MIN_F'))
min_temp_c = float(os.getenv('TEMP_MIN_C'))
max_temp_f = float(os.getenv('TEMP_MAX_F'))
max_temp_c = float(os.getenv('TEMP_MAX_C'))
admin_list = os.getenv('ADMIN_PHONES').split(',')
mode = "sms"

if __name__ == "__main__":
    print(f"Min temp: {min_temp_f}{degree_sign}")
    print(f"Max temp: {max_temp_f}{degree_sign}")
    print('\n---ADMIN NUMBERS---')

    for number in admin_list:
        print(number)

    print()

    if mode == "sms":

        while True:
            temp_f = int(read_temp()[1])
            if temp_f >= max_temp_f:
                send_sms("<HARDCODE>",f"Shop temperature is {temp_f}{degree_sign}F.")
                time.sleep(300)

            if temp_f <= min_temp_f:
                send_sms("<HARDCODE>",f"Shop temperature is {temp_f}{degree_sign}F.")
                time.sleep(300)

            else:
                print("\r" + str(return_temp()[0]) + ' ... ' + str(return_temp()[1]), end='')
                time.sleep(1)

    if mode == "call":

        while True:
            temp_f = int(read_temp()[1])
            if temp_f >= max_temp_f:
                make_call("<HARDCODE>",temp_f)
                time.sleep(300)

            if temp_f <= min_temp_f:
                send_sms("<HARDCODE>",temp_f)
                time.sleep(300)

            else:
                print("\r" + str(return_temp()[0]) + ' ... ' + str(return_temp()[1]), end='')
                time.sleep(1)

