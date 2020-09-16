function [X]=dft_01(x)
#
# Cálculo de la DFT de modo directo.
#
Xsize=length(x);
# Cálculo la DFT (Por el camino menos eficiente)
for m=0:Xsize-1
sum=0;
for n=0:Xsize-1
sum=sum+x(n+1)*(cos(2*pi*n*m/Xsize)-1i*sin(2*pi*n*m/Xsize));
end
X(m+1)=sum;
end