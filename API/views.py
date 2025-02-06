from django.http import JsonResponse
import requests
from asgiref.sync import async_to_sync
from math import sqrt

def is_prime(num):
    #counter = 0
    if num < 2:
        return "false"
    
    for itter in range(2, int(sqrt(num) + 1)):
        if num % itter == 0:
            return "false"
    return "true"


def is_perfect(num):
    temp = 0
    for i in range(1, num):
        if num % i == 0:
            temp += i
    if temp == num:
        return "true"
    return "false"


def get_properties(num):
    global digit_sum
    nc = num
    properties = []
    num_digits = []
    arm_val = 0

    digit_sum = 0

    # is armstrong
    while nc >= 10:
        temp = num % 10
        num_digits.append(temp)
        nc -= temp
        nc /= 10
    num_digits.append(nc)

    for n in num_digits:
        arm_val += n**3
        digit_sum += n

    if arm_val == num:
        properties.append("armstrong")
    if num % 2 == 0:
        properties.append("even")
    else:
        properties.append("odd")

    return properties


async def home(request, *args, **kwargs):
    #print(request.GET["number"])

    # print(kwargs["number"])
    number = request.GET["number"]
    response_data = requests.get(f"http://numbersapi.com/{number}/math")

    json_data = {
        "number": number,
        "is_prime": is_prime(int(number)),
        "is_perfect": is_perfect(int(number)),
        "properties": get_properties(int(number)),
        "digit_sum": digit_sum,
        "fun_fact": response_data.text,
    }
    print(response_data.text)
    return JsonResponse(json_data)
