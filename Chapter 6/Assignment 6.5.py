text = "X-DSPAM-Confidence:    0.8475"
new_text = text.replace(" ", "")
col_loc = new_text.find(":")
num_str = new_text[col_loc+1 : ]

num = float(num_str)
print(num)
print(type(num))
