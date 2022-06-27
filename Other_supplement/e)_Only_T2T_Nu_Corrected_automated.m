% Input the files that Roverscan outputs for  T2T
% Output: Plot nu corrected vs coordinates for T2T 
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
    
    % Coordinates and nu values for both Hg38 assembly and T2T 
    OutputFileT2T1 = readmatrix("OutputFile_T2T_"+n+".txt"); 

    % nu
    nu_T2T = OutputFileT2T1(:,[3]);
    % Coordinates
    Coords_T2T = OutputFileT2T1(:,[1]);

    % Correction
    nu_t2t_corrected = (nu_T2T-mean(nu_T2T))/std(nu_T2T);

    % T2T +- 1std 
    diff_t2t = std(nu_t2t_corrected);
    p1_t2t = mean(nu_t2t_corrected) - diff_t2t;
    p2_t2t = mean(nu_t2t_corrected) + diff_t2t;

    % Plot
    set(gca,'FontSize',35)
    set(gcf, 'WindowState', 'maximized') % fullscreen
    title("Chromosome " + n + ",window of 25000bp"); 
        ylabel('Relative Coverage');
        xlabel('Coordinates in bp');

    hold on
    % T2T 
    plot(Coords_T2T(:,[1]),nu_t2t_corrected,'LineWidth',1.5,'DisplayName','Nu_t2t', 'color', '#D95319');
    yline(mean(nu_t2t_corrected),'r-','Mean','LineWidth',3.0, 'DisplayName','Mean');
    ylim([-5,5])
    yticks([-5,-4,-3,-2,-1,0,1,2,3,4,5])

    % 1 std deviation
    % T2T
    yline(p1_t2t,':','DisplayName','-σ');
    yline(p2_t2t,':','DisplayName','+σ');

    hold off
    legend("T2T Chr "+ n,'Mean')
    % Save image
    saveas(gcf,"T2T_Chr"+n+".jpg")

    close
end
