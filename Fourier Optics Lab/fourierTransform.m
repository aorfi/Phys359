w = linspace(0,5000,5000);
for i = 1:length(w)
y(i,1) = sqrt(pi/2)*((2*t-w(i))*sign(2*t-w(i)) -...
    2*w(i)*sign(w(i)) + (2*t+w(i))*sign(2*t+w(i)))/(4*t^2);
end
y = y/((1/t)*sqrt(pi/2))
w = w/(2*t)
plot(w,y)