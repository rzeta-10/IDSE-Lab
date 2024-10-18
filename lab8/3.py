import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

sample_sizes = [10,100,500,1000,5000,10000,50000]

l_exp = 1
p_bern = 0.5

def gen_statistics(dist,para,size):
    mean = []
    variance = []
    for i in size:
        if dist == "Exponential":
            sample = np.round(np.random.exponential(1/para,i),1)
        elif dist == "Uniform":
            sample = np.round(np.random.uniform(0,1,i),1)
        elif dist == "Bernoulli":
            sample = np.round(np.random.binomial(1,para,i),1)
        else:
            print("Invalid Type, Error!!")
            break
        
        mean_val = np.mean(sample)
        variance_val = np.var(sample)
        mean.append(mean_val)
        variance.append(variance_val)
        
    return mean,variance
    
mean_exp, var_exp = gen_statistics("Exponential",l_exp,sample_sizes)
mean_uni, var_uni = gen_statistics("Uniform",None,sample_sizes)
mean_bern, var_bern = gen_statistics("Exponential",p_bern,sample_sizes)

print("Exponential Distribution")
print("Sample Mean : ", mean_exp)
print("Sample Variance : ", var_exp)

print("-------------------------------")
print("Uniform Distribution")
print("Sample Mean : ", mean_uni)
print("Sample Variance : ", var_uni)

print("-------------------------------")
print("Bernoulli Distribution")
print("Sample Mean : ", mean_bern)
print("Sample Variance : ", var_bern)

print("-------------------------------")

plt.figure(figsize=(15,5))

plt.subplot(1,3,1)
plt.plot(sample_sizes,mean_exp,marker='x',label='Sample Mean')
plt.axhline(y=1/l_exp,color='r',linestyle='--', label='Expected Mean (1/lambda)')
plt.title("Exponential Distribution")
plt.xlabel("Sample Size")
plt.ylabel("Sample Mean")
plt.legend()
plt.xscale('log')

plt.subplot(1,3,2)
plt.plot(sample_sizes,mean_uni,marker='x',label='Sample Mean')
plt.axhline(y=p_bern,color='r',linestyle='--', label='Expected Mean (0.5)')
plt.title("Uniform Distribution")
plt.xlabel("Sample Size")
plt.ylabel("Sample Mean")
plt.legend()
plt.xscale('log')

plt.subplot(1,3,3)
plt.plot(sample_sizes,mean_bern,marker='x',label='Sample Mean')
plt.axhline(y=p_bern,color='r',linestyle='--', label='Expected Mean (p_bern)')
plt.title("Bernoulli Distribution")
plt.xlabel("Sample Size")
plt.ylabel("Sample Mean")
plt.legend()
plt.xscale('log')

plt.tight_layout()
plt.show()