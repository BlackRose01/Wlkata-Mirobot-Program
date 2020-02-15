import time
import PythonWrap

def Main():
	count = 0
	while True:
		PythonWrap.Log("123");
		count=count+1
	while count < 1000:
		count = count + 1
		time.sleep(1)
	print("aaa")

if __name__ == "__main__":
	Main()






































