import time

def opt1(times):
    dic = {}
    dic["l1"] = {"l2":{"l3":0}}
    # dic["aaaaaaaaaaae"] = 0
    # dic["aaaaaaaaaaab"] = 0
    # dic["aaaaaaaaaaac"] = 0
    # dic["aaaaaaaaaaad"] = 0
    # dic["aaaaaaaaaaaa"] = 0
    # dic["aaaaaaaaaaaf"] = 0
    for i in range(times):
#        "aaaaaaaaaaae" in dic
        dic["l1"]['l2']['l3'] += 1

def opt2(times):
    dic = {}
    dic["l1"] = {"l2":{"l3":0}}
    # dic = {}
    # dic["aaaaaaaaaaae"] = 0
    # dic["aaaaaaaaaaab"] = 0
    # dic["aaaaaaaaaaac"] = 0
    # dic["aaaaaaaaaaad"] = 0
    # dic["aaaaaaaaaaaa"] = 0
    # dic["aaaaaaaaaaaf"] = 0
    t = dic['l1']['l2']
    for i in range(times):
        #dic["aaaaaaaaaaaa"]
        t['l3'] += 1

# def opt1(times):
#     list = ["aaaaaaaaaaaa","bbbbbbbbbbbb","cccccccccccc","dddddddddddd","eeeeeeeeeeee","ffffffffffff"]
#     for i in range(times):
#         "aaaaaaaaaaaa" in list

# def opt2(times):
#     list = ["aaaaaaaaaaaa","bbbbbbbbbbbb","cccccccccccc","dddddddddddd","eeeeeeeeeeee","ffffffffffff"]
#     for i in range(times):
#         list


def test_time(f, times):
    start = time.perf_counter()
    f(times)
    stop = time.perf_counter()
    print(str(stop-start))
