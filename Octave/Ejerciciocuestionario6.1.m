X=[10 0 0 2+4j 0 1 0 0 0 2-4j]
%CALCULO DE LA IDFT DE X
x_2=idft_01(X)		% Función IDFT de X
x_2Real=real(x_2);	% Valor real de x
x_2Imag=imag(x_2);	
x_2abs=abs(x_2);
% Valor imaginario de x
% CALCULO DE LA DFT DE x
%
% Datos de entrada x
x=x_2;
X=dft_01(x);		% Función DFT de x
XReal=real(X);		% Valor real de X
XImag=imag(X);
Xabs=abs(X);
Xangle=angle(X);		% Valor imaginario de X
% Grafica de la DFT
figure(1);
stem(Xabs,'*r');
% Grafica de la iDFT
figure(2);
stem(x_2,'*r');