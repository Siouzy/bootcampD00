from datetime import datetime

t = (3, 30, 2019, 9, 25)

format_str = ("{3:02d}/{4:02d}/{2:04d} {0:02d}:{1:02d}")
print(format_str.format(*t))
