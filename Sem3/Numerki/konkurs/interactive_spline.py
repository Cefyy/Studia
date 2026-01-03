"""
Program pozwala interaktywnie tworzyć NIFS3.
Węzły interpolacji tworzymy poprzez klikanie na wykres
z podłożonym jako tłem wybranym obrazem
(w naszym przypadku "napis.jpg" to oryginalny napis konkursowy)
Program po wprowadzeniu punktów i ręcznym ustawieniu gęstości punktów
tworzy splajny dzięki funkcjom programu spline.py
Tryby są zmieniane za pomocą klawisza E
Funkcje:
    Tryby:
        DRAW:
            umożliwia dodawanie punktów interpolacji na wykresie
            poprzez kliknięcie LPM
            zakończenie powstałej krzywej - PPM/Enter
            cofnięcie dodania punktu - Z
            zapisanie powstałych krzywych i wyjście z programu - Q
        EDIT:
            powstałą krzywą możemy edytować poprzez przesuwanie węzłów
            poprzez przeciągniecie trzymająć LPM
            usunięcie wskazanego punktu po najechaniu na niego kursorem
            i wciśnięcie PPM
            usunięcie całej zaznaczonej krzywej - DEL
            cofnięcie - Z
            zapisanie - Q
            zwiększenie/zmniejszenie gęstości o 0.1 punktów pośrednich - (+,=,up)/(-,_,down)
Program dodatkowo tworzy pliki podsumowujące powstały obraz:
    konkurs-<nr indeksu>.png - plik z obrazem
    konkurs-<nr indeksu>-density.txt - plik tekstowy zawierający dane
    o gęstości punktów w każdej z krzywych
    konkurs-<nr indeksu>-dane.txt - plik tekstowy zawierający koordynaty x i y
    każdego węzła interpolacji w każdej z krzywych
    konkurs-<nr indeksu>-podsumowanie.txt -
    kolejno : ilość splajnów, ilość węzłów interpolacji,suma rozmiaru wszystkich tablic u
Program przy uruchomieniu prosi o podanie numeru indeksu, którego użyje do stworzenia tytułów plików (domyślnie 123456)
Domyślne ustawienie gęstości to 0.5 dla każdej krzywej
Używa pakietów bibliotek numpy,matplotlib oraz os
Oraz funkcji programu spline.py
W folderze musi znajdować się plik z rozszerzeniem jpg lub png, które nazwę należy wpisać
w stałej IMAGE_PATH (na moje potrzeby plik z oryginalnym obrazem nosił tytuł "napis.jpg" tak jak jest w kodzie)
Autor : Jakub Grzelak
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from spline import FastNIFS3
import os

# Konfiguracja plików, input nr indeksu oraz ścieżka do obrazu
script_dir = os.path.dirname(os.path.abspath(__file__))
IMAGE_PATH = os.path.join(script_dir, "napis.jpg")

INDEX_NUMBER = input("Podaj numer indeksu: ").strip()
if not INDEX_NUMBER:
    INDEX_NUMBER = "123456"

OUTPUT_DATA_FILE = os.path.join(script_dir, f"konkurs-{INDEX_NUMBER}-dane.txt")
OUTPUT_SUMMARY_FILE = os.path.join(
    script_dir, f"konkurs-{INDEX_NUMBER}-podsumowanie.txt"
)
OUTPUT_IMAGE_FILE = os.path.join(script_dir, f"konkurs-{INDEX_NUMBER}.png")
OUTPUT_DENSITY_FILE = os.path.join(script_dir, f"konkurs-{INDEX_NUMBER}-density.txt")
U_DENSITY = 0.5  # Domyślna gęstość,czyli ilość punktów na pixel


class SplineBuilder:
    def __init__(self, image_path):
        self.image_path = image_path  # ścieżka do obrazu
        self.curves = (
            []
        )  # każda krzywa ma parametry: x, y, t, u, sx, sy, line, knots, density
        self.current_points = {"x": [], "y": []}

        self.mode = "DRAW"  # domyślny tryb to DRAW
        self.selected_curve_idx = None
        self.selected_point_idx = None
        self.default_density = U_DENSITY

        # Obsługa przeciągania punktów na wykresie
        self.dragging_point = None
        self.hovered_curve_idx = None
        self.drag_radius = 10  # tolerancja wskazywania punktu
        # wczytywanie obrazu, jeśli podana scieżka byłaby nie prawidłowa otrzymamy błąd na konsoli
        self.img = None
        if image_path:
            try:
                self.img = mpimg.imread(image_path)
            except FileNotFoundError:
                print(f"Error: Image {image_path} not found.")

        self.fig, self.ax = plt.subplots(figsize=(10, 6))
        if self.img is not None:
            self.ax.imshow(self.img)
        else:  # error handling w razie błędnej ścieżki, taką informacje otrzyammy na wykresie zamiast obrazu
            self.ax.set_xlim(0, 1000)
            self.ax.set_ylim(1000, 0)
            self.ax.text(500, 500, "No Image Found", ha="center")
        # tytuł wykresu dla trybów
        self.ax.set_title(
            f"Index: {INDEX_NUMBER} | Mode: {self.mode} | 'e': toggle mode, 'q': save"
        )

        self.cid_click = self.fig.canvas.mpl_connect(
            "button_press_event", self.on_click
        )
        self.cid_release = self.fig.canvas.mpl_connect(
            "button_release_event", self.on_release
        )
        self.cid_motion = self.fig.canvas.mpl_connect(
            "motion_notify_event", self.on_motion
        )
        self.cid_key = self.fig.canvas.mpl_connect("key_press_event", self.on_key)

        (self.line,) = self.ax.plot(
            [], [], "ro-", markersize=4, alpha=0.6
        )  # Current points
        (self.temp_spline_line,) = self.ax.plot([], [], "b-", linewidth=0.5)  # Preview

        self.load_data()

    # wczytywanie danych z plików konfiguracjnych density i dane
    def load_data(self):
        # Najpierw wczytujemy densities
        densities = []
        if os.path.exists(OUTPUT_DENSITY_FILE):
            try:
                with open(OUTPUT_DENSITY_FILE, "r") as f:
                    for line in f:
                        if ":" in line:
                            try:
                                densities.append(float(line.split(":")[1].strip()))
                            except ValueError:
                                pass
            except Exception as e:
                print(f"Error loading densities: {e}")
        # później dane o punktach przechowywane jako tablice par koordynatów x i y
        if not os.path.exists(OUTPUT_DATA_FILE):
            return

        print(f"Loading existing data from {OUTPUT_DATA_FILE}...")
        try:
            with open(OUTPUT_DATA_FILE, "r") as f:
                content = f.read()

            blocks = content.strip().split("\n\n")

            curve_idx = 0
            for block in blocks:
                block = block.strip()
                if not block:
                    continue

                density = (
                    densities[curve_idx] if curve_idx < len(densities) else U_DENSITY
                )

                try:
                    data = eval(block)
                    if (
                        isinstance(data, list)
                        and len(data) > 0
                        and isinstance(data[0], (list, tuple))
                    ):
                        x = np.array([p[0] for p in data])
                        y = np.array([p[1] for p in data])
                        self.add_existing_curve(x, y, density)
                        curve_idx += 1
                        continue
                except:
                    pass

                lines = block.split("\n")
                if len(lines) < 2:
                    continue

                x_line = [l for l in lines if l.startswith("x :=")]
                y_line = [l for l in lines if l.startswith("y :=")]

                if not x_line or not y_line:
                    continue

                # tworzymy z każdej z tablic krzywą o parametrach : tablica x, tablica y, jej density
                try:
                    x_str = x_line[0].split(":=")[1].strip()
                    y_str = y_line[0].split(":=")[1].strip()

                    x = np.array(eval(x_str))
                    y = np.array(eval(y_str))

                    self.add_existing_curve(x, y, density)
                    curve_idx += 1
                except Exception as e:
                    print(f"Error parsing curve block: {e}")
        except Exception as e:
            print(f"Error loading data: {e}")

    def add_existing_curve(self, x, y, density=U_DENSITY):
        (line_obj,) = self.ax.plot(
            [], [], "g-", linewidth=0.5
        )  # linia w kolorze zielonym
        (knots_obj,) = self.ax.plot(
            [], [], "rx", markersize=3
        )  # węzły w kolorze czerwonym
        self.curves.append(
            {
                "x": x,
                "y": y,
                "t": [],
                "u": [],
                "sx": [],
                "sy": [],
                "line": line_obj,
                "knots": knots_obj,
                "density": density,
            }
        )
        self.recalculate_curve(len(self.curves) - 1)  # liczymy splajna na tej krzywej

    # funkcja szukająca węzeł interpolacji najbliżej kursora
    def get_closest_point(self, x_data, y_data):
        if not self.curves and not self.current_points["x"]:
            return None

        min_dist = float("inf")
        closest = None

        # sprawdzamy punkty w aktualnej krzywej
        curr_x = self.current_points["x"]
        curr_y = self.current_points["y"]
        for i, (px, py) in enumerate(zip(curr_x, curr_y)):
            dist = np.sqrt((px - x_data) ** 2 + (py - y_data) ** 2)
            if dist < min_dist:
                min_dist = dist
                closest = (-1, i)

        # sprawdzamy ukończone krzywe
        for c_idx, curve in enumerate(self.curves):
            for p_idx, (px, py) in enumerate(zip(curve["x"], curve["y"])):
                dist = np.sqrt((px - x_data) ** 2 + (py - y_data) ** 2)
                if dist < min_dist:
                    min_dist = dist
                    closest = (c_idx, p_idx)

        if min_dist < self.drag_radius:
            return closest
        return None

    # działania podczas kliknięcia
    def on_click(self, event):
        if event.inaxes != self.ax:
            return

        # wyłączone edytowanie podczas używania opcji wykresu matplotlib
        # jak np. zoomowanie lub przesuwanie wykresu
        if self.fig.canvas.toolbar.mode != "":
            return

        if self.mode == "DRAW":
            if event.button == 1:  # LPM
                # ignorujemy duplikaty punktów by uniknąć dzielenia przez 0 przy liczeniu splajnów
                if self.current_points["x"]:
                    last_x = self.current_points["x"][-1]
                    last_y = self.current_points["y"][-1]
                    if np.isclose(event.xdata, last_x) and np.isclose(
                        event.ydata, last_y
                    ):
                        print("Ignored duplicate point")
                        return
                # dodajemy punkt w miejscu kliknięcia
                self.current_points["x"].append(event.xdata)
                self.current_points["y"].append(event.ydata)
                self.update_plot()
            elif event.button == 3:  # PPM
                self.finish_curve()  # kończymy aktualną krzywą

        elif self.mode == "EDIT":
            closest = self.get_closest_point(
                event.xdata, event.ydata
            )  # najbliższy punkt, który chcemy edytować

            if event.button == 1:  # LPM - zależnie dodanie punktu, przesunięcie go
                if closest:  # przesuwanie
                    c_idx, p_idx = closest
                    if c_idx != -1:  # działamy tylko na zakończonych krzywych
                        self.selected_curve_idx = c_idx
                        self.selected_point_idx = p_idx
                        self.dragging_point = closest
                        self.highlight_selection()
                else:
                    # dodanie punktu - klikniecie blisko linii na zaznaczonej krzywej i dodajemy nowy wezel na niej
                    if not self.try_add_point(event.xdata, event.ydata):
                        # jeśli klikniemy puste pole to odznaczamy
                        self.selected_curve_idx = None
                        self.selected_point_idx = None
                        self.highlight_selection()

            elif event.button == 3:  # PPM - usunięcie punktu
                if closest:
                    c_idx, p_idx = closest
                    if c_idx != -1:
                        self.delete_point(c_idx, p_idx)

    def highlight_selection(
        self,
    ):  # zaznaczenie krzywej zmienia jej kolor na magenta i kolor wezłów na niebieski dla czytelności

        for i, curve in enumerate(self.curves):
            if i == self.selected_curve_idx:
                curve["line"].set_linewidth(2.5)
                curve["line"].set_color("magenta")
                curve["knots"].set_color("blue")
                curve["knots"].set_markersize(6)
            else:
                curve["line"].set_linewidth(0.5)
                curve["line"].set_color("green")
                curve["knots"].set_color("red")
                curve["knots"].set_markersize(3)
        self.fig.canvas.draw()

    def delete_point(self, c_idx, p_idx):  # usunięcie punktu
        curve = self.curves[c_idx]
        if len(curve["x"]) < 2:  # krzywą traktujemy jako co najmniej 2 punkty
            print("Cannot delete point: Curve needs at least 2 points.")
            return

        # usunięcie
        curve["x"] = np.delete(curve["x"], p_idx)
        curve["y"] = np.delete(curve["y"], p_idx)
        # informacja o usunięciu na konsoli
        print(f"Deleted point {p_idx} from curve {c_idx+1}")
        self.recalculate_curve(c_idx)  # obliczamy na nowo
        self.selected_point_idx = None  # odznaczamy punkt
        self.highlight_selection()

    # puszczając przycisk wyłączamy tryby przesuwania, co powoduje że punkt zostaje w miejscu przesuniętym
    def on_release(self, event):
        self.dragging_point = None

    # działania podczas przesuwania
    def on_motion(self, event):
        if event.inaxes != self.ax:
            return

        # Jeśli używamy jakies opcji z maplotlib wyłączamy edytowanie
        if self.fig.canvas.toolbar.mode != "":
            return
        # Jeśli nie przesuwamy żadnego punktu to nic nie robimy
        if self.dragging_point is None:
            return

        c_idx, p_idx = self.dragging_point

        # Aktualne punkty możemy przesuwać tylko w trybie DRAW
        if self.mode == "DRAW":
            if c_idx == -1:
                self.current_points["x"][p_idx] = event.xdata
                self.current_points["y"][p_idx] = event.ydata
                self.update_plot()
        # Punkty w skończonych krzywych możemy przesuwać w trybie EDIT
        elif self.mode == "EDIT":
            if c_idx != -1:
                curve = self.curves[c_idx]
                curve["x"][p_idx] = event.xdata
                curve["y"][p_idx] = event.ydata
                self.recalculate_curve(c_idx)

    # Funkcja obliczający splajn na krzywej
    def recalculate_curve(self, c_idx):
        curve = self.curves[c_idx]
        x = curve["x"]
        y = curve["y"]
        density = curve.get("density", U_DENSITY)

        # t[i] to łączna suma od początku do i-tego punktu obliczona wzorem na odl. dwóch punktów
        # umożliwia nam to posiadanie pętli oraz pionowych linii na naszym wykresie, ponieważ t cały czas rośnie
        t = np.zeros(len(x))
        for i in range(1, len(x)):
            dist = np.sqrt((x[i] - x[i - 1]) ** 2 + (y[i] - y[i - 1]) ** 2)
            t[i] = t[i - 1] + dist
        # u są to równomiernie ułożone punkty od początku początku krzywej do jej końca
        # ilość punktów to długość krzywej*density + 10 (stały dodatek 10 umożliwia gładkie rysowanie nawet krótkim krzywym)
        u = np.linspace(t[0], t[-1], int(t[-1] * density) + 9)
        # używamy funkcji z pliku spline.py
        try:
            spline = FastNIFS3(t)
            Mx = spline.get_moments(x)  # funkcja get_moments oblicza momenty
            My = spline.get_moments(y)

            sx = spline.evaluate_spline(
                x, Mx, u
            )  # funkcja evaluate_spline wylicza splajny metodą znaną z wykładu
            sy = spline.evaluate_spline(y, My, u)

            curve["t"] = t
            curve["u"] = u
            curve["sx"] = sx
            curve["sy"] = sy

            # Zamieniamy krzywą na splajna na tych węzłach oraz ponownie rysujemy ją na wykresie
            curve["line"].set_data(sx, sy)
            curve["knots"].set_data(x, y)
            self.fig.canvas.draw()

        except Exception as e:
            print(f"Error updating spline: {e}")

    # funkcje aktywowane klawiaturą
    def on_key(self, event):
        if event.key == "q":
            self.save_and_exit()
        elif event.key == "e":  # zmiana trybu
            self.mode = "EDIT" if self.mode == "DRAW" else "DRAW"
            self.selected_curve_idx = None
            self.selected_point_idx = None
            self.highlight_selection()  # resetowanie podswietlenia
            title = f"Index: {INDEX_NUMBER} | Mode: {self.mode} | "  # zmiana tytułu
            if self.mode == "DRAW":
                title += "Left: add, Right: finish, 'z': undo"
            else:
                title += "Left: select/drag/add, Right: delete point, 'del': delete curve, +/-: density"
            self.ax.set_title(title)
            self.fig.canvas.draw()

        elif self.mode == "DRAW":
            if event.key == "enter":  # kończenie
                self.finish_curve()
            elif (
                event.key == "z" and len(self.current_points["x"]) > 0
            ):  # Cofnięcie dodania punktu
                self.current_points["x"].pop()
                self.current_points["y"].pop()
                self.update_plot()

        elif self.mode == "EDIT":
            if event.key in ["+", "=", "up"]:  # zwiększenie density o 0.1
                self.adjust_density(1)
            elif event.key in ["-", "_", "down"]:  # zmniejszenie density o 0.1
                self.adjust_density(-1)
            elif event.key == "delete":  # usunięcie krzywej
                self.delete_selected_curve()

    # funkcja usuwająca zaznaczoną krzywą
    def delete_selected_curve(self):
        if self.selected_curve_idx is not None:
            # usuwamy wszystkie parametry
            self.curves[self.selected_curve_idx]["line"].remove()
            self.curves[self.selected_curve_idx]["knots"].remove()

            # usuwamy krzywą z listy
            self.curves.pop(self.selected_curve_idx)
            # resetujemy zaznaczenie
            self.selected_curve_idx = None
            self.selected_point_idx = None
            # przerysowujemy wykres
            self.fig.canvas.draw()
            # informacja w konsoli
            print("Curve deleted.")

    # odległośc kursora od krzywej używana przy dodawaniu punktów
    def get_distance_to_segment(self, p, a, b):
        # p - punkt gdzie kliknięto, a i b dwa sąsiednie węzły krzywej tworzące segment
        p = np.array(p)
        a = np.array(a)
        b = np.array(b)
        # obliczamy rzutowanie punktu p na krzywą i zwracamy odległość p od tego punktu
        ab = b - a
        if np.all(ab == 0):
            return np.linalg.norm(p - a)

        ap = p - a
        t = np.dot(ap, ab) / np.dot(ab, ab)
        t = max(0, min(1, t))

        projection = a + t * ab
        return np.linalg.norm(p - projection)

    # dodanie punktu
    def try_add_point(self, x_click, y_click):
        if self.selected_curve_idx is None:
            return False

        curve = self.curves[self.selected_curve_idx]
        x = curve["x"]
        y = curve["y"]

        min_dist = float("inf")
        best_idx = -1

        # szukamy segmentu (miejsca pomiedzy dwoma wezlami) gdzie wstawic nowy punkt
        for i in range(len(x) - 1):
            p = (x_click, y_click)
            a = (x[i], y[i])
            b = (x[i + 1], y[i + 1])
            dist = self.get_distance_to_segment(p, a, b)
            if dist < min_dist:
                min_dist = dist
                best_idx = i + 1  # wstawiamy punkt za i-ty

        # Sprawdzamy konce w razie potrzeby wstawienia wydłużenia krzywej na poczatku lub koncu
        # Odleglosc od poczatku krzywej
        dist_start = np.sqrt((x[0] - x_click) ** 2 + (y[0] - y_click) ** 2)
        if dist_start < min_dist:
            min_dist = dist_start
            best_idx = 0

        # Odleglosc od konca krzywej
        dist_end = np.sqrt((x[-1] - x_click) ** 2 + (y[-1] - y_click) ** 2)
        if dist_end < min_dist:
            min_dist = dist_end
            best_idx = len(x)
        # Tolerancja odleglosci to 20px jesli odleglosc od segmentu
        # jest mniejsza to wstawiamy w miejscu klikniecia nowy punkt
        if min_dist < 20:

            curve["x"] = np.insert(curve["x"], best_idx, x_click)
            curve["y"] = np.insert(curve["y"], best_idx, y_click)
            self.recalculate_curve(self.selected_curve_idx)
            self.highlight_selection()
            return True

        return False

    # zmiana density (direction 1 to zwiekszenie -1 to zmniejszenie o 0.1)
    def adjust_density(self, direction):
        if self.selected_curve_idx is not None:
            idx = self.selected_curve_idx
            # pobranie aktualnego density
            current_density = self.curves[idx].get("density", self.default_density)

            # zmiana
            if direction > 0:
                new_density = current_density + 0.1
            else:
                new_density = max(0.1, current_density - 0.1)

            self.curves[idx]["density"] = new_density
            self.default_density = new_density
            print(
                f"Curve {idx+1} density: {new_density:.1f}"
            )  # informacja o zmianie na konsoli
            self.recalculate_curve(idx)  # przeliczamy splajna z nowym density
        else:
            # Jeśli nie zaznaczymy zadnej krzywej to zmieniamy default density o 0.1
            if direction > 0:
                self.default_density += 0.1
            else:
                self.default_density = max(0.1, self.default_density - 0.1)
            print(f"Default density set to: {self.default_density:.1f}")

    def update_plot(self):  # zmiana na całym wykresie
        self.line.set_data(self.current_points["x"], self.current_points["y"])
        self.fig.canvas.draw()

    def finish_curve(self):  # zakończenie krzywej
        if len(self.current_points["x"]) < 2:
            print("Need at least 2 points for a curve.")
            return

        x = np.array(self.current_points["x"])
        y = np.array(self.current_points["y"])

        # Liczymy tablicę t
        t = np.zeros(len(x))
        for i in range(1, len(x)):
            dist = np.sqrt((x[i] - x[i - 1]) ** 2 + (y[i] - y[i - 1]) ** 2)
            t[i] = t[i - 1] + dist

        # Liczymy u
        u = np.linspace(t[0], t[-1], int(t[-1] * self.default_density) + 9)

        # Liczymy splajna
        try:
            spline = FastNIFS3(t)
            Mx = spline.get_moments(x)
            My = spline.get_moments(y)

            sx = spline.evaluate_spline(x, Mx, u)
            sy = spline.evaluate_spline(y, My, u)

            (line_obj,) = self.ax.plot(sx, sy, "g-", linewidth=0.5)
            (knots_obj,) = self.ax.plot(x, y, "rx", markersize=3)

            self.curves.append(
                {
                    "x": x,
                    "y": y,
                    "t": t,
                    "u": u,
                    "sx": sx,
                    "sy": sy,
                    "line": line_obj,
                    "knots": knots_obj,
                    "density": self.default_density,
                }
            )

            print(
                f"Curve {len(self.curves)} added with {len(x)} points."
            )  # informacja o nowej krzywej w konsoli

            # Resetujemy aktualne punkty, by zacząc nową krzywą
            self.current_points = {"x": [], "y": []}
            self.update_plot()

        except Exception as e:
            print(f"Error fitting spline: {e}")

    # zapisywanie danych do plików
    def save_and_exit(self):
        print("Saving data...")  # informacja w konsoli

        # Plik data
        with open(OUTPUT_DATA_FILE, "w") as f:
            for curve in self.curves:
                f.write(f"x := {curve['x'].tolist()}\n")
                f.write(f"y := {curve['y'].tolist()}\n")
                f.write(f"t := {curve['t'].tolist()}\n")
                f.write(f"u := {curve['u'].tolist()}\n\n")

        # Zapisujemy podsumowanie
        num_curves = len(self.curves)
        total_points = sum(len(c["x"]) for c in self.curves)
        total_u_size = sum(len(c["u"]) for c in self.curves)

        with open(OUTPUT_SUMMARY_FILE, "w") as f:
            f.write(f"{num_curves}, {total_points}, {total_u_size}")

        # Zapisujemy density
        with open(OUTPUT_DENSITY_FILE, "w") as f:
            for i, curve in enumerate(self.curves):
                density = curve.get("density", U_DENSITY)
                f.write(f"Curve {i+1}: {density}\n")

        # Zapisujemy obraz jako stworzone krzywe na białym tle
        # poprzez stworzenie nowego figure
        fig_out, ax_out = plt.subplots()
        ax_out.set_aspect("equal")
        if self.img is not None:
            h, w, _ = self.img.shape
            ax_out.set_xlim(0, w)
            ax_out.set_ylim(h, 0)  # (0,0 to lewy górny róg)
        else:
            ax_out.invert_yaxis()

        for curve in self.curves:
            ax_out.plot(curve["sx"], curve["sy"], "r-", linewidth=0.5)

        ax_out.axis("off")
        fig_out.savefig(OUTPUT_IMAGE_FILE, bbox_inches="tight", pad_inches=0, dpi=1200)
        # informacja w konsoli
        print(
            f"Saved {OUTPUT_DATA_FILE}, {OUTPUT_SUMMARY_FILE}, {OUTPUT_DENSITY_FILE}, {OUTPUT_IMAGE_FILE}"
        )
        # zamykamy figure
        plt.close("all")


# wywołanie programu
if __name__ == "__main__":
    builder = SplineBuilder(IMAGE_PATH)
    plt.show()
