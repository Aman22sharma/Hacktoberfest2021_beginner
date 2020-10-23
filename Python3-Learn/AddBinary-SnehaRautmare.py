
def addBinary(num1: str, num2: str) -> str:
    """
    Method to add to binary numbers
    Parameters: Two binary numbers num1 and num2 (string)
    Output: Addition in binary
    """
    sumnum = int(num1,2) + int(num2,2)
    print(bin(sumnum)[2:])

addBinary("11", "1")