t = (0, 4, 132.42222, 10000, 12345.67)

form_str = "day_{0:02d}, ex_{1:02d} : {2:.2f}, {3:.2e}, {4:.2e}"
print(form_str.format(*t))
