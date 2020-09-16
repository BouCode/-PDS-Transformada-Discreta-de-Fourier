
# Ejercicio 6.6
# DFT 
# Datos
Omega=pi/4; #frecuencia analogica
N=20;
n=0:N-1;
x=cos(Omega*n); #secuencia de prueba
X=dft_01(x);   #DFT de x(n)
f=ifft(X);

figure (1);
stem(x,"*o"); #figuras resultantes
grid;
title("Muestras de x(t)");
ylabel('Amplitud');
xlabel('Muestras');


figure (2);
stem(abs(X),"*r"); 
grid;
title("Modulo de la DFT de x");
ylabel('Amplitud');
xlabel('Muestras');

figure (3);
stem(f,"*o"); #IFFT
grid;
title("IFFT");
ylabel('Amplitud');
xlabel('Muestras');