import tkinter as tk
from tkinter import filedialog, messagebox
import heapq
import time
import tracemalloc
from collections import deque

# Funzioni per il trattamento del grafo
def parse_grafo(file_path):
    """Legge un file contenente un grafo e lo converte in un dizionario di adiacenza."""
    grafo = {}
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if not line or line.startswith('#'):
                continue  # Salta le righe vuote o commentate
            try:
                nodo1, nodo2 = map(int, line.split())
                if nodo1 not in grafo:
                    grafo[nodo1] = []
                grafo[nodo1].append(nodo2)
            except ValueError:
                print(f"Riga ignorata (non numerica): {line}")
    return grafo

def traccia_percorso(genitori, start, goal):
    """Ricostruisce il percorso dal nodo di partenza a quello di arrivo."""
    percorso = []
    nodo = goal
    while nodo != start:
        percorso.append(nodo)
        nodo = genitori[nodo]
    percorso.append(start)
    percorso.reverse()
    return percorso

def carica_file_grafo():
    """Apre una finestra per caricare un file di grafo."""
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        return parse_grafo(file_path), file_path
    else:
        return None

# Algoritmi di ricerca
def bfs(grafo, start, goal):
    """Esegue la ricerca BFS (Breadth-First Search) in un grafo."""
    if start == goal:
        return [start]

    coda = deque([start])  # Coda per BFS
    visitati = {start}
    genitori = {start: None}

    while coda:
        nodo = coda.popleft()

        for vicino in grafo.get(nodo, []):
            if vicino not in visitati:
                visitati.add(vicino)
                genitori[vicino] = nodo
                if vicino == goal:
                    return traccia_percorso(genitori, start, goal)
                coda.append(vicino)

    return None

def dfs(grafo, start, goal):
    """Esegue la ricerca DFS (Depth-First Search) in un grafo."""
    stack = [start]  # Stack per DFS
    visitati = {start}
    genitori = {start: None}

    while stack:
        nodo = stack.pop()

        if nodo == goal:
            return traccia_percorso(genitori, start, goal)

        for vicino in grafo.get(nodo, []):
            if vicino not in visitati:
                visitati.add(vicino)
                genitori[vicino] = nodo
                stack.append(vicino)

    return None

def a_star(grafo, start, goal):
    """Esegue l'algoritmo A* per trovare il percorso ottimale."""
    open_set = [(0, start)]
    heapq.heapify(open_set)
    genitori = {start: None}
    g_score = {start: 0}  # Costo accumulato del percorso dal nodo di partenza

    while open_set:
        _, nodo = heapq.heappop(open_set)

        if nodo == goal:
            return traccia_percorso(genitori, start, goal)

        for vicino in grafo.get(nodo, []):
            costo = g_score[nodo] + 1  # Ipotizziamo un costo uniforme per ogni nodo
            if vicino not in g_score or costo < g_score[vicino]:
                g_score[vicino] = costo
                heapq.heappush(open_set, (costo, vicino))
                genitori[vicino] = nodo

    return None

def uniform_cost_search(grafo, start, goal):
    """Esegue la ricerca a costo uniforme (UCS) su un grafo."""
    queue = [(0, start)]  # (costo accumulato, nodo)
    visited = set()
    genitori = {start: None}

    while queue:
        costo, nodo = heapq.heappop(queue)

        if nodo in visited:
            continue
        visited.add(nodo)

        if nodo == goal:
            return traccia_percorso(genitori, start, goal)

        for vicino in grafo.get(nodo, []):
            nuovo_costo = costo + 1  # Supponiamo costo uniforme tra i nodi
            if vicino not in visited:
                genitori[vicino] = nodo
                heapq.heappush(queue, (nuovo_costo, vicino))

    return None

def greedy_search(grafo, start, goal, heuristic):
    """Esegue l'algoritmo Greedy Best-First Search con misurazioni di tempo, memoria e operazioni."""
    operazioni = 0
    tracemalloc.start()
    start_time = time.time()

    open_set = [(0, start)]
    heapq.heapify(open_set)
    genitori = {start: None}

    while open_set:
        _, nodo = heapq.heappop(open_set)
        operazioni += 1

        if nodo == goal:
            execution_time = time.time() - start_time
            current_memory, peak_memory = tracemalloc.get_traced_memory()
            tracemalloc.stop()
            return traccia_percorso(genitori, start, goal), execution_time, peak_memory, operazioni

        for vicino in grafo.get(nodo, []):
            if vicino not in genitori:  # Non visitato
                genitori[vicino] = nodo
                costo = heuristic(vicino, goal)
                heapq.heappush(open_set, (costo, vicino))

    execution_time = time.time() - start_time
    current_memory, peak_memory = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    return None, execution_time, peak_memory, operazioni

# Definiamo una semplice euristica per Greedy Search (ad esempio, la distanza manhattan per nodi numerici)
def heuristic(nodo, goal):
    """Euristica semplice basata sulla differenza assoluta tra nodo e goal."""
    return abs(nodo - goal)

def esegui_ricerca_algoritmoX(grafo, start, goal, algoritmo):
    """Esegue un algoritmo di ricerca specifico e misura il tempo, memoria e operazioni."""
    operazioni = 0
    tracemalloc.start()
    start_time = time.time()

    if algoritmo == 'bfs':
        percorso = bfs(grafo, start, goal)
    elif algoritmo == 'dfs':
        percorso = dfs(grafo, start, goal)
    elif algoritmo == 'a_star':
        percorso = a_star(grafo, start, goal)
    elif algoritmo == 'ucs':
        percorso = uniform_cost_search(grafo, start, goal)
    elif algoritmo == 'greedy':
        percorso, tempo, memoria, operazioni = greedy_search(grafo, start, goal, heuristic)
        return percorso, tempo, memoria, operazioni
    else:
        raise ValueError(f"Algoritmo non supportato: {algoritmo}")

    execution_time = time.time() - start_time
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    operazioni = len(percorso) if percorso else 0
    return percorso, execution_time, peak, operazioni

# GUI con Tkinter per interagire con gli algoritmi
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Algoritmi di Ricerca su Grafo")
        self.grafo = None
        self.file_name = ""

        # Frame per la gestione del caricamento del file
        self.frame_load = tk.Frame(root)
        self.frame_load.pack(pady=10)

        self.button_load = tk.Button(self.frame_load, text="Carica Grafo", command=self.carica_grafo, height=2, width=15)
        self.button_load.pack(side=tk.LEFT, padx=5)

        self.label_file_name = tk.Label(self.frame_load, text="Nessun file caricato")
        self.label_file_name.pack(side=tk.LEFT)

        # Frame per inserire nodi di partenza e arrivo
        self.frame_inputs = tk.Frame(root)
        self.frame_inputs.pack(pady=10)

        self.label_start = tk.Label(self.frame_inputs, text="Nodo di Partenza")
        self.label_start.pack(side=tk.LEFT, padx=5)
        self.entry_start = tk.Entry(self.frame_inputs, width=10)
        self.entry_start.pack(side=tk.LEFT, padx=5)

        self.label_goal = tk.Label(self.frame_inputs, text="Nodo di Arrivo")
        self.label_goal.pack(side=tk.LEFT, padx=5)
        self.entry_goal = tk.Entry(self.frame_inputs, width=10)
        self.entry_goal.pack(side=tk.LEFT, padx=5)

        # Frame per i pulsanti di esecuzione degli algoritmi
        self.frame_buttons = tk.Frame(root)
        self.frame_buttons.pack(pady=10)

        self.button_bfs = tk.Button(self.frame_buttons, text="BFS", command=self.run_bfs, height=2, width=10)
        self.button_bfs.pack(side=tk.LEFT, padx=5)

        self.button_dfs = tk.Button(self.frame_buttons, text="DFS", command=self.run_dfs, height=2, width=10)
        self.button_dfs.pack(side=tk.LEFT, padx=5)

        self.button_a_star = tk.Button(self.frame_buttons, text="A*", command=self.run_a_star, height=2, width=10)
        self.button_a_star.pack(side=tk.LEFT, padx=5)

        self.button_ucs = tk.Button(self.frame_buttons, text="UCS", command=self.run_ucs, height=2, width=10)
        self.button_ucs.pack(side=tk.LEFT, padx=5)

        self.button_greedy = tk.Button(self.frame_buttons, text="Greedy", command=self.run_greedy, height=2, width=10)
        self.button_greedy.pack(side=tk.LEFT, padx=5)

        # Frame per mostrare il risultato
        self.frame_result = tk.Frame(root)
        self.frame_result.pack(pady=10)

        self.text_result = tk.Text(self.frame_result, height=15, width=60)
        self.text_result.pack()

    def carica_grafo(self):
        self.grafo, self.file_name = carica_file_grafo()
        if self.grafo:
            self.label_file_name.config(text=f"File caricato: {self.file_name}")
        else:
            self.label_file_name.config(text="Nessun file caricato")

    def get_input_nodes(self):
        try:
            start = int(self.entry_start.get())
            goal = int(self.entry_goal.get())
            return start, goal
        except ValueError:
            messagebox.showerror("Errore", "Inserisci valori numerici validi per i nodi")
            return None, None

    def mostra_risultato(self, percorso, tempo, memoria, operazioni):
        self.text_result.delete(1.0, tk.END)
        if percorso:
            self.text_result.insert(tk.END, f"Percorso trovato: {percorso}\n")
        else:
            self.text_result.insert(tk.END, "Nessun percorso trovato\n")
        self.text_result.insert(tk.END, f"Tempo di esecuzione: {tempo:.4f} secondi\n")
        self.text_result.insert(tk.END, f"Picco di memoria: {memoria / 1024:.2f} KB\n")
        self.text_result.insert(tk.END, f"Nodi esplorati: {operazioni}\n")

    def run_bfs(self):
        start, goal = self.get_input_nodes()
        if start is not None and goal is not None:
            percorso, tempo, memoria, operazioni = esegui_ricerca_algoritmoX(self.grafo, start, goal, 'bfs')
            self.mostra_risultato(percorso, tempo, memoria, operazioni)

    def run_dfs(self):
        start, goal = self.get_input_nodes()
        if start is not None and goal is not None:
            percorso, tempo, memoria, operazioni = esegui_ricerca_algoritmoX(self.grafo, start, goal, 'dfs')
            self.mostra_risultato(percorso, tempo, memoria, operazioni)

    def run_a_star(self):
        start, goal = self.get_input_nodes()
        if start is not None and goal is not None:
            percorso, tempo, memoria, operazioni = esegui_ricerca_algoritmoX(self.grafo, start, goal, 'a_star')
            self.mostra_risultato(percorso, tempo, memoria, operazioni)

    def run_ucs(self):
        start, goal = self.get_input_nodes()
        if start is not None and goal is not None:
            percorso, tempo, memoria, operazioni = esegui_ricerca_algoritmoX(self.grafo, start, goal, 'ucs')
            self.mostra_risultato(percorso, tempo, memoria, operazioni)

    def run_greedy(self):
        start, goal = self.get_input_nodes()
        if start is not None and goal is not None:
            percorso, tempo, memoria, operazioni = esegui_ricerca_algoritmoX(self.grafo, start, goal, 'greedy')
            self.mostra_risultato(percorso, tempo, memoria, operazioni)

# Inizializzazione dell'app
root = tk.Tk()
app = App(root)
root.mainloop()