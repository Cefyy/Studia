function I = calka(f, a, b)
	% Numeryczne liczenie calki oznaczonej metoda Romberga
	% (tablica Romberga + ekstrapolacja Richardsona).
	% I = calka(f, a, b) aproksymuje
	%   integral od a do b z f(x) dx.
	%
	% Argumenty:
	%   f - uchwyt do funkcji, np. @(x) gestosc_chi2(x, k)
	%   a - dolna granica
	%   b - gorna granica
	% Parametry metody:
	%   max_m - maksymalna liczba refinements siatki
	%   tol   - tolerancja stopu oparta o elementy diagonalne R(m,m)

	max_m = 12;
	tol = 1e-10;

	if b < a
		I = -calka(f, b, a);
		return;
	end

	if a == b
		I = 0;
		return;
	end

	R = zeros(max_m + 1, max_m + 1);
	h = b - a;

	fa = safe_eval(f, a, h, 1);
	fb = safe_eval(f, b, h, -1);
	R(1, 1) = 0.5 * h * (fa + fb);

	last_m = 1;
	for m = 2:(max_m + 1)
		h_m = h / (2^(m - 1));
		n_new = 2^(m - 2);

		sum_new = 0;
		for i = 1:n_new
			x_i = a + (2 * i - 1) * h_m;
			sum_new = sum_new + safe_eval(f, x_i, h_m, 0);
		end

		% R(m,1) to trapezy po kolejnym podwojeniu liczby przedzialow.
		R(m, 1) = 0.5 * R(m - 1, 1) + h_m * sum_new;

		% Ekstrapolacja Richardsona na kolejnych kolumnach tablicy.
		for j = 2:m
			R(m, j) = R(m, j - 1) + (R(m, j - 1) - R(m - 1, j - 1)) / (4^(j - 1) - 1);
		end

		last_m = m;
		if m >= 3
			err = abs(R(m, m) - R(m - 1, m - 1));
			if err < tol * max(1, abs(R(m, m)))
				break;
			end
		end
	end

	I = R(last_m, last_m);
end

function y = safe_eval(f, x, h, side)
	% Probuje policzyc f(x), a przy Inf/NaN delikatnie przesuwa punkt.
	y = f(x);
	if isfinite(y)
		return;
	end

	delta = max(h * 1e-6, eps(1 + abs(x)));

	if side > 0
		candidates = [x + delta, x + 10 * delta, x + 100 * delta];
	elseif side < 0
		candidates = [x - delta, x - 10 * delta, x - 100 * delta];
	else
		candidates = [x + delta, x - delta, x + 10 * delta, x - 10 * delta];
	end

	for i = 1:numel(candidates)
		y_try = f(candidates(i));
		if isfinite(y_try)
			y = y_try;
			return;
		end
	end

	error('Nie mozna obliczyc wartosci funkcji: Inf/NaN w poblizu x = %g.', x);
end
