% MATLAB script RoverScan.m

% Needed scripts
load('ai_sore423.mat') % From PSSM
load('ai_LookupTable_CDF.mat')

NT = ['A','C','G','T'];
SeqFileName = input('Enter FASTA file name: ','s');
[Header,Seq] = fastaread(SeqFileName,'IgnoreGaps',true);
Hd_param = regexp(Header,'[=:-\s]','split');
Chr = 1;
Nseq = size(Seq,2);
fprintf('File contains %10u nucleotides.\n',Nseq);

Coords_start = 1;
NSegbp = input('Number of base pairs per segment: ');
if mod(Nseq,NSegbp) ~= 0
    fprintf('Number of base pairs in sequence is not an integer multiple');
    fprintf('\nof segment size. ');
    Ans = input('Truncate (T/t) or extend (E/e) sequence? ','s');
    if ismember(Ans,['T','t'])
        % Truncate to nearest integer multiple of NSegbp
        Coords_end = floor(Nseq/NSegbp)*NSegbp;
        fprintf('New sequence range = %2u - %6u bp\n',Coords_start,...
            Coords_end);
    elseif ismember(Ans,['E','e'])
        % Pad sequence by treating as circular
        Coords_end = ceil(Nseq/NSegbp)*NSegbp;
        Diff = Coords_end-Nseq;
        Seq = [Seq Seq(1:Diff+1)];
        Nseq = Nseq+Diff;
        fprintf('New sequence range = %2u - %6u bp\n',Coords_start,...
            Coords_end);
    else
        fprintf('Response is not valid.\n Terminating execution.');
        return;
    end
end    

% Get the initial coordinates for the fragemenets from the entire genome
NS = Coords_end/NSegbp;
I_s = zeros(NS,2);
Coords(1,:) = [Coords_start Coords_start+NSegbp];
Coords(NS,:) = [Coords_end-NSegbp+1 Coords_end];
for i = 1:NS
    I_s(i,:) = [(i-1)*NSegbp+1 i*NSegbp];
    if (i >= 2) && (i <= NS-1)
        Coords(i,:) = [Coords_start+(i-1)*NSegbp+1 i*NSegbp];
    end
end

% REVA incidence file histogram 
FragDistFileName = input('Enter file name for fragment size distribution: ','s');
P_L = readmatrix(FragDistFileName);
L = size(P_L,1);
if L > NSegbp
    fprintf('WARNING: Upper bound of fragment distribution exceeds ');
    fprintf('window size.\n');
    fprintf('Resetting size-distribution range.\n');
    L = NSegbp;
    fprintf('New upper bound = %5u bp\n',L);
    P_L = P_L(1:L,:);
else
    %Pad P_L with trailing zeros
    P_L = [P_L; (L+1:NSegbp)' zeros(NSegbp-L,1)];
end
Psum = sum(P_L(:,2));
P_L(:,2) = P_L(:,2)./Psum;
SiteSize = 23;
M = round(SiteSize/2);

% Compute cleavage probabilities from interpolated PSSM
% Timed portion of code
fprintf('Computing interpolated cleavage probabilities.\n');
tic
Indx = zeros(M,4);
Score = zeros(Nseq,1);
v = zeros(4,SiteSize);
sm = zeros(4,SiteSize);

for i = M:Nseq-M-1
    Subseq = Seq(i-M+1:i+M-1);
    sm = s; % values of PSSM
    for j = 1:SiteSize
        for k = 1:4
            Indx(j,k) = Subseq(j) == NT(k);
            Score(i) = Score(i)+Indx(j,k)*sm(k,j);
        end
    end
    if mod(i,NSegbp) == 0
        fprintf('Interpolation progress = %6.1f %% complete.\n',100*i/Nseq);
    end
end
fprintf('Interpolation of scoring matrix completed.\n');
toc

x1d = LookupTable((1:end), 1);
y1d = LookupTable(1:end, 2);
fd = Score;
q = interp1(x1d, y1d,fd,'spline');

qq = zeros(NSegbp,1);
nu = zeros(NS,1);
for i = 1:NS
q_r = q(I_s(i,1):I_s(i,2));
q_s = q_r;
    for j = 1:NSegbp-1
        q_s = [q_s(2:NSegbp);0];
        qq(j) = q_r'*q_s./(double(NSegbp)-j);
    end
nu(i) = P_L(:,2)'*qq;
fprintf('nu value for region %4.0d (%s:%8d-%8d) = %6.4f\n',i,Chr,...
    Coords(i,:),nu(i));
end
fprintf('Coverage computations completed\n');

Tbl_entries = [Coords nu];
% OutputFileName = input('File name for output: ','s');
writematrix(Tbl_entries,'OutputFile.txt');

exp = nu;
Corrected  = (exp-mean(nu))/std(nu);

diff = std(Corrected);
p1 = mean(Corrected) - diff;
p2 = mean(Corrected) + diff;

set(gca,'FontSize',35)
title('Human Chromosome 5, window of 25000bp');
    ylabel('Relative Coverage');
    xlabel('Coordinates in Mbp');
hold on
plot(Coords(:,[1]),Corrected,'LineWidth',2.0,'DisplayName','Nu');
yline(mean(Corrected),'r-','Mean','LineWidth',4.0, 'DisplayName','Mean') ;
yline(p1,'k--');
yline(p2,'k--');
hold off
