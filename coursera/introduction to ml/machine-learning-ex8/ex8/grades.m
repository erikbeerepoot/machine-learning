data = [10,32.5,37.5,42.5,67.5,40,37.5,32.5,35,55,87.5,20,35,30,62.5,45,25,95,25,25,62.5,50,50,32.5,67.5,42.5,35,67.5,67.5,22.5,50,60,45,35,90,62.5,62.5,42.5,40,82.5,65,32.5,67.5,60,70,75,70,52.5,70,62.5,75,87.5,57.5,67.2,72.5,40,80,57.5,70,70,80,82.5,60,60]
hist(data,30)
model = fitgmdist(data',2)

figure;
clf;
hold on;
