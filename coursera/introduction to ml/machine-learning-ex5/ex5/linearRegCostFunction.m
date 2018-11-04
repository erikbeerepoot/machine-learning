function [J, grad] = linearRegCostFunction(X, y, theta, lambda)
%LINEARREGCOSTFUNCTION Compute cost and gradient for regularized linear 
%regression with multiple variables
%   [J, grad] = LINEARREGCOSTFUNCTION(X, y, theta, lambda) computes the 
%   cost of using theta as the parameter for linear regression to fit the 
%   data points in X and y. Returns the cost in J and the gradient in grad

% Initialize some useful values
m = length(y); % number of training examples
n = length(theta);
% You need to return the following variables correctly 
J = 0;
grad = zeros(size(theta));

% ====================== YOUR CODE HERE ======================
% Instructions: Compute the cost and gradient of regularized linear 
%               regression for a particular choice of theta.
%
%               You should set J to the cost and grad to the gradient.
%


J = (1/(2*m))*(X*theta - y)'*(X*theta - y);
% Pretty sure the loop is wrong and the line below is correct
%+ (lambda/(2*m))*(theta' * theta);
for j = 2 : n     
    J = J + (lambda/(2*m))*theta(j)^2;
end

grad = (1/m)*(X*theta - y)'*X;
for j = 2 : n 
    grad(j) = grad(j) + (lambda/m)*theta(j);
end

% =========================================================================

grad = grad(:);

end
