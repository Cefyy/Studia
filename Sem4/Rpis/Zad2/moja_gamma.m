function g = moja_gamma(p)
    %korzystamy z własności Gamma(p) = (p-1)*Gamma(p-1)
    wynik = 1;

    while p > 1
        p = p - 1;
        wynik = wynik * p;
    end

    if p == 0.5
        wynik = wynik * sqrt(pi); %sytuacja dla p nieparzystych -> krok bazowy równy 1/2
    elseif p == 1 %sytuacja dla p parzystych -> krok bazowy równy 1
        wynik = wynik * 1;
    end
    
    g = wynik;
end
