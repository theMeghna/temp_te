# TEST ID: TEST-001
# TEST CATEGORY: SAFE CODE
# EXPECTED SECURITY CHARACTERISTIC: Should be treated as benign application logic.
# WHETHER THE CODE IS SAFE TO EXECUTE: Yes


def add_numbers(a, b):
    return a + b


if __name__ == "__main__":
    print(add_numbers(2, 3))
