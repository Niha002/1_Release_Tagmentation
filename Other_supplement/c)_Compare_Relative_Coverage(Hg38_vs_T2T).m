% Input of two files that Roverscan outputs for Hg38 and T2T for the same chromosome
% Output: Plot relative coverage vs coordinates for both assemblies on the same graph 

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
    % Correction 
    nu_corrected = (nu-mean(nu))/std(nu)
    % Hg38 +- 1std 
    diff = std(nu_corrected);
    p1 = mean(nu_corrected) - diff;
    p2 = mean(nu_corrected) + diff;

    % T2T vars
    nu_T2T = OutputFileT2T1(:,[3]);
    Coords_T2T = OutputFileT2T1(:,[1]);
    % Correction
    nu_t2t_corrected = (nu_T2T-mean(nu_T2T))/std(nu_T2T);
    % T2T +- 1std 
    diff_t2t = std(nu_t2t_corrected);
    p1_t2t = mean(nu_t2t_corrected) - diff_t2t;
    p2_t2t = mean(nu_t2t_corrected) + diff_t2t;

    % Plot
    set(gca,'FontSize',35)
    set(gcf, 'WindowState', 'maximized')
    title("Chromosome " + n + ",window of 25000bp"); 
        ylabel('Relative Coverage');
        xlabel('Coordinates in bp');
    hold on
    
    % T2T
    plot(Coords_T2T(:,[1]),nu_t2t_corrected,'LineWidth',1.5,'DisplayName','Nu','color', '#D95319');
    yline(mean(nu_T2T),'r-','Mean','LineWidth',3.0, 'DisplayName','Mean') ;
    % HG38
    plot(Coords(:,[1]),nu_corrected,'LineWidth',1.5,'DisplayName','Nu','color', '#0072BD' );
    yline(mean(nu),'r-','Mean','LineWidth',3.0, 'DisplayName','Mean') ;
  
    % Std dev 
    yline(p1,'k--', 'DisplayName','-σ');
    yline(p2,'k--','DisplayName','+σ');
    yline(p1_t2t,':','DisplayName','-σ');
    yline(p2_t2t,':','DisplayName','+σ');

    hold off
    legend("T2T Chr "+ n,'Mean',"Hg38 Chr "+ n)
    saveas(gcf,"Compare_Rel_Chr"+n+".jpg")
    close
end 
