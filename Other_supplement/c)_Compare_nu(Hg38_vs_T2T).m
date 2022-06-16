% Input of two files that Roverscan outputs for Hg38 and T2T for the same chromosome
% Output: Plot nu vs coordinates for both assemblies on the same graph 

% Change n to chromosome number
n = 'Y'; 

% Coordinates and nu values for both Hg38 assembly and T2T 
OutputFile1 = readmatrix("OutputFile_"+n+".txt"); 
OutputFileT2T1 = readmatrix("OutputFile_T2T_"+n+".txt"); 

% nu
nu = OutputFile1(:,[3]); 
nu_T2T = OutputFileT2T1(:,[3]);
% Coordinates
Coords = OutputFile1(:,[1]);
Coords_T2T = OutputFileT2T1(:,[1]);

% Hg38 +- 1std 
diff = std(nu);
p1 = mean(nu) - diff;
p2 = mean(nu) + diff;
% T2T +- 1std 
diff_t2t = std(nu_T2T);
p1_t2t = mean(nu_T2T) - diff_t2t;
p2_t2t = mean(nu_T2T) + diff_t2t;

% Plot
set(gca,'FontSize',35)
set(gcf, 'WindowState', 'maximized') % fullscreen
title("Chromosome " + n + ",window of 25000bp"); 
    ylabel('Nu');
    xlabel('Coordinates in bp');

hold on
% Hg38
plot(Coords(:,[1]),nu,'LineWidth',1.5,'DisplayName','Nu');
yline(mean(nu),'r-','Mean','LineWidth',3.0, 'DisplayName','Mean');
% T2T 
plot(Coords_T2T(:,[1]),nu_T2T,'LineWidth',1.5,'DisplayName','Nu');
yline(mean(nu_T2T),'r-','Mean','LineWidth',3.0, 'DisplayName','Mean');

% 1 std deviation
% Hg38
yline(p1_t2t,':','DisplayName','-σ');
yline(p2_t2t,':','DisplayName','+σ');
% T2T
yline(p1,'k--', 'DisplayName','-σ');
yline(p2,'k--','DisplayName','+σ');

hold off
legend("Chr "+ n,'Mean',"T2T Chr "+ n)

% Save image
saveas(gcf,"Compare_Chr"+n+".jpg")
