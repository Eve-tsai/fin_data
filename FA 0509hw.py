import numpy as np
import scipy.stats as si
S, K, T, r, sigma = 90, 100, 0.5, 0.01, 0.3
def BS(S,K,T,r,sigma): 
    d1 = (np.log(S/K)+(r+0.5*sigma**2)*T)/(sigma*np.sqrt(T))
    d2 = (np.log(S/K)+(r-0.5*sigma**2)*T)/(sigma*np.sqrt(T))    
    call = S*si.norm.cdf(d1,0.0,1.0)-K*np.exp(-r*T)*si.norm.cdf(d2,0.0,1.0)
    put = -S*si.norm.cdf(-d1,0.0,1.0)+K*np.exp(-r*T)*si.norm.cdf(-d2,0.0,1.0)
    return call,put
BS_call, BS_put= BS(S,K,T,r,sigma)
print ('S,K,T,r,sigma=',S,",",K,",",T,",",r,",",sigma)
print ('BS_call=',round(BS_call,4),', BS_put=', round(BS_put,4))

#hw: 換不同k
#不同k回傳出來的結果
#不同履約價 買權的價格回傳
#延伸範例6.4，繪製不同 K (履約價)下，之買權(call)的價格

#不同k 得不同call 儲存結果然後畫圖

import numpy as np
import scipy.stats as si
ks= np.linspace(10,150,num=10)  #linspace用來選取中間間隔
S, T, r, sigma = 90, 0.5, 0.01, 0.3
BS_calls=[]
BS_puts=[]

for i in range(10):
    K=ks[i]
    print('S,K,T,r,sigma=',S,K,T,r,sigma)
    
def BS(S,K,T,r,sigma): 
    d1 = (np.log(S/K)+(r+0.5*sigma**2)*T)/(sigma*np.sqrt(T))
    d2 = (np.log(S/K)+(r-0.5*sigma**2)*T)/(sigma*np.sqrt(T))    
    call = S*si.norm.cdf(d1,0.0,1.0)-K*np.exp(-r*T)*si.norm.cdf(d2,0.0,1.0)
    put = -S*si.norm.cdf(-d1,0.0,1.0)+K*np.exp(-r*T)*si.norm.cdf(-d2,0.0,1.0)
    return call,put    
    
for i in range(10):
    K=ks[i]
    BS_call,BS_put=BS(S,K,T,r,sigma)
    BS_calls.append(BS_call)
    BS_puts.append(BS_put)
    print('BS_call=',round(BS_call,4),',BS_put=',round(BS_put,4))
    
import matplotlib.pyplot as plt
plt.plot(ks,BS_calls)
plt.xlabel("ks")
plt.ylabel("BS_call")
plt.savefig('call.png')
plt.show()
    
    
    
    
    
    
    
    
    

