
import sys
num = int(3 ** 9090001)
bytes = sys.getsizeof(num)
print ('размер в байтах', bytes)
megabytes = bytes / (1024 * 1024)
print ('размер в мегабайтах', megabytes)
