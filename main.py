from nckh.Vendor import Vendor
from nckh.Parameters import Parameters
import matplotlib.pyplot as plt
import numpy as np
import time


def ypoints(arr, str1):
    vt = str1.rfind(' ')
    str1 = str1[vt + 1:]
    str1 = int(str1)
    arr = np.append(arr, str1)
    return arr


def strtonumber(str):
    str = str[1:len(str) - 1]
    vtc = 0
    if len(str) < 8:
        vtc = int(str)
    else:
        arr = str.split()
        for i in range(len(arr)):
            if int(arr[i]) % 15 == 14:
                vtc = int(arr[i])
                break
    return vtc


def show(T, i, j, k, q1, q2, q3, THC1, THC2, TOC, TPC2, TRC, TSC1, TSC2, TCp):
    str1 = ''
    arr = np.array([T, i, j, k, q1, q2, q3, THC1, THC2, TOC, TPC2, TRC, TSC1, TSC2, TCp])
    for i in arr:
        str1 += str(i) + ": "
    return str1


def showinfile(T, i, j, k, q1, q2, q3, THC1, THC2, TOC, TPC2, TRC, TSC1, TSC2, TCp):
    f = open("loop %s.txt" % T, "a")
    str1 = ''
    arr = np.array([T, i, j, k, q1, q2, q3, THC1, THC2, TOC, TPC2, TRC, TSC1, TSC2, TCp])
    for i in arr:
        str1 += str(i) + ": "
    f.write(str1 + "\n")


def loop(T):
    arr1 = np.array([], dtype='i')
    arr2 = np.array([], dtype='i')
    str1 = ''
    for i in range(1, T+1):
        for j in range(1, T+1):
            for k in range(1, T+1):
                q1 = round(vd1.q(T, i))
                q2 = round(vd2.q(T, j))
                q3 = round(vd3.q(T, k))
                THC1 = round((vd1.THC1(T, i) + vd2.THC1(T, j) + vd3.THC1(T, k))/T)
                THC2 = round((vd1.THC2(T, i) + vd2.THC2(T, j) + vd3.THC2(T, k))/T)
                TOC = round((vd1.TOC() + vd2.TOC() + vd3.TOC())/T)
                TPC2 = round((vd1.TPC2(T, i) + vd2.TPC2(T, j) + vd3.TPC2(T, k))/T)
                TRC = round((vd1.TRC(T, i) + vd2.TRC(T, j) + vd3.TRC(T, k))/T)
                TSC1 = round((vd1.TSC1())/T)
                TSC2 = round((vd1.TSC2() + vd2.TSC2() + vd3.TSC2())/T)

                TCp = round(THC1 + THC2 + TOC + TPC2 + TRC + TSC1 + TSC2)
                # showinfile(T, i, j, k, q1, q2, q3, THC2, THC1, TOC, TPC2, TRC, TSC1, TSC2, TCp)

                arr1 = np.append(arr1, T)
                arr1 = np.append(arr1, i)
                arr1 = np.append(arr1, j)
                arr1 = np.append(arr1, k)
                arr1 = np.append(arr1, q1)
                arr1 = np.append(arr1, q2)
                arr1 = np.append(arr1, q3)
                arr1 = np.append(arr1, THC1)
                arr1 = np.append(arr1, THC2)
                arr1 = np.append(arr1, TOC)
                arr1 = np.append(arr1, TPC2)
                arr1 = np.append(arr1, TRC)
                arr1 = np.append(arr1, TSC1)
                arr1 = np.append(arr1, TSC2)
                arr1 = np.append(arr1, TCp)
                arr2 = np.append(arr2, TCp)

    x = min(arr2)
    vtmin = np.where(arr1 == x)
    str0 = str(vtmin[0])
    vtc = strtonumber(str0)
    vtd = vtc - 14
    arr1 = arr1[vtd: vtc + 1]
    for i in arr1:
        str1 += str(i) + " : "
    return str1
    # print(str0)
    # print(type(str0))


pr = Parameters()
print("nhap tham so")
pr.nhap()
vd1 = Vendor()
vd2 = Vendor()
vd3 = Vendor()
print("vendor 1")
vd1.nhap(pr)
print("vendor 2")
vd2.nhap(pr)
print("vendor 3")
vd3.nhap(pr)
start_time = time.time()
str1 = ''
ypoint = np.array([], dtype='i')
xpoint = np.array([10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
for i in range(10, 21):
    str1 = loop(i)
    str1 = str1[: -3]
    print(str1)
    ypoint = ypoints(ypoint, str1)
end_time = time.time()
plt.plot(xpoint, ypoint)
plt.show()
print("thoi gian thuc hien: {0:.2f}".format(end_time - start_time) + " second")
