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
            
    print(temp)
    print(num)
    if temp == num:
        print("equal")
        return True
    return False


def get_properties(num):
    global digit_sum
    nc = num
    properties = []
    num_digits = []
    arm_val = 0

    digit_sum = 0

    # is armstrong
    while nc >= 10:
        temp = nc % 10
        num_digits.append(temp)
        nc -= temp
        nc /= 10
    num_digits.append(nc)

    for n in num_digits:
        arm_val += n**len(num_digits)
        #print(n)
        digit_sum += n

    if arm_val == num:
        properties.append("armstrong")
    if num % 2 == 0:
        properties.append("even")
    else:
        properties.append("odd")

    return properties


async def home(request, *args, **kwargs):
    
    if request.method == "GET":
        number = request.GET["number"]

        if not f"{number}".isdigit():
            return JsonResponse({"error": "true", "number": f"{number}"}, status=400)

        response_data = requests.get(f"http://numbersapi.com/{number}/math")

        json_data = {
            "number": int(number),
            "is_prime": is_prime(int(number)),
            "is_perfect": is_perfect(int(number)),
            "properties": get_properties(int(number)),
            "digit_sum": int(digit_sum),
            "fun_fact": response_data.text,
        }
        return JsonResponse(json_data, status=200)
