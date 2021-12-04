import numpy as np

with open("input.txt") as f:
	s = f.read()
arr = list(s)
for i in range(len(arr)):
	arr[i] = ord(arr[i])*2
arr = list(np.abs(np.fft.ifft(np.fft.fft(arr))))
for i in range(len(arr)):
	arr[i] = chr(int(arr[i]/2))
print(s, "\n↓")
print("".join(arr))