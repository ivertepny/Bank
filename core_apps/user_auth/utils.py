import random
import string


def generate_otp(length=6) -> str:
    otp = "".join(random.choices(string.digits, k=length))
    return otp
