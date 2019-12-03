import re

def main():
    username = input("please input your name:")
    qq_num = input("please input your qq:")
    m1 = re.match(r'^[0-9a-zA-Z_]{6,20}', username)
    if not m1:
        print("username is fail.")
    m2 = re.match(r'^[1-9]\d{4-11}$', qq_num)
    if not m2:
        print("qq is fail.")
    if m1 and m2:
        print("ok.")

if __name__ == "__main__":
    main()
