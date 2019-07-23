from src.storage import Storage
from src.common.data import Data


def main():
    data = Data([1, 2, 3, 4, 5], "lol")
    print(data)
    storage = Storage()
    storage.add(data)
    storage.add(Data([1, 2, 3, 4, 5], "kek"))
    print(storage.getAll())

if __name__ == '__main__':
    # execute only if run as the entry point into the program
    main()



# def disp(lst, m, p):
#     res = 0
#     for i in lst:
#         res += p*((i - m)**2)
#     return res


# print(disp([1,2,3,4], 2.5, 0.25))


# def lol(lst):
#     res = 0
#     for i in lst:
#         res += (i - 7.5)**2
#     return res


# print(lol([1,2,3,4,5]) * 2)
