from time import sleep, perf_counter


def func1():
    sleep(2)
    print("func1")


def func2():
    sleep(4)
    print("func2")


def func3():
    sleep(3)
    print("func3")


def main():
    start = perf_counter()
    func1()
    func2()
    func3()
    end = perf_counter()
    print(f"Время выполнения: {end - start}")


if __name__ == "__main__":
    main()
