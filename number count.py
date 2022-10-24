def myfunc(num):
    total = num
    avg = 0
    count = 1
    while num != "done":
        num = input("enter the input number")
        if num.isnumeric():
            total += num
            count += 1

        else:
            print("this is not a number")
    avg = float(total) / float(count)
    print(f"total is : {total} \n count is : {count} \n avg is : {avg}")

num = input("enter the input number")

myfunc(num)
