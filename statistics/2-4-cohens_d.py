[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

import pandas as pd

# Formula for Cohen's D Given from textbook in exercise

def CohenEffectSize(group1, group2):
    """Computes Cohen's effect size for two groups.
    
    group1: Series or DataFrame
    group2: Series or DataFrame
    
    returns: float if the arguments are Series;
             Series if the arguments are DataFrames
    """
    diff = group1.mean() - group2.mean()

    var1 = group1.var()
    var2 = group2.var()
    n1, n2 = len(group1), len(group2)

    pooled_var = (n1 * var1 + n2 * var2) / (n1 + n2)
    d = diff / np.sqrt(pooled_var)
    return d

# SOLUTION
# SAMPLES The two different samples are First Babies and Non-First Babies
first_babies = preg[preg.birthord == 1.0].prglngth
later_babies = preg[preg.birthord != 1.0].prglngth

#first_babies.values
later_to_term = pd.Series([birth for birth in later_babies.values if birth > 20])
first_to_term = pd.Series([birth for birth in first_babies.values if birth > 20])

d = CohenEffectSize(first_to_term, later_to_term)

d

