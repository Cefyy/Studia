function f = gestosc_chi2(x, k)
    % Gęstość rozkładu chi-kwadrat χ²(k)
    % f(x) = 1/(2^(k/2) * Γ(k/2)) (normalizacja) * x^(k/2-1) * e^(-x/2) (potega_i_exp)
    % f(x) = (normalizacja) * (potega_i_exp)
    % Argumenty:
    %   x - punkt, w którym obliczamy gęstość (x >= 0)
    %   k - liczba stopni swobody (k ∈ N)
    %
    % Zwraca:
    %   f - wartość gęstości w punkcie x
    
    if x < 0
        f = 0;  % gęstość jest 0 dla x < 0
    else
        % Obliczenie: 1 / (2^(k/2) * Γ(k/2))
        normalizacja = 1 / (2^(k/2) * moja_gamma(k/2));
        
        % Obliczenie: x^(k/2-1) * e^(-x/2)
        potega_i_exp = x^(k/2 - 1) * exp(-x/2);
        
        f = normalizacja * potega_i_exp;
    end
end
