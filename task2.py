def is_leap(x):
    x = int(x)
    if x % 4==0 and ((x%100==0 and x%400==0) or (x%100!=0)):
        return True
    return False


if __name__ == '__main__':
    if is_leap(2008)==True:
        print("it works")
