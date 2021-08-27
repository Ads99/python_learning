def fancy_divide(numbers,index):
    try:
        denom = numbers[index]
        for i in range(len(numbers)):
            numbers[i] /= denom
    except IndexError:
        print("-1")
    else:
        print("1")
    finally:
        print("0")


#fancy_divide([0, 2, 4], 1)
#fancy_divide([0, 2, 4], 4)
#fancy_divide([0, 2, 4], 0)

def fancy_divide_2(numbers, index):
    try:
        denom = numbers[index]
        for i in range(len(numbers)):
            numbers[i] /= denom
    except IndexError:
        fancy_divide(numbers, len(numbers) - 1)
    except ZeroDivisionError:
        print("-2")
    else:
        print("1")
    finally:
        print("0")

#fancy_divide_2([0, 2, 4], 1)
#fancy_divide_2([0, 2, 4], 4)
#fancy_divide_2([0, 2, 4], 0)

def fancy_divide_3(numbers, index):
    try:
        try:
            denom = numbers[index]
            for i in range(len(numbers)):
                numbers[i] /= denom
        except IndexError:
            fancy_divide(numbers, len(numbers) - 1)
        else:
            print("1")
        finally:
            print("0")
    except ZeroDivisionError:
        print("-2")

#fancy_divide_3([0, 2, 4], 1)
#fancy_divide_3([0, 2, 4], 4)
#fancy_divide_3([0, 2, 4], 0)

def fancy_divide_5(list_of_numbers, index):
    try:
        try:
            raise Exception("0")
        finally:
            denom = list_of_numbers[index]
            for i in range(len(list_of_numbers)):
                list_of_numbers[i] /= denom
    except Exception as ex:
        print(ex)

fancy_divide_5([0, 2, 4], 0)