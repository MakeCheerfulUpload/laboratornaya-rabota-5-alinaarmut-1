
from matplotlib import pyplot

f = open('SPFB.RTS-12.18_180901_181231.txt')
massive1_open = []
massive1_close = []
massive1_high = []
massive1_low = []

massive2_open = []
massive2_close = []
massive2_high = []
massive2_low = []


massive3_open = []
massive3_close = []
massive3_high = []
massive3_low = []


massive4_open = []
massive4_close = []
massive4_high = []
massive4_low = []


title = f.readline()
rm = f.read()
rm = rm.split('\n')
rm.pop()
for i in rm:
    i = i.split(",")
    if '17/09' in i[2]:
        massive1_low.append(int(float(i[6])))
        massive1_high.append(int(float(i[5])))
        massive1_close.append(int(float(i[7])))
        massive1_open.append(int(float(i[4])))
for i in rm:
    i = i.split(",")
    if '17/10' in i[2]:
        massive2_low.append(int(float(i[6])))
        massive2_high.append(int(float(i[5])))
        massive2_close.append(int(float(i[7])))
        massive2_open.append(int(float(i[4])))
for i in rm:
    i = i.split(",")
    if '15/11' in i[2]:
        massive3_low.append(int(float(i[6])))
        massive3_high.append(int(float(i[5])))
        massive3_close.append(int(float(i[7])))
        massive3_open.append(int(float(i[4])))
for i in rm:
    i = i.split(",")
    if '17/12' in i[2]:
        massive4_low.append(int(float(i[6])))
        massive4_high.append(int(float(i[5])))
        massive4_close.append(int(float(i[7])))
        massive4_open.append(int(float(i[4])))
pyplot.boxplot([massive1_open, massive1_low, massive1_high, massive1_close,
                massive2_open, massive2_low, massive2_high, massive2_close,
                massive3_open, massive3_low, massive3_high, massive3_close,
                massive4_open, massive4_low, massive4_high, massive4_close])
pyplot.show()

