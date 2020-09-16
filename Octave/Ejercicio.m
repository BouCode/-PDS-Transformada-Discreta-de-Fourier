% CALCULO DE LA DFT por el método directo
% utilizando la función dft_01().m
close all;
clear all;
clc;
% Datos iniciales.
f1=40;
f2=140; % frecuencia analógica en Hz.
fs=200; % frecuencia de muestreo en Hz.
Ts=1/fs; % periodo de muestreo
n=0:Ts:0.50
% Secuencia de prueba
x=cos(2*pi*f1*n)+0.5*cos(2*pi*f2*n)
N=length(x);
% Calculo de la DFT de x[n]
X=dft_01(x);
Xabs=abs(X);
Xmax=max(abs(X));
% Ploteo de las gráficas resultantes
figure(1);
stem(x, '.-b'); % Gráfica de x[n]en tiempo discreto.
xlabel(sprintf('%6.5f Segundos entre muestra y muestra', Ts));
title('Muestras de x(t)');
% Gráfica en el dominio de la frecuencia.
figure(2);
stem(abs(X),'.','Color',[0.41,0.26,0.10]);
xlabel(sprintf('La resolución de frecuencia es de %5.2f Hz entre muestras', fs/(length(X)-1)));
title('Módulo de la DFT de x')