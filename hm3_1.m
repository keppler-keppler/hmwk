clear; clc; close all;

m1 = 1.0;     
m2 = 4.0;     
l  = 1.5;     
g  = 9.81;    
omega_0_list = [1.3, 2.3]; 

x0 = (m1 * l) / (m1 + m2);

tspan = [0 30];

y0 = [0; 0]; 

figure('Position', [100, 100, 800, 600]);

for i = 1:length(omega_0_list)
    w0 = omega_0_list(i);
   
    odefun = @(t, y) [
        y(2); 
        (x0 * w0^2 / l) * cos(w0 * t) - (g / l) * y(1)
    ];

    [t_eval, y_sol] = ode45(odefun, tspan, y0);
    
    x_t = x0 * cos(w0 * t_eval);

    % Plotting
    subplot(2, 1, i);
    plot(t_eval, x_t, '--b', 'LineWidth', 1.5, 'DisplayName', 'Forcing function x(t) [m]');
    hold on;
    plot(t_eval, y_sol(:,1), '-r', 'LineWidth', 1.5, 'DisplayName', 'Pendulum angle \phi(t) [rad]');
    hold off;
    
    title(sprintf('Motion with Driving Frequency \\omega_0 = %.1f rad/s', w0));
    xlabel('Time [s]');
    ylabel('Amplitude');
    legend('Location', 'northeast');
    grid on;
end