import matplotlib.pyplot as plt
import pandas as pd

# sample data
df = pd.DataFrame({
    'string_col':['foo','bar','baz','quux','bum','bam','blah'],
    'x':[10,20,30,40,20,10,30],
    'y':[1,3,1,1,4,5,8]
})

# plt.subplots returns an array of arrays. We can
# directly assign those to variables directly
fig, ((ax1,ax2),(ax3,ax4)) = plt.subplots(2,2)

# bar plot for column 'x'
df.plot(y='x', kind='bar', ax=ax1)

# horizontal bar plot for column 'y'
df.plot(y='y', kind='bar', ax=ax2)

# both columns in a scatter plot
df.plot('x','y', kind='scatter', ax=ax3)

# to have two lines, plot twice in the same axis
df.plot(y='x', kind='line', ax=ax4)
df.plot(y='y', kind='line', ax=ax4)
plt.show()