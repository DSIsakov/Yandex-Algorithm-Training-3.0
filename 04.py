n = int(input())
k = int(input())
raw = int(input())
var = int(input())

p_num = (raw-1) * 2 + var
v_num1 = p_num - k
v_num2 = p_num + k
v_var1 = (v_num1 - 1) % 2 + 1
v_var2 = (v_num2 - 1) % 2 + 1
v_raw1 = (v_num1 + 1) // 2
v_raw2 = (v_num2 + 1) // 2

if v_num1 > 0 and v_num2 <= n:
	if v_raw2 - raw <= raw - v_raw1:
		print(v_raw2, v_var2)
	else:
		print(v_raw1, v_var1)
elif v_num1 > 0:
	print(v_raw1, v_var1)
elif v_num2 <= n:
	print(v_raw2, v_var2)
else:
	print(-1)