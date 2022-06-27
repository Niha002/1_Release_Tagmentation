% Input of two files that Roverscan outputs for Hg38 and T2T for the same chromosome
% Output: Plot nu vs coordinates for both assemblies on the same graph 

for i = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24];% iterate the array
    n = 0;
    
    % For X chromosome 23 and Y chromsosme 24
    if i == 23;
        n = 'X';
    elseif i == 24;
        n = 'Y';
    else
        n = i;
    end

    % Read Input files from both assemblies 
    OutputFile1 = readmatrix("OutputFile_"+n+".txt"); 
    OutputFileT2T1 = readmatrix("OutputFile_T2T_Chr"+n+".txt"); 

    % Hg38 vars 
    nu = OutputFile1(:,[3]); 
    Coords = OutputFile1(:,[1]);
    % Hg38 +- 1std 
    diff = std(nu);
    p1 = mean(nu) - diff;
    p2 = mean(nu) + diff;

    % T2T vars
    nu_T2T = OutputFileT2T1(:,[3]);
    Coords_T2T = OutputFileT2T1(:,[1]);
    % T2T +- 1std 
    diff_t2t = std(nu_T2T);
    p1_t2t = mean(nu_T2T) - diff_t2t;
    p2_t2t = mean(nu_T2T) + diff_t2t;

    % Plot
    set(gca,'FontSize',35)
    set(gcf, 'WindowState', 'maximized')
    title("Chromosome " + n + ",window of 25000bp"); 
        ylabel('Nu');
        xlabel('Coordinates in bp');
    hold on
    
    % HG38
    plot(Coords(:,[1]),nu,'LineWidth',1.5,'DisplayName','Nu');
    %yline(mean(nu),'r-','Mean','LineWidth',3.0, 'DisplayName','Mean') ;

    % T2T
    plot(Coords_T2T(:,[1]),nu_T2T,'LineWidth',1.5,'DisplayName','Nu');
    %yline(mean(nu_T2T),'r-','Mean','LineWidth',3.0, 'DisplayName','Mean') ;
    ylim([0.04,0.1])
    
    % Std dev 
    yline(p1,'k--', 'DisplayName','-σ');
    yline(p2,'k--','DisplayName','+σ');
    yline(p1_t2t,':','DisplayName','-σ');
    yline(p2_t2t,':','DisplayName','+σ');

    hold off
    legend("Chr "+ n,"T2T Chr "+ n)
    saveas(gcf,"Compare_Chr"+n+".jpg")
    close
end 
