function [x]=idft_01(X)
%
% Uso
%   [x] = idft_01(X);
%
% Esta funcion no es muy eficiente.
% pero demuestra como se realiza el calculo de la IDFT
 
Xsize=length(X)
 
% Realizar la reconstruccion
 
for n=0: Xsize-1
    for m=0: Xsize-1
        arra(n+1,m+1)=X(m+1)*(cos(2*pi*m*n/Xsize)+i*sin(2*pi*m*n/Xsize));
    end
end
for n=0:Xsize-1
    summ = 0;
    for m=0:Xsize-1
        summ = summ+arra(n+1,m+1);
    end
% Division de la longitu de la salida
x(n+1)=summ/Xsize
end