## Exercices Python – Bases


### Exercice 1 – Variables et types (TVA)

**Objectif**: manipuler des variables numériques et afficher une phrase formatée.

**Consignes**:

- Définissez un prix hors taxe (`prix_ht`) et un taux de TVA (`taux`).
- Calculez le prix toutes taxes comprises (`ttc`).
- Affichez une phrase formatée, par exemple :  
  `Pour un prix de X€ HT avec un taux de Y%, le prix TTC est de Z€.`

---

### Exercice 2 – Contrôle de flux (Menu du jour)

**Objectif**: pratiquer `if/elif/else` sans logique de réduction.

**Consignes**:

- Demandez à l’utilisateur de choisir un type de repas avec `input()` :  
  `"1"` pour **petit-déjeuner**  
  `"2"` pour **déjeuner**  
  `"3"` pour **dîner**
- Selon le choix, affichez un menu différent, par exemple :
  - Si `1` → affichez un menu petit-déjeuner (boisson chaude, tartines, jus, etc.).
  - Si `2` → affichez un menu déjeuner (plat, accompagnement, dessert, etc.).
  - Si `3` → affichez un menu dîner (soupe, plat léger, etc.).
- Si l’utilisateur entre une autre valeur, affichez un message d’erreur :  
  `"Choix invalide, veuillez entrer 1, 2 ou 3."`

---

### Exercice 3 – Boucles et listes (Stock)

**Objectif**: parcourir une liste avec une boucle.

**Données**:

```python
ventes = [12.5, 8.0, 4.5, 19.9, 10.0]
```

**Consignes**:

- Calculez la somme totale des ventes avec une boucle `for`.
- Comptez le nombre d’articles dont le prix est strictement supérieur à 10 €.

---

### Exercice 4 – Dictionnaires (Employé)

**Objectif**: manipuler les clés et valeurs d’un dictionnaire.

**Données**:

```python
employe = {"nom": "Dupont", "poste": "dev", "salaire": 2500}
```

**Consignes**:

- Augmentez le salaire de 200 €.
- Ajoutez la clé `"anciennete"` avec la valeur `5`.
- Affichez le dictionnaire complet.

---

### Exercice 5 – Fonctions (Refactorisation)

**Objectif**: encapsuler une logique dans une fonction réutilisable.

**Consignes**:

- Créez une fonction `calculer_ttc(prix_ht, taux)` qui retourne le prix TTC.
- Testez-la avec au moins **deux montants différents** et affichez les résultats.

---

### Exercice 6 – Projet fil rouge (Le juste prix)

**Objectif**: combiner variables, boucles, conditions et entrée utilisateur.

**Consignes**:

- Utilisez `import random` pour générer un nombre secret entre 0 et 100.
- Demandez à l’utilisateur de deviner ce nombre dans une boucle `while`.
- Après chaque tentative :
  - Si la proposition est trop basse, affichez `"C'est plus"`.
  - Si elle est trop haute, affichez `"C'est moins"`.
- Continuez jusqu’à ce que l’utilisateur trouve le bon nombre, puis affichez un message de victoire.

---

### Exercice 7 – Chaînes de caractères (Compteur de voyelles)

**Objectif**: parcourir une chaîne de caractères et compter des éléments.

**Consignes**:

- Demandez un mot à l’utilisateur via `input()`.
- Parcourez ce mot avec une boucle et comptez le nombre de voyelles (`a, e, i, o, u, y`).
- Affichez le total de voyelles trouvées.

---

### Exercice 8 – Listes et filtres (Nombres pairs)

**Objectif**: filtrer des éléments d’une liste.

**Données**:

```python
nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

**Consignes**:

- Créez une nouvelle liste vide `pairs = []`.
- Parcourez la liste `nombres` et ajoutez uniquement les nombres pairs dans `pairs`.
- Affichez la liste `pairs` finale.

---

### Exercice 9 – Gestion des erreurs (Créateur de pizza)

**Objectif**: utiliser `try/except` pour sécuriser des choix et des nombres saisis par l’utilisateur.

**Consignes**:

- Affichez une liste de tailles de pizza :
  - `1` → Petite (8 €)
  - `2` → Moyenne (10 €)
  - `3` → Grande (12 €)
- Demandez à l’utilisateur :
  - de choisir une taille (1, 2 ou 3),
  - de saisir le **nombre de suppléments** (ingrédients en plus) à 1 € chacun.
- Utilisez `try/except` pour convertir les saisies en nombres (`int`).
- Gérez les cas suivants avec des messages clairs :
  - Saisie non numérique (`ValueError`),
  - Taille invalide (pas 1, 2 ou 3),
  - Nombre négatif de suppléments.
- Si tout est valide, calculez et affichez le **prix total** de la pizza.

---

### Exercice 10 – Logique algorithmique (FizzBuzz)

**Objectif**: combiner conditions et boucles.

**Consignes**:

- Bouclez sur les nombres de 1 à 20.
- Pour chaque nombre :
  - S’il est divisible par 3, affichez `"Fizz"`.
  - S’il est divisible par 5, affichez `"Buzz"`.
  - S’il est divisible par 3 **et** 5, affichez `"FizzBuzz"`.
  - Sinon, affichez simplement le nombre.

---

### Exercice 11 – Dictionnaires (Comptage de lettres)

**Objectif**: compter des fréquences avec un dictionnaire.

**Consignes**:

- Demandez une phrase à l’utilisateur.
- Créez un dictionnaire qui compte combien de fois chaque lettre apparaît.  
  Exemple : `"aaabb"` → `{'a': 3, 'b': 2}`.

---

### Exercice 12 – Fonctions (Convertisseur de température)

**Objectif**: écrire et utiliser une fonction de conversion.

**Consignes**:

- Créez une fonction `celsius_vers_fahrenheit(celsius)` qui applique la formule :  
  \((celsius * 9 / 5) + 32\)  
  et retourne le résultat.
- Demandez une température en Celsius à l’utilisateur.
- Appelez la fonction et affichez la température convertie en Fahrenheit.

---

### Exercice 13 – Algorithme (Inversion manuelle)

**Objectif**: manipuler une liste sans utiliser les raccourcis Python.

**Données**:

```python
ma_liste = [10, 20, 30, 40]
```

**Consignes**:

- Sans utiliser la méthode `.reverse()` ni le slicing `[::-1]`, écrivez un algorithme qui inverse l’ordre des éléments pour obtenir `[40, 30, 20, 10]`.
- Indice : vous pouvez utiliser une deuxième liste vide et insérer les éléments au début.