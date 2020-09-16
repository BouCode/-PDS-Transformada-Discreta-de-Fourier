% CALCULO DE LA DFT por el m�todo directo
% utilizando la funci�n dft_01().m
close all;
clear all;
clc;
% Datos iniciales.
f=0.4; % frecuencia anal�gica en Hz.
Ts=0.125; % periodo de muestreo 
fs=1/Ts; % frecuencia de muestreo en Hz. 
n=0:Ts:6;
% Secuencia de prueba
x=cos(2*pi*f*n);
N=length(x);
% Calculo de la DFT de x[n]
X=dft_01(x);
Xabs=abs(X);
Xmax=max(abs(X));
% Ploteo de las gr�ficas resultantes
figure(1);
plot(x, '.-b'); % Gr�fica de x[n]en tiempo discreto.
xlabel(sprintf('%6.5f Segundos entre muestra y muestra', Ts));
title('Muestras de x(t)');
% Gr�fica en el dominio de la frecuencia.
figure(2);
plot(abs(X),'*','Color',[0.41,0.26,0.10]);
xlabel(sprintf('La resoluci�n de frecuencia es de %5.2f Hz entre muestras', fs/(length(X)-1)));
title('M�dulo de la DFT de x')

save -ascii dft_01.txt x X #Nombre del archivo: dft_01.txt
#clear x X

#load dft_01.txt -ascii
