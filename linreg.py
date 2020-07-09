import numpy as np 
import matplotlib.pyplot as plt 

def estimate_coef(x, y): 
	# number of observations/points 
	m = np.size(x) 

	# mean of x and y vector 
	m_x, m_y = np.mean(x), np.mean(y) 

	# calculating cross-deviation and deviation about x 
	SS_xy = np.sum(y*x) - m*m_y*m_x 
	SS_xx = np.sum(x*x) - m*m_x*m_x 

	# calculating regression coefficients 
	th_1 = SS_xy / SS_xx 
	th_0 = m_y - th_1*m_x 

	return(th_0, th_1) 

def plot_regression_line(x, y, th): 
	# plotting the actual points as scatter plot 
	plt.scatter(x, y, color = "m", 
			marker = "o", s = 30) 

	# predicted response vector 
	y_pred = th[0] + th[1]*x 

	# plotting the regression line 
	plt.plot(x, y_pred, color = "g") 

	# putting labels 
	plt.xlabel('x') 
	plt.ylabel('y') 

	# function to show plot 
	plt.show() 

def main(): 
	# observations 
	x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) 
	y = np.array([1, 3, 2, 5, 7, 8, 8, 9, 10, 12]) 

	# estimating coefficients 
	th = estimate_coef(x, y) 
	print("Estimated coefficients:\n th_0 = {} \n th_1 = {}".format(th[0], th[1])) 

	# plotting regression line 
	plot_regression_line(x, y, th) 

if __name__ == "__main__": 
	main() 
