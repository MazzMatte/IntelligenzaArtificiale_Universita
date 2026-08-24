# Intelligenza Artificiale Universita
> **Progetto per il corso di Fondamenti di  Intelligenza Artificiale** > Corso di Laurea in Ingegneria Informatica - Università di Napoli Federico Secondo, UNINA

---

# Analisi e Confronto di Algoritmi di Ricerca su un Dataset Reale[cite: 1]

## 🎯 Obiettivo del Progetto
Il progetto ha l'obiettivo di analizzare e confrontare le prestazioni di vari algoritmi di ricerca del cammino su un dataset reale rappresentato dalla rete di coacquisti di Amazon, aggiornata a marzo 2002[cite: 1]. Il dataset viene utilizzato per testare algoritmi di ricerca classici, evidenziando i tempi di esecuzione, l'uso della memoria e la complessità operativa per ciascun approccio[cite: 1].

## 📊 Dataset Utilizzato
*   **Nome del file:** `Amazon0302.txt`[cite: 1]
*   **Descrizione:** Il dataset contiene un grafo diretto che rappresenta le vendite su Amazon[cite: 1].
*   **Struttura del Grafo:** 
    *   **Nodi (262.111):** Ogni nodo rappresenta un prodotto[cite: 1].
    *   **Archi (1.234.877):** Ogni arco diretto rappresenta la relazione "i clienti che hanno acquistato questo articolo hanno acquistato anche"[cite: 1].

## 🧠 Algoritmi di Ricerca Implementati
1.  **Breadth-First Search (BFS):** Ricerca in ampiezza che garantisce di trovare il percorso più corto in un grafo non pesato[cite: 1].
2.  **Depth-First Search (DFS):** Ricerca in profondità che esplora ogni ramo fino alla sua fine prima di tornare indietro; potrebbe non trovare il percorso ottimale[cite: 1].
3.  **A*:** Ricerca euristica adatta per grafi pesati che utilizza una funzione euristica per trovare il cammino ottimale[cite: 1].
4.  **Uniform Cost Search (UCS):** Variante della BFS (Algoritmo di Dijkstra) che esplora sempre il percorso con il costo accumulato più basso per trovare il percorso a costo minimo[cite: 1].
5.  **Greedy Search:** Utilizza una funzione euristica per guidare la ricerca verso l'obiettivo, concentrandosi sulla prossimità senza garantire il percorso ottimale[cite: 1].

## 🛠️ Tecnologie e Strumenti
*   **Linguaggio:** Python[cite: 1]
*   **Librerie standard:** `time` per monitorare il tempo di esecuzione, `tracemalloc` per il consumo di memoria, e `heapq` per gestire le code con priorità[cite: 1].
*   **Interfaccia Grafica:** Sviluppata con Tkinter (GUI) per permettere di caricare il file del grafo, selezionare l'algoritmo di ricerca e visualizzare visivamente i risultati[cite: 1].

## 📈 Risultati e Osservazioni
I test, effettuati ricercando percorsi di varie dimensioni (fino a 200.000 nodi), hanno rivelato le seguenti dinamiche[cite: 1]:
*   **BFS:** Trova sempre il percorso più breve nei grafi non pesati ed è generalmente estremamente rapido, ma possiede picchi di memoria relativamente elevati a causa dell'esplorazione in ampiezza[cite: 1].
*   **DFS:** Tende a trovare soluzioni estremamente lunghe e non ottimali, con performance temporali e di memoria molto imprevedibili e variabili[cite: 1].
*   **A*:** Trova sempre il percorso a costo minimo ed risulta tra i più rapidi e consistenti, sebbene il consumo di memoria sia significativo a causa della coda di priorità[cite: 1].
*   **UCS:** Garantisce di trovare il percorso a costo minimo, ma tende ad essere leggermente più lento rispetto a A* e BFS a causa dell'overhead della coda di priorità[cite: 1].
*   **Greedy Search:** Non garantisce l'ottimalità del percorso e tende a trovare soluzioni estremamente lunghe; ha tempi di esecuzione e picchi di memoria altamente variabili[cite: 1].
