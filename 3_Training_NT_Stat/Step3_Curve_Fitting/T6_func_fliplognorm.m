function y = fliplognorm(x0, xdata)
    mu = x0(1);
    sigma = x0(2);
    shift = x0(3);
    y = lognpdf(-xdata+shift,mu,sigma);
end

% Updated code for trail of skewgauss
%function skew = skewgauss(x0, xdata) % order [x, mean, std_dev, alpha]
%mu    = x0(1);
%sigma = x0(2);
%alpha = x0(3);
%t = (xdata - mu)/sigma;
%normgauss = 1/sqrt((2*pi))*exp(-(t).^2/2); % PDF
%skew = 2*normgauss.*normcdf(alpha*t); % F(x) = 2*PDF(t)*CDF(alpha*t)
%end
