from django.http import JsonResponse
import requests
from asgiref.sync import async_to_sync
from math import sqrt

def is_prime(num):
    # counter = 0
    if num < 2:
        return False

    for itter in range(2, int(sqrt(num) + 1)):
        if num % itter == 0:
            return False
    return True


def is_perfect(num):
    temp = 0
    for i in range(1, num):
        if num % i == 0:
            temp += i
            
    #print(temp)
    #print(num)
    if temp == num:
        print("equal")
        return True
    return False


def get_properties(num):
    global digit_sum
    properties = []
    num_digits = []
    arm_val = 0
    is_negative = False

    digit_sum = 0

    if num < 0:
        num *= -1
        is_negative = True
    
    # is armstrong
    nc = num
    while nc >= 10:
        temp = nc % 10
        num_digits.append(temp)
        nc -= temp
        nc /= 10
    num_digits.append(nc)

    for n in num_digits:
        arm_val += n**len(num_digits)
        digit_sum += n

    if arm_val == num and not is_negative:
        properties.append("armstrong")
    if num % 2 == 0:
        properties.append("even")
    else:
        properties.append("odd")
    return properties


async def home(request, *args, **kwargs):

    if request.method == "GET":
        number = request.GET["number"]

        try:
            #print(type(number))
            number = int(number)
            response_data = requests.get(f"http://numbersapi.com/{number}/math")
            
            #print(response_data.text)
            json_data = {
                "number": number,
                "is_prime": is_prime(number),
                "is_perfect": is_perfect(number),
                "properties": get_properties(number),
                "digit_sum": int(digit_sum),
                "fun_fact": response_data.text,
                }
            return JsonResponse(json_data, status=200)

        except Exception as e:
            print(e)
            json_data = {
                "error": True,
                "number": number
                }
            return JsonResponse(json_data, status=400)
