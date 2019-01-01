[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

# The following are the formulas, but I need to find a way to normalize the biased probabilities. Moving on to next Question in meantime.
import pandas as pd
import numpy as np

resp = nsfg.ReadFemResp()

# children = np.array(resp.numkdhh.value_counts())


children_hist = resp.numkdhh.value_counts()

children_pmf = resp.numkdhh.value_counts().div(resp.numkdhh.size)
children_pmf

biased_pmf = children_pmf.mul(children_hist)
