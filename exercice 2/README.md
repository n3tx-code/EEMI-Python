## Exercice 14 – Héritage simple (le zoo)

Créez une classe mère `Animal` avec un attribut `nom` initialisé dans le constructeur.  
Créez deux classes filles `Lion` et `Oiseau` qui héritent de `Animal`.  
Instanciez un lion nommé `"Simba"` et un oiseau nommé `"Titi"`, puis affichez leurs noms en utilisant l’attribut hérité.

---

## Exercice 15 – Surcharge de méthode (polymorphisme)

Dans la classe `Animal`, ajoutez une méthode `crier()` qui affiche `"..."`.  
Dans `Lion`, redéfinissez `crier()` pour afficher `"roaar"`.  
Dans `Oiseau`, redéfinissez `crier()` pour afficher `"cui cui"`.  
Testez le polymorphisme en mettant plusieurs animaux (lions et oiseaux) dans une liste, puis parcourez cette liste dans une boucle et appelez `crier()` sur chaque élément.

---

## Exercice 16 – Le mot-clé `super()`

Créez une classe `Personne` avec les attributs `nom` et `age`.  
Créez une classe `Etudiant` qui hérite de `Personne` et qui ajoute un attribut supplémentaire `cursus`.  
Dans le constructeur de `Etudiant`, utilisez `super().__init__(nom, age)` pour initialiser les attributs hérités au lieu de répéter le code.

---

## Exercice 17 – Affichage d’objet (`__str__`)

Créez une classe `Livre` avec les attributs `titre` et `auteur`.  
Montrez que, sans méthode spéciale, `print(mon_livre)` affiche une adresse mémoire peu lisible.  
Implémentez la méthode magique `__str__` pour que `print(mon_livre)` affiche :  
`"Titre : [titre], écrit par [auteur]"`.

---

## Exercice 18 – Création de module

Créez un fichier `math_utils.py` contenant une fonction `carre(x)` qui renvoie le carré de `x`.  
Créez un fichier `main.py` dans le même dossier.  
Dans `main.py`, importez la fonction et utilisez-la pour afficher le carré de `5`.

---

## Exercice 19 – Installation via `pip` (exercice pratique)

Ouvrez votre terminal.  
Créez un environnement virtuel.
Installez la bibliothèque externe `requests` avec la commande `pip install requests`.  
Lancez ensuite la commande `pip freeze` pour voir la liste des paquets installés et vérifier que `requests` apparaît bien.

---

## Exercice 20 – Utilisation d’une bibliothèque externe

Créez un script qui utilise la bibliothèque `requests` pour faire une requête `GET` sur l’URL  
`https://jsonplaceholder.typicode.com/todos/1`.  
Affichez le contenu JSON récupéré avec `response.json()`.

---

## Exercice 21 – Compte bancaire (préparation à l’exercice 22)

Créez une classe `CompteBancaire` avec un attribut `solde` (initialisé par exemple à 0 dans le constructeur).  
Ajoutez une méthode `deposer(self, montant)` qui augmente le solde.  
Ajoutez une méthode `retirer(self, montant)` qui diminue le solde **si** le solde est suffisant ; sinon, affichez un message d’erreur (par exemple avec `print`) et ne modifiez pas le solde.  
Instanciez un compte, effectuez un dépôt puis un retrait, et affichez le solde. Testez aussi un retrait supérieur au solde pour vérifier le message d’erreur.

---

## Exercice 22 – Exception personnalisée

Créez une classe d’erreur `SoldeInsuffisantError` qui hérite de `Exception`.  
Reprenez votre exercice précédent de compte bancaire (classe avec au minimum `solde`, `deposer` et `retirer`).  
Dans la méthode `retirer`, au lieu d’afficher un message d’erreur lorsque le solde est insuffisant, levez l’exception `SoldeInsuffisantError`.  
Écrivez un script de test qui appelle `retirer` dans un bloc `try/except` et intercepte cette exception personnalisée pour afficher un message d’erreur clair.
