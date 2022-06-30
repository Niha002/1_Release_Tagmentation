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

% 14
% r_start = 25002;
% r_stop  = 20575002;

% 15
% r_start = 1;
% r_stop  = 21800002;

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

% 22
% r_start = 1;
% r_stop  = 18725002;

% X
r_start = 52500002;
r_stop  = 66750002;

% Y
% r_start = 8200002;
% r_stop  = 13500002;

n = "X";
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
    
