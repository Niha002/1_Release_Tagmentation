% Input the files that Roverscan outputs for Hg38 
% Output: Plot nu corrected vs coordinates for Hg38 
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
    OutputFile1 = readmatrix("OutputFile_"+n+".txt"); 
    
    % nu
    nu = OutputFile1(:,[3]); 
    % Coordinates
    Coords = OutputFile1(:,[1]);

    % Correction
    nu_corrected = (nu-mean(nu))/std(nu);

    % Hg38 +- 1std 
    diff = std(nu_corrected);
    p1 = mean(nu_corrected) - diff;
    p2 = mean(nu_corrected) + diff;
 
    % Plot
    set(gca,'FontSize',35)
    set(gcf, 'WindowState', 'maximized') % fullscreen
    title("(U)Chromosome " + n + ",window of 25000bp"); 
        ylabel('Relative Coverage');
        xlabel('Coordinates in bp');

    hold on
    % Hg38
    plot(Coords(:,[1]),nu_corrected,'LineWidth',1.5,'DisplayName','Nu','color', '#0072BD');
    yline(mean(nu_corrected),'r-','Mean','LineWidth',3.0, 'DisplayName','Mean');
    ylim([-6,6]) % fixed Y axis 

    % 1 std deviation Hg38
    yline(p1,'k--', 'DisplayName','-σ');
    yline(p2,'k--','DisplayName','+σ');

    hold off
    legend("Chr "+ n,'Mean')
    % Save image
    saveas(gcf,"Zoom_Fixed_Chr"+n+".jpg")
    
    close
end
