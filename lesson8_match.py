a =7

match a:
    case 3:
        print("Hello")
    case 0:
        print("bye")
    case 25:
        print("money")
    case 4:
        print("happy")
    case _:
        print("error")

def fan(mode: int):
    match mode:
        case 0:
            print("swittched off")
        case 1:
            print("speed 1")
        case 2:
            print("speed 2")
        case 3:
            print("turbo mode")
        case _:
            print("invalid input!")

fan(2)

