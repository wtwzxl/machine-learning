''''
scatter(x, y, s=None, c=None, marker=None, cmap=None, norm=None, vmin=None, vmax=None, alpha=None, linewidths=None, verts=None, edgecolors=None,
 hold=None, data=None, **kwargs)
 
  x, y : array_like, shape (n, )
        Input data   
    
    s : scalar or array_like, shape (n, ), optional
        size in points^2.  Default is `rcParams['lines.markersize'] ** 2`.
    
    c : color, sequence, or sequence of color, optional, default: 'b'
        `c` can be a single color format string, or a sequence of color
        specifications of length `N`, or a sequence of `N` numbers to be
        mapped to colors using the `cmap` and `norm` specified via kwargs
        (see below). Note that `c` should not be a single numeric RGB or
        RGBA sequence because that is indistinguishable from an array of
        values to be colormapped.  `c` can be a 2-D array in which the
        rows are RGB or RGBA, however, including the case of a single
        row to specify the same color for all points.
    
    marker : `~matplotlib.markers.MarkerStyle`, optional, default: 'o'
        See `~matplotlib.markers` for more information on the different
        styles of markers scatter supports. `marker` can be either
        an instance of the class or the text shorthand for a particular
        
    cmap : `~matplotlib.colors.Colormap`, optional, default: None
        A `~matplotlib.colors.Colormap` instance or registered name.
        `cmap` is only used if `c` is an array of floats. If None,
        defaults to rc `image.cmap`.
    
    norm : `~matplotlib.colors.Normalize`, optional, default: None
        A `~matplotlib.colors.Normalize` instance is used to scale
        luminance data to 0, 1. `norm` is only used if `c` is an array of
        floats. If `None`, use the default :func:`normalize`.
    
    vmin, vmax : scalar, optional, default: None
        `vmin` and `vmax` are used in conjunction with `norm` to normalize
        luminance data.  If either are `None`, the min and max of the
        color array is used.  Note if you pass a `norm` instance, your
        settings for `vmin` and `vmax` will be ignored.
    
    alpha : scalar, optional, default: None
        The alpha blending value, between 0 (transparent) and 1 (opaque)
    
    linewidths : scalar or array_like, optional, default: None
        If None, defaults to (lines.linewidth,).
'''
'''
from numpy  import *
import matplotlib.pyplot as plt

def createData():
	data = array([[1.0,1.0],[1.3,1.4]])
	label= ['A','B']
	return data,label

def plotScatter(dataSet,label):
	fig = plt.figure()
	ax1= fig.add_subplot(111)  # 表示将画布分成m行n列，并取第k块
	x= [x[0] for x in dataSet] # get x value
	y= [y[1] for y in dataSet] # get y value
	ax1.scatter(x,y,c='r')
	plt.xlabel("x")
	plt.ylabel("y")
	plt.title("data analysis")
	plt.show()

dataSet,label = createData()
plotScatter(dataSet,label)
'''




from matplotlib import pyplot as plt
import numpy as np
 
# Generating a Gaussion dataset:
# creating random vectors from the multivariate normal distribution
# given mean and covariance
mu_vec1 = np.array([0,0])
cov_mat1 = np.array([[2,0],[0,2]])
print(mu_vec1)
print(cov_mat1)
x1_samples = np.random.multivariate_normal(mu_vec1, cov_mat1, 100)
x2_samples = np.random.multivariate_normal(mu_vec1+0.2, cov_mat1+0.2, 100)
x3_samples = np.random.multivariate_normal(mu_vec1+0.4, cov_mat1+0.4, 100)
 
# x1_samples.shape -> (100, 2), 100 rows, 2 columns
 
plt.figure(figsize=(8,6))
 
plt.scatter(x1_samples[:,0], x1_samples[:,1], marker='x',color='blue', alpha=0.7, label='x1 samples')
plt.scatter(x2_samples[:,0], x1_samples[:,1], marker='o', color='green', alpha=0.7, label='x2 samples')
plt.scatter(x3_samples[:,0], x1_samples[:,1], marker='^',color='red', alpha=0.7, label='x3 samples') # label 表示图例的内容
plt.title('Basic scatter plot')
plt.ylabel('variable X')
plt.xlabel('Variable Y')
plt.legend(loc='upper right')  # 图例显示的位置
 
plt.show()




















