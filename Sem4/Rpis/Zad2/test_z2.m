% Testy funkcji dystrybuanty z2(x, k) dla rozkladu chi-kwadrat.
% Skrypt porownuje wyniki z referencja (gammainc),
% sprawdza podstawowe wlasnosci dystrybuanty i rysuje wykresy.

clear;
clc;

fprintf('=== TEST z2(x, k) ===\n\n');

% Punkty testowe:
% - kilka wartosci k (stopnie swobody)
% - kilka reprezentatywnych wartosci x
k_values = [1, 2, 5, 10];
x_values = [0, 0.2, 1, 3, 8, 15];

% Zliczanie statystyk testu punktowego.
total_tests = 0;
passed_tests = 0;
max_abs_err = 0;

fprintf('Porownanie z referencja F(x) = gammainc(x/2, k/2, ''lower'')\n');
fprintf('----------------------------------------------------------\n');
fprintf('   k      x          z2(x,k)        referencja      blad\n');
fprintf('----------------------------------------------------------\n');

for k = k_values
    for x = x_values
        total_tests = total_tests + 1;

        F_num = z2(x, k);
        F_ref = gammainc(x / 2, k / 2, 'lower');
        err = abs(F_num - F_ref);

        max_abs_err = max(max_abs_err, err);

        % Prog zaliczenia pojedynczego punktu.
        if err < 5e-4
            passed_tests = passed_tests + 1;
        end

        fprintf('%4d  %6.2f   %14.8f   %14.8f   %.3e\n', k, x, F_num, F_ref, err);
    end
end

fprintf('----------------------------------------------------------\n');
fprintf('Zaliczone testy punktowe: %d / %d\n', passed_tests, total_tests);
fprintf('Maksymalny blad bezwzgledny: %.3e\n\n', max_abs_err);

% Test monotonicznosci: F(x1) <= F(x2) dla x1 < x2.
% Dopuszczamy bardzo maly margines ze wzgledu na bledy numeryczne.
fprintf('Test monotonicznosci... ');
mono_ok = true;
for k = k_values
    xs = linspace(0, 20, 50);
    Fs = arrayfun(@(x) z2(x, k), xs);
    if any(diff(Fs) < -1e-8)
        mono_ok = false;
        break;
    end
end
if mono_ok
    fprintf('OK\n');
else
    fprintf('NIEPOWODZENIE\n');
end

% Test zakresu: 0 <= F(x) <= 1.
% Tolerancja chroni przed drobnymi odchyleniami numerycznymi.
fprintf('Test zakresu [0,1]... ');
range_ok = true;
for k = k_values
    xs = linspace(-2, 30, 80);
    Fs = arrayfun(@(x) z2(x, k), xs);
    if any(Fs < -1e-10) || any(Fs > 1 + 1e-10)
        range_ok = false;
        break;
    end
end
if range_ok
    fprintf('OK\n');
else
    fprintf('NIEPOWODZENIE\n');
end

fprintf('\n=== PODSUMOWANIE ===\n');
if passed_tests == total_tests && mono_ok && range_ok
    fprintf('Wszystkie testy przeszly poprawnie.\n');
else
    fprintf('Czesc testow nie przeszla. Sprawdz wypisane bledy powyzej.\n');
end

% Wykres porownania z2 i referencji dla kilku k.
% Gorny panel: krzywe F(x), dolny panel: blad bezwzgledny.
ks_plot = [1, 3, 5, 10];
xs_plot = linspace(0, 20, 180);

figure('Name', 'Dystrybuanta chi-kwadrat: z2 vs referencja');
tiledlayout(2, 1);

nexttile;
hold on;
for k = ks_plot
    F_num = arrayfun(@(x) z2(x, k), xs_plot);
    F_ref = arrayfun(@(x) gammainc(x / 2, k / 2, 'lower'), xs_plot);

    plot(xs_plot, F_num, 'LineWidth', 1.6, 'DisplayName', sprintf('z2, k=%d', k));
    plot(xs_plot, F_ref, '--', 'LineWidth', 1.2, 'DisplayName', sprintf('ref, k=%d', k));
end
grid on;
xlabel('x');
ylabel('F(x)');
title('Porownanie dystrybuanty: implementacja vs referencja');
legend('Location', 'southeast');

nexttile;
hold on;
for k = ks_plot
    F_num = arrayfun(@(x) z2(x, k), xs_plot);
    F_ref = arrayfun(@(x) gammainc(x / 2, k / 2, 'lower'), xs_plot);
    err = abs(F_num - F_ref);
    plot(xs_plot, err, 'LineWidth', 1.6, 'DisplayName', sprintf('k=%d', k));
end
grid on;
xlabel('x');
ylabel('|blad|');
title('Blad bezwzgledny |z2 - referencja|');
legend('Location', 'northeast');
