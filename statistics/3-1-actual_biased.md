[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

# Solution

If only households with children reported to the survey, the probability of having children in households shifts dramatically. 
Firstly, the chance of having no children in a household drops to zero, which is obviously incorrect. The other most dramatic
swing is the probability of having a househould with two children. The probability of having two children jumps from ~ 20% to ~ 40%.

 ```python

# I did a lot of work before getting to this answer. But in the end, this answer is mostly derived from the solution in the 
textbook. But it isn't a direct copy/paste.

resp = nsfg.ReadFemResp()

%matplotlib inline

import pandas as pd
import numpy as np


kd_count = resp.numkdhh

def BiasPmf(pmf, label): 
    new_pmf = pmf.Copy(label=label) 
    
    for x, p in pmf.Items(): 
        new_pmf.Mult(x, x) 
        
    new_pmf.Normalize() 
    
    return new_pmf

# Copied from (Page 37 in textbook). 

pmf = thinkstats2.Pmf(kd_count, label='Real')
biased = BiasPmf(pmf, label='Biased')

thinkplot.PrePlot(2)
thinkplot.Pmfs([pmf, biased])
thinkplot.Show(xlabel="Kids in HH", ylabel="PMF")

```
