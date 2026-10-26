import numpy as np
from sklearn.linear_model import Lasso

X = np.array([[1,1,0],[1,0,1],[1,1,1],[1,2,0]])
X_c = np.array([[1,0],[0,1],[1,1],[2,0]])
Y = np.array([2,2,3,4])
lambI = np.array([[0,0,0],[0,2,0],[0,0,2]])
beta_ols = np.linalg.inv(X.T @ X) @ X.T @ Y
print(beta_ols)


lamb = 2
beta_ridge = np.linalg.inv(X.T@X + lambI) @ X.T@Y

print(beta_ridge)


lasso = Lasso(alpha=0.25) 
lasso.fit(X_c, Y)
    
beta_lasso = np.insert(lasso.coef_, 0, lasso.intercept_)
print(f"Współczynniki LASSO (alpha=2): {beta_lasso}")