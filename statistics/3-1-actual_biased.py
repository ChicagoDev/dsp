[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

resp = nsfg.ReadFemResp()

%matplotlib inline

import pandas as pd
import numpy as np


kd_count = resp.numkdhh.value_counts()
biased_kd_count = kd_count[1:]

print(f'Unbiased Count: \n{kd_count} \n\nBiased Count:\n {biased_kd_count}')


# Copied from (Page 37 in textbook). 
def BiasPmf(pmf, label): 
    new_pmf = pmf.Copy(label=label) 
    
    for x, p in pmf.Items(): 
        new_pmf.Mult(x, x) 
        
    new_pmf.Normalize() 
    
    return new_pmf
# End copy


pmf = thinkstats2.Pmf(kd_count, label='Real')
biased = BiasPmf(pmf, label='Biased')

thinkplot.PrePlot(2)
thinkplot.Pmfs([pmf, biased])
thinkplot.Show(xlabel="Kids in HH", ylabel="PMF")
