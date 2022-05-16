clc
NT = ['A','C','G','T'];
FileName = input('Enter sequence-file name: ','s');
Seq = readcell(FileName);
fprintf('File contains %7u sequences.\n',size(Seq,1));
N = uint32(input('Number of sequences to process: '));
MSize = 23;
resp = input('Enforce motif symmetry? ','s');
sym = ismember(resp,['Y','y']);

% Extracts first Subseq_length nucleotides from each read
Subseq = cell(N,1);
for i = 1:N
    ext = cell2mat(Seq(i,1));
    Subseq(i) = cellstr([ext]);
end

% Concatenates each subsequence since basecount function expects 
% a single string
Subseq_cat = strjoin(Subseq,'');

% Compute base-call statsdem
NT_counts = cell2mat(struct2cell(basecount(Subseq_cat)));
NT_total = sum(NT_counts(1:4));
NT_freq = 100*NT_counts./NT_total;
FreqAT = (NT_counts(1)+NT_counts(4))/NT_total;


% Generate profile, positional information matrix, and alignment score
WtMatrix = zeros(4,MSize);

%Generate sequence logo
SeqLogoFig = T0_func_seqlogo(WtMatrix);
Indx = zeros(MSize,4);
Score = zeros(N,1);

%SeqStr = char( );*
SeqStr = char(Subseq);
% 4xn binary array 
for i = 1:N
    for j = 1:MSize
        for k = 1:4
            Indx(j,k) = (SeqStr(i,j)) == NT(k);
            Score(i) = Score(i)+Indx(j,k)*s(k,j);
        end
    end
end


% Fit score distribution to Gaussian
resp = input('Generate score histogram and fitted pdf? ','s');
if ismember (resp,['Y','y'])
    Fig1 = figure('Name','Motif-score PDF','NumberTitle','off');
    Hist = histogram(Score,'Normalization','pdf'); % Generate score histogram and fitted pdf
 
    title('Motif-score Probability Density');
    xlabel('Score');
    ylabel('Number of scores');
    
    binw = xdata(2)-xdata(1);
    sumhist = 0;
    for i=1:length(xdata)
        sumhist = sumhist + binw*ydata(i); 
    end
    disp(sumhist);

    score = linspace(xdata(1), xdata(end)); % x-axis for plotting

    % initial stat parameters for estimation -> fliplognormal
    x0 = [1.0, 0.5, -0.5];
    x1 = [2.5, 0.09, 10.0];
    % lognormal is flipped as -ve tail on the other end
    w_fun = fliplognorm(x1, score);
    % f = integral(@(s) fliplognorm (x1,s), -Inf, Inf) %integral of initial estimate

    % LSQCURVIT on the initial flip lognormal values
    options = optimoptions('lsqcurvefit','Algorithm','levenberg-marquardt');
    lb = []; ub = [];
    q = lsqcurvefit(@fliplognorm,x1,xdata,ydata,lb,ub,options)
    h = integral(@(s) fliplognorm(q,s),-Inf, Inf)
    q_fun = fliplognorm(q,score);

    % CDF intrgrating PDF
    for j = 1:length(score)
        rk(j) = integral(@(s) fliplognorm(q,s),-Inf, score(j))
    end

    % plot functions
    Fig1 = figure('Name','Motif-score PDF','NumberTitle','off');
    title('Motif-score Probability Density and Cumulative Density');
    xlabel('Score Bins');
    ylabel('Number of scores');

    hold on;
    % Score
    bar(xdata,ydata, 'DisplayName','Scores');
    % PDF
    yyaxis left
    plot(score,q_fun,'b','LineWidth',2.0, 'DisplayName','PDF');
    ylabel('PDF');
    % CDF
    yyaxis right
    gd = plot(score,rk, 'r','LineWidth',2.0, 'DisplayName','CDF')
    ylabel('CDF');
    hold off;
    legend

    % Lookup table (x,y) = (score,cdf)
    XData = get(gd, 'XData');
    YData = get(gd, 'YData');
    LookupTable = [XData' YData']
    
end

% Save Parameters and scoring matrix to file
FileName = input('Output MAT file for fitted params and scoring matrix: ', 's');
save(FileName,'Gauss_param','s'); 
