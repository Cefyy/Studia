function F = z2(x, k)
	% Dystrybuanta rozkladu chi-kwadrat dla zadania 0.
	% F(x) = calka od 0 do x z gestosc_chi2(t, k) dt
	%
	% Dziala dla skalarow i wektorow x.
	% Przy wywolaniu bez argumentow zwraca wartosc dla domyslnych
	% parametrow testowych x=0.5, k=5.

	if nargin == 0
		x = 0.5;
		k = 5;
	elseif nargin < 2
		error('Podaj oba argumenty: z2(x, k).');
	end

	if ~isscalar(k) || k <= 0 || floor(k) ~= k
		error('k musi byc dodatnia liczba calkowita.');
	end

	if ~isnumeric(x) || ~isreal(x)
		error('x musi byc rzeczywiste i numeryczne.');
	end

	F = zeros(size(x));
	idx_pos = (x > 0);

	if any(idx_pos(:))
		x_pos = x(idx_pos);
		F_pos = arrayfun(@(xi) calka(@(s) 2 * s .* gestosc_chi2(s.^2, k), 0, sqrt(xi)), x_pos);
		F(idx_pos) = F_pos;
	end

	% Ograniczenie na [0, 1] ze wzgledu na bledy numeryczne.
	F = max(0, min(1, F));
end
