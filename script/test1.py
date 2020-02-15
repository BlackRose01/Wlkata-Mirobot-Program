import time
import PythonWrap

def Add(a, b):

    return a+b
	
def Main():
	i = 1
	t1,t2,t3,t4,t5,t6 = PythonWrap.DOF6(160,0,133,0,0,0)
	s="%d,%d,%d,%d,%d,%d"%(t1,t2,t3,t4,t5,t6)
	PythonWrap.Log(s)
	while i <= 3:
		#print i
		PythonWrap.GCode("G1 x100 y100;")
		PythonWrap.Log("123");
		i += 1
		time.sleep(1)



