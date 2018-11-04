function [C, sigma] = dataset3Params(X, y, Xval, yval)
%DATASET3PARAMS returns your choice of C and sigma for Part 3 of the exercise
%where you select the optimal (C, sigma) learning parameters to use for SVM
%with RBF kernel
%   [C, sigma] = DATASET3PARAMS(X, y, Xval, yval) returns your choice of C and 
%   sigma. You should complete this function to return the optimal C and 
%   sigma based on a cross-validation set.
%

% You need to return the following variables correctly.
C = 1;
sigma = 0.3;

param_candidates = [0.01,0.02,0.04,0.08,0.16,0.32,0.64,1.28,2.5,5,10,20,40,80];
% param_candidates = [0.01, 0.03, 0.1, 0.3, 1, 3, 10, 30];

% ====================== YOUR CODE HERE ======================
% Instructions: Fill in this function to return the optimal C and sigma
%               learning parameters found using the cross validation set.
%               You can use svmPredict to predict the labels on the cross
%               validation set. For example, 
%                   predictions = svmPredict(model, Xval);
%               will return the predictions on the cross validation set.
%
%  Note: You can compute the prediction error using 
%        mean(double(predictions ~= yval))
%

% Train models
c_index = 1;
sigma_index = 1;
for C_candidate = param_candidates
    for sigma_candidate = param_candidates        
        model(c_index,sigma_index) = svmTrain(X, y, C_candidate, @(x1, x2) gaussianKernel(x1, x2, sigma_candidate)); 
        predictions = svmPredict(model(c_index,sigma_index), Xval);        
        error(c_index, sigma_index) = mean(double(predictions ~= yval));
        params(c_index, sigma_index,:) = [C_candidate, sigma_candidate];
        sigma_index = sigma_index + 1;
    end
    sigma_index = 1;
    c_index = c_index + 1;
end

% Predict errors


% =========================================================================
idxs = find(min(min(error)) == error);
C = params(mod(idxs(1),length(param_candidates)),1 + (round(idxs(1) / length(param_candidates))),1)
sigma = params(mod(idxs(1),length(param_candidates)),1 + (round(idxs(1) / length(param_candidates))),2)


% Plot training data
plotData(Xval, yval);
visualizeBoundary(Xval, yval, model(mod(idxs(1),14),1 + (round(idxs(1) / 14))));
end
