[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

The percentage of men that qualify to audition for Blue Man Group based on height is 34.27%
 
```python 
                                   
import scipy.stats

min_in = (5*12)+10
max_in = (6*12)+1

min_height = min_in * 2.54
max_height = max_in * 2.54

mu = 178.0
sigma = 7.7

min_ht_prob = scipy.stats.norm.cdf(min_height,loc=mu,scale=sigma)
max_ht_prob = scipy.stats.norm.cdf(max_height,loc=mu,scale=sigma)

#print(f'Min ht prob: {min_ht_prob:1.5f}, Max ht prob: {max_ht_prob:1.5f}')

blue_man_prob = max_ht_prob - min_ht_prob

print(f'The percentage of men that qualify to audition \n for Blue Man Group based on height is {blue_man_prob*100:2.2f}%')

result = blue_man_prob

# Tested because of the question of > or >= in the percentiles
#_51_or_greater = 1 - min_ht_prob
#_61_or_greater = 1 - max_ht_prob
#alt_blue_man_prob = _51_or_greater - _61_or_greater
# print(f'Prob via addition: {blue_man_prob:1.5f}, prob via direct subtraction: {alt_blue_man_prob:1.5f}')
```
