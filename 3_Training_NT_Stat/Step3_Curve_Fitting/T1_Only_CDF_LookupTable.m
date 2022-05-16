clc; clear all;

load('T0_Histogram.mat');

binw = xdata(2)-xdata(1);
sumhist = 0;
for i=1:length(xdata);
    sumhist = sumhist + binw*ydata(i); 
end
disp(sumhist);

score = linspace(xdata(1), xdata(end)); % x-axis for plotting

% initial stat parameters for estimation -> fliplognormal
x0 = [1.0, 0.5, -0.5];
x1 = [2.5, 0.09, 10.0];
% lognormal is flipped as -ve tail on the other end
w_fun = T0_func_fliplognorm(x1, score);
% f = integral(@(s) fliplognorm (x1,s), -Inf, Inf) %integral of initial estimate

% LSQCURVIT on the initial flip lognormal values
options = optimoptions('lsqcurvefit','Algorithm','levenberg-marquardt');
lb = []; ub = [];
q = lsqcurvefit(@T0_func_fliplognorm,x1,xdata,ydata,lb,ub,options);
h = integral(@(s) T0_func_fliplognorm(q,s),-Inf, Inf);
q_fun = T0_func_fliplognorm(q,score);

% CDF intrgrating PDF
for j = 1:length(score);
    rk(j) = integral(@(s) T0_func_fliplognorm(q,s),-Inf, score(j));
end

% plot functions
Fig1 = figure('Name','Motif-score PDF','NumberTitle','off');
title('Motif-score Probability Density and Cumulative Density');
xlabel('Score Bins');
ylabel('Number of scores');

hold on;
set(gca,'FontSize',30);
% Score
bar(xdata,ydata, 'DisplayName','Scores');
% PDF
yyaxis left;
plot(score,q_fun,'b','LineWidth',2.0, 'DisplayName','PDF');
ylabel('PDF');
% CDF
yyaxis right;
gd = plot(score,rk, 'r','LineWidth',2.0, 'DisplayName','CDF');
ylabel('CDF');

hold off;
legend;

% Lookup table (x,y) = (score,cdf)
XData = get(gd, 'XData');
YData = get(gd, 'YData');
LookupTable = [XData' YData'];
save('T_Output_LookupTable','LookupTable'); 
