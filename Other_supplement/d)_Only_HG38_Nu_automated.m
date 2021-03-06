% Input files that Roverscan outputs for Hg38 chromosomes
% Output: Plot nu vs coordinates for Hg38

% Have the outputfiles for all chromosomes in same directory run the code to get output for all 24 chromosomes.
for i = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24];% iterate the array
    n = 0
    
    % For X chromosome 23 and Y chromsosme 24
    if i == 23;
        n = 'X';
    elseif i == 24;
        n = 'Y';
    else
        n = i;
    end
  
    % Coordinates and nu values for both Hg38 assembly and T2T 
    OutputFile1 = readmatrix("OutputFile_"+n+".txt"); 
    % OutputFileT2T1 = readmatrix("OutputFile_T2T_"+n+".txt"); 

    % nu
    nu = OutputFile1(:,[3]); 
    % nu_T2T = OutputFileT2T1(:,[3]);
    % Coordinates
    Coords = OutputFile1(:,[1]);
    % Coords_T2T = OutputFileT2T1(:,[1]);

    % Correction
    nu_corrected = (nu-mean(nu))/std(nu);
    % nu_t2t_corrected = (nu_T2T-mean(nu_T2T))/std(nu_T2T);

    % Hg38 +- 1std 
    diff = std(nu);
    p1 = mean(nu) - diff;
    p2 = mean(nu) + diff;

    % T2T +- 1std 
    % diff_t2t = std(nu_t2t_corrected);
    % p1_t2t = mean(nu_t2t_corrected) - diff_t2t;
    % p2_t2t = mean(nu_t2t_corrected) + diff_t2t;

    % Plot
    set(gca,'FontSize',35)
    set(gcf, 'WindowState', 'maximized') % fullscreen
    title("Chromosome " + n + ",window of 25000bp"); 
        ylabel('Nu');
        xlabel('Coordinates in bp');

    hold on
    % Hg38
    plot(Coords(:,[1]),nu,'LineWidth',1.5,'DisplayName','Nu','color', '#0072BD');
    yline(mean(nu),'r-','Mean','LineWidth',3.0, 'DisplayName','Mean');
    % T2T
    % plot(Coords_T2T(:,[1]),nu_t2t_corrected,'LineWidth',1.5,'DisplayName','Nu_t2t', 'color', '#D95319');
    % yline(mean(nu_t2t_corrected),'r-','Mean','LineWidth',3.0, 'DisplayName','Mean');
    ylim([0.04,0.1])
    yticks([0.04,0.05,0.06,0.07,0.08,0.09,0.1])

    % 1 std deviation Hg38
    yline(p1,'k--', 'DisplayName','-σ');
    yline(p2,'k--','DisplayName','+σ');
    % T2T
    % yline(p1_t2t,':','DisplayName','-σ');
    % yline(p2_t2t,':','DisplayName','+σ');

    hold off
    %legend("Chr "+ n,'Mean',"T2T Chr "+ n)
    legend("Chr "+ n,'Mean')
    % Save image
    saveas(gcf,"Chr"+n+".jpg")
    close
end
