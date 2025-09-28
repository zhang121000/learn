import time
from time import localtime, strftime

'''
localtime= time.localtime(time.time())
print("本地时间：" ,localtime)
'''

print(strftime("%Y-%m-%d %H:%M:%S", localtime()))
print(strftime("%a %b %d %H:%M:%S %Y", localtime()))
print(strftime("%A %B %d %H:%M:%S %Y", localtime()))

# %a 本地简化的星期名称
# %A     完整
# %b 本地简化的月份名称
# %B     完整
# %d 月内中的一天

