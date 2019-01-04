[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)


# Solution goes here
                               
The probability mass function displays a chart of equal probability of 1/1000 chance of being selected. On the other hand,
the cumulative disribution function shows an increasing probability from ~0 -> 1.
                                   
Code Below                                   

```python
                                   
randos = [np.random.random_sample() for i in range(1000)]

rand_cdf = thinkstats2.Cdf(randos, label='NP Rand Float Cdf')

rand_pmf = thinkstats2.Pmf(randos, label='NP Rand Float Pmf')


thinkplot.Pmf(rand_pmf)


thinkplot.Config(xlabel='Value', ylabel='P')

# What went wrong is that I have a complete chart filled out. I believe what this is saying is that every value has an equal chance of being chosen, but it doesn't directly represent the sample because the lines are not accurate enough. 

# Next Cell ###

thinkplot.Cdf(rand_cdf)
thinkplot.Config(xlabel='Value', ylabel='P')
                                   
 ```
