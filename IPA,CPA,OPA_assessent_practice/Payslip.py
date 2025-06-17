'''
Create a class Payslip having attributes basicSalary,hra and ita.

​

Create a class PaySlipDemo containing a method getHighestPF with takes list of payslip objects and return the highest PF among the objects.

​

PF should be 12% of basic salary

​

input:

2

10000

2000

1000

50000

3000

2000

​

output:

6000

​

 Solution:

​

class Payslip:
  def __init__(self,bs,h,t):
    self.bs=bs
    self.h=h
    self.t=t
class Pd:
  def __init__(self):
    self.a=10
  def getpf(self,l):
    k=[]
    for i in l:
        a=i.bs*0.12
        k.append(a)
    k1=max(k)
    return int(k1)
if __name__=='__main__':
  p=[]
  c=input()
  for  i in range(c):
    bs=input()
    h=raw_input()
    t=input()
    p.append(Payslip(bs,h,t))
  pa=Pd()
  pf=pa.getpf(p)
  print pf
'''

class Payslip:

    def __init__(self,basicSalary,hra,ita):
        self.basicSalary = basicSalary
        self.hra = hra
        self.ita = ita

class PaySlipDemo:

    def __int__(self):
        self.rough = 'rough'

    def getHighestPF(self,list_obj):
        z=[]
        for i in list_obj:
            z.append(i.basicSalary*(12/100))
        return int(max(z))


if __name__ == '__main__':
    n=int(input())
    list_obj = []
    for i in range(n):
        basicSalary = int(input())
        hra = int(input())
        ita = int(input())
        p=Payslip(basicSalary,hra,ita)
        list_obj.append(p)
    d=PaySlipDemo()
    answer=d.getHighestPF(list_obj)
    print(answer)
