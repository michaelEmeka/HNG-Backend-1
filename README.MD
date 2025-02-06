NUMBER CLASSIFICATION API

This project is a simple number classification API in fulfilment of the HNG intership level 1 project.
It receives a GET request via an API endpoint and send a JSON response, and appropriate HTTP status code.

*API BASE URL
https://hng-backend-1-g6xc.onrender.com
*API Endpoint
/api/classify-number/?number={number}


*JSON RESPONSE FORMAT:
{
    "number": "{number}",
    "is_prime": "{is_prime(number)}",
    "is_perfect": "{is_perfect(number)}",
    "properties": "{properties(number)}",
    "digit_sum": "{digit_sum}",  // sum of its digits
    "fun_fact": "{response.text}" //numbers API response(https://hng-backend-1-g6xc.onrender.com/api/classify-number/?number={number})
}

* API RESPONSE PARAMETERS
-number: url parameter number entry
-is_prime: boolean indicating if the number is a prime number or not
-is_perfect: boolean indicating if the number us a perfect number
-properties: array indicating parity properties. could consist of even(if number is even), odd(if number is odd), armstrong(if number is an armstrong)
-digit_sum: this is the sum of the number's individual digits
-fun_fact: fun fact about the number obtained from 3rd party numbers API

* HTTP RESPONSE CODES
-Success:
HTTP_200_OK
-Bad Request:
HTTP_403_FORBIDDEN
-Wrong Parameter Entry:
HTTP_400_BAD_REQUEST


* SETUP INSTRUCTIONS
1. Clone software from github repository into local machine
2. Install dependencies (pip install -r requirements.txt) from root directory
3. Run server (python manage.py runserver)


* EXAMPLE USE CASE

API Call: https://hng-backend-1-g6xc.onrender.com/api/classify-number/?number=371

API Response: {
    "number": "371",
    "is_prime": "false",
    "is_perfect": "false",
    "properties": [
        "armstrong",
        "odd"
    ],
    "digit_sum": 11.0,
    "fun_fact": "371 is a narcissistic number."
}