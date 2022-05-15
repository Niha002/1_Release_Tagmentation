function hFigure = seqlogo_new(bitValues,minBits)

%# SEQLOGO_NEW   Displays sequence logos for DNA.
%#   HFIGURE = SEQLOGO_NEW(SEQS,MINBITS) displays the
%#   sequence logo for a set of aligned sequences SEQS,
%#   showing only those columns containing at least one
%#   nucleotide with a minimum bit value MINBITS. The
%#   MINBITS parameter is optional. SEQLOGO_NEW returns
%#   a handle to the rendered figure HFIGURE.
%#
%#   SEQLOGO_NEW calls SEQLOGO to perform some of the
%#   computations, so to use this function you will need
%#   access to the Bioinformatics Toolbox.
%#
%#   See also seqlogo.

%# Author: Ken Eaton
%# Version: MATLAB R2009a
%# Last modified: 3/30/10

% SDL modifications to generate sequence logos for NTstats.m
% Verson: MATLAB R2016a
% Created 8/26/2019
%#---------------------------------------------------------
 
% Character set: DNA sequences only.
NT = ['A','C','G','T'];

% Select columns with a minimum bit value:

if nargin > 1
    highBitCols = any(bitValues > minBits,1);  %# Plot only high-bit columns
    bitValues = bitValues(:,highBitCols);
else
    highBitCols = true(1,size(bitValues,2));   %# Plot all columns
end

% Sort the bit value data:

[bitValues,charIndex] = sort(bitValues,'descend');  %# Sort the columns
nSequence = size(bitValues,2);                      %# Number of sequences
bitValuesSum = sum(bitValues,1);
if max(bitValuesSum) > 1                            %# Upper plot limit
    maxBits = ceil(max(bitValuesSum)); 
elseif max(bitValuesSum) > 0.5
    maxBits = 1;
else
    maxBits = 0.2;
%elseif max(bitValuesSum) > 0.05
%    maxBits = 0.1;
%else
%    maxBits = roundl(max(bitValuesSum),'u',3);
end

% Create 1-by-4 cell array of letter images from the individual images:

letterImages = cell(1,4);
for i = 1:4
    FileName = [NT(i) '.png'];
    letterImages{i} = imread(FileName);
    Rows(i) = size(letterImages{i},1);
    Cols(i) = size(letterImages{i},2);
end
nRows = max(Rows(i));
nCols = max(Cols(i));

%# Create the image texture map:

    blankImage = repmat(uint8(255),[nRows nCols 3]);  %# White image
    fullImage = repmat({blankImage},4,2*nSequence-1);          %# Cell array of images
    fullImage(:,1:2:end) = letterImages(charIndex);            %# Add letter images
    fullImage = cat(1,cat(2,fullImage{1,:}),...                %# Collapse cell array
                    cat(2,fullImage{2,:}),...                  %# to one 3-D image
                    cat(2,fullImage{3,:}),...
                    cat(2,fullImage{4,:}));

% Initialize coordinates for the texture-mapped surface:

    X = [(1:nSequence)-0.375; (1:nSequence)+0.375];
    X = repmat(X(:)',5,1);     %'# Surface x coordinates
    Y = [zeros(1,nSequence); cumsum(flipud(bitValues))];
    Y = kron(flipud(Y),[1 1]);  %# Surface y coordinates
    Z = zeros(5,2*nSequence);   %# Surface z coordinates

% Render the figure:

    figureSize = [902 800];                   %# Figure size
    screenSize = get(0,'ScreenSize');         %# Screen size
    offset = (screenSize(3:4)-figureSize)/2;  %# Offset to center figure
    hFigure = figure('Units','pixels',...
                   'Position',[offset figureSize],...
                   'Color',[1 1 1],...
                   'Name','Sequence Logo',...
                   'NumberTitle','off');
    axes('Parent',hFigure,...
       'Units','pixels',...
       'Position',[100 100 750 600],...
       'FontWeight','bold',...
       'LineWidth',3,...
       'TickDir','out',...
       'XLim',[0.5 nSequence+0.5],...
       'XTick',1:nSequence,...
       'XTickLabel',num2str(find(highBitCols)'),...  %'
       'YLim',[-0.005 maxBits],...
       'YTick',0:0.1:maxBits);
    xlabel('Sequence Position');
    ylabel('Bits');
    surface(X,Y,Z,fullImage,...
          'FaceColor','texturemap',...
          'EdgeColor','none');
    view(2);

end 
