function plotData(X, y)
%PLOTDATA Plots the data points X and y into a new figure 
%   PLOTDATA(x,y) plots the data points with + for the positive examples
%   and o for the negative examples. X is assumed to be a Mx2 matrix.

% Create New Figure
figure; hold on;
gscatter(X(:,1),X(:,2),y)
xlabel('Exam score 1')
ylabel('Exam score 2')
legend('Not admitted', 'Admitted')
hold off;

end
