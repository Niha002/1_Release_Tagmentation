% MATLAB script NTStats

% Obtains nucleotide-composition statistics from Illumina reads processed
% by REVA to generate 5' extensions. Makes use of Bioinformatics Toolbox 
% function "basecount."

% Dependencies:     basecount   [           "          ]
%                   seqprofile  [           "          ]
%                   histogram
%                   evfit       [Statistics and Machine Learning Toolbox]
%                   SeqLogoFig

% 08/09/19  Initial version 
% 08/10/19  Modified to generate profiles and sequence logos
% 08/11/19  Generates 5'-subsequence profiles and similarity
%           score distributions
% 08/13/19  Fits score distribution to EVD 
%           [Extreme Value Distributions]
% 08/22/19  Corrected bug in score calculation; score distributions now
%           fitted to Gaussian model
% 10/21/19  Modified to read REVA data containing 5' extensions
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

% Compute base-call stats
NT_counts = cell2mat(struct2cell(basecount(Subseq_cat)));
NT_total = sum(NT_counts(1:4));
NT_freq = 100*NT_counts./NT_total;
FreqAT = (NT_counts(1)+NT_counts(4))/NT_total;

% Generate base-call stats output
fprintf('\n');
for i = 1:4
    fprintf('%c counts = %i, %%%c = %5.2f\n',NT(i),NT_counts(i),NT(i), ...
    NT_freq(i));
end
fprintf('\n');
fprintf('%%%c%c in subseqs = %5.2f\n',NT(1),NT(4),NT_freq(1)+NT_freq(4));
fprintf('%%%c%c in subseqs = %5.2f\n',NT(2),NT(3),NT_freq(2)+NT_freq(3));
fprintf('\n');

% Generate profile, positional information matrix, and alignment score
WtMatrix = zeros(4,MSize);
[Profile,Symbols] = seqprofile(Subseq,'Alphabet','NT');
if sym
    Profile = (Profile+flip(flip(Profile,1),2))./2;
end
s(1,:) = log2(2*Profile(1,:)/FreqAT);
s(2:3,:) = log2(2*Profile(2:3,:)/(1-FreqAT));
s(4,:) = log2(2*Profile(4,:)/FreqAT);
Hn = sum(Profile.*s,1);
for i = 1:MSize
    for j = 1:4
        WtMatrix(j,i) = Hn(i).*Profile(j,i);
    end
end

%Generate sequence logo
SeqLogoFig = seqlogo_new(WtMatrix);

Indx = zeros(MSize,4);
Score = zeros(N,1);

%SeqStr = char( );*
SeqStr = char(Subseq);
% 4xn binary array 
for i = 1:N
    for j = 1:MSize
        for k = 1:4
            %disp(i);
            %disp(j);
            Indx(j,k) = (SeqStr(i,j)) == NT(k);
            Score(i) = Score(i)+Indx(j,k)*s(k,j);
        end
    end
end

% Fit score distribution to Gaussian
Gauss = fitgmdist(Score,1);
Gauss_param(1) = Gauss.mu;
Gauss_param(2) = Gauss.Sigma;

resp = input('Generate score histogram and fitted pdf? ','s');
if ismember (resp,['Y','y'])
    Fig1 = figure('Name','Motif-score PDF','NumberTitle','off');
    Hist = histogram(Score);      % Generate score histogram and fitted pdf
    title('Motif-score Probability Density');
    xlabel('Score');
    ylabel('Number of scores');
    x_Hist = Hist.BinEdges+Hist.BinWidth/2;
    y_pdf = double(N)*Hist.BinWidth*pdf(Gauss,x_Hist');
    hold on;
    plot(x_Hist,y_pdf,'LineWidth',1.0);
    hold off;
end

% Save EVD Parameters and scoring matrix to file
FileName = input('Output MAT file for fitted params and scoring matrix: ', 's');
save(FileName,'Gauss_param','s');

  
