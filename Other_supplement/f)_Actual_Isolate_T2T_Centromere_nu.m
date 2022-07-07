% This script isolates the centromere region of the T2T dataset based on the actual T2T bed file
% Plots the nu values and coordinates for the centromere and aslo saves the files

start = [121625002, 92300002,	90800002, 49700002,	46825002, 58275002, 60400002, 44250002,	44950002, 39625002,	51025002, 34600002,	       1,        1,        1, 35825002,	23425002, 15650002,	24575002, 26375002,	       1,	       1,	57825002,  8200002]; 
 stop = [142250002, 94700002, 96425002, 55300002, 50950002, 61050002, 63725002, 46325002, 76700002, 41925002, 54475002, 37200002, 17500002, 12700002, 17700002, 52225002, 27575002, 21125002, 29775002, 32975002, 11300002, 15700002, 60925002, 13500002];
 
n = "X";
OutputFileT2T1 = readmatrix("OutputFile_T2T_Chr"+n+".txt");

% nu
nu_T2T = OutputFileT2T1(:,[3]);
% Coordinates
Coords_T2T = OutputFileT2T1(:,[1]);

r_start = start(23);
r_stop  = stop(23);  
    
% extarct regions of intrest
ind1 = find(Coords_T2T == r_start);
ind2 = find(Coords_T2T == r_stop);

C1 = Coords_T2T(ind1:ind2);
N1 = nu_T2T(ind1:ind2);

% Plot
set(gca,'FontSize',35)
set(gcf, 'WindowState', 'maximized') % fullscreen
title("T2T Centromere Chr "+n+" Window size 25000bp");
    ylabel('Nu');
    xlabel('Coordinates in bp');
hold on 
% Plot region 1 
plot(C1,N1,'LineWidth',2.0,'DisplayName','Nu', 'color', '#D95319');
yline(mean(N1),'r-','Mean','LineWidth',4.0, 'DisplayName','Mean');
ylim([0.04,0.1]);

% Nu and Coords file for centro
Tbl_entries = [C1 N1];
writematrix(Tbl_entries,"t2t_Centro_Chr"+n+".txt");
% centro
saveas(gcf,"t2t_Centro_Chr"+n+".jpg")
hold off 
