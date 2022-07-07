% This script isolates the centromere region of the T2T dataset
% Find the coordinates by running the nu and coordinates(patterns if visible) for each chromosome and feed it to this code
% Plots the nu values and cooedinates for the centromere(patterns if visible)

% Actual T2T bed file
% Chromosome	chr1	chr2	chr3	chr4	chr5	chr6	chr7	chr8	chr9	chr10	chr11	chr12	chr13	chr14	chr15	chr16	chr17	chr18	chr19	chr20	chr21	chr22	chrX	chr Y
% Start 	121625000	92300000	90800000	49700000	46825000	58275000	60400000	44250000	44950000	39625000	51025000	34600000	0	0	0	35825000	23425000	15650000	24575000	26375000	0	0	57825000	            8,200,002 
% Stop	142250000	94700000	96425000	55300000	50950000	61050000	63725000	46325000	76700000	41925000	54475000	37200000	17500000	12700000	17700000	52225000	27575000	21125000	29775000	32975000	11300000	15700000	60925000	          13,500,002 

% 1
% r_start = 121225002;
% r_stop  = 144800002;

% 2
% r_start = 87350002;
% r_stop  = 101975002;

% 3
% r_start = 87650002;
% r_stop  = 101375002;

% 4
% r_start = 43800002;
% r_stop  = 59400002;

% 5
% r_start = 43650002;
% r_stop  = 56025002;

% 6
% r_start = 54450002;
% r_stop  = 62625002;

% 7
% r_start = 55650002;
% r_stop  = 66700002;

% 8
% r_start = 41350002;
% r_stop  = 49100002;

% 9
% r_start = 42950002;
% r_stop  = 81650002;

% 10
% r_start = 35600002;
% r_stop  = 48925002;

% 11
% r_start = 48250002;
% r_stop  = 59250002;

% 12
% r_start = 31800002;
% r_stop  = 41825002;

% 13
% r_start = 125002;
% r_stop  = 18675002;
    % Pattern
    % r_start = 5700002;
    % r_stop  = 9350002;

% 14
% r_start = 25002;
% r_stop  = 20575002;
    % Pattern
    % r_start = 2000002;
    % r_stop  = 2825002;

% 15
% r_start = 1;
% r_stop  = 21800002;
    % Pattern
    % r_start = 2425002;
    % r_stop  = 4800002;

% 16
% r_start = 31475002;
% r_stop  = 54100002;

% 17
% r_start = 20400002;
% r_stop  = 29450002;

% 18
% r_start = 14325002;
% r_stop  = 22400002;

% 19
% r_start = 22875002;
% r_stop  = 31325002;

% 20
% r_start = 25550002;
% r_stop  = 34400002;

% 21
% r_start = 1;
% r_stop  = 13825002;
    % Pattern
    % r_start = 2950002;
    % r_stop  = 5700002;

% 22
% r_start = 1;
% r_stop  = 18725002;
    % Pattern
    % r_start = 4725002;
    % r_stop  = 5750002;

% X
% r_start = 52500002;
% r_stop  = 66750002;

% Y
% r_start = 8200002;
% r_stop  = 13500002;

n = 22;
OutputFileT2T1 = readmatrix("OutputFile_T2T_Chr"+n+".txt");

% nu
nu_T2T = OutputFileT2T1(:,[3]);
% Coordinates
Coords_T2T = OutputFileT2T1(:,[1]);
    
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
    
