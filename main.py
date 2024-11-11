import logging

# Thiết lập logging để lưu lại quá trình tracing
logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger()

def trace(func):
    def wrapper(*args, **kwargs):
        logger.info(f"Calling {func.__name__} with arguments {args} {kwargs}")
        result = func(*args, **kwargs)
        logger.info(f"{func.__name__} returned {result}")
        return result
    return wrapper

@trace
def gcd(a, b):
    while b != 0:
        logger.info(f"Calculating GCD of {a} and {b}")
        a, b = b, a % b
    return a

@trace
def lcm(a, b):
    gcd_value = gcd(a, b)
    lcm_value = abs(a * b) // gcd_value
    return lcm_value

@trace
def main():
    # Ví dụ 2 số a,b
    a = 48
    b = 18
    logger.info(f"Tính GCD và LCM cho hai số: {a} và {b}")
    
    # Tính GCD
    gcd_result = gcd(a, b)
    logger.info(f"GCD của {a} và {b} là: {gcd_result}")
    
    # Tính LCM
    lcm_result = lcm(a, b)
    logger.info(f"LCM của {a} và {b} là: {lcm_result}")

if __name__ == "__main__":
    main()
