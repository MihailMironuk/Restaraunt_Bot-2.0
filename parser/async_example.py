import asyncio
from time import perf_counter


async def func1():
    await asyncio.sleep(4)
    print("func1")
    return "func1"


async def func2():
    await asyncio.sleep(2)
    print("func2")
    return "func2"


async def func3():
    await asyncio.sleep(3)
    print("func3")
    return "func3"


async def main():
    start = perf_counter()
    results = await asyncio.gather(func1(), func2(), func3())
    end = perf_counter()
    print(f"Время выполнения: {end - start}")

    print(results)


if __name__ == "__main__":
    asyncio.run(main())
