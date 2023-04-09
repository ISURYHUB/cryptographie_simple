# Cryptographie Simple

Voici un petit projet que j'ai réalisé sur la cryptographie textuelle afin de pratiquer mon niveau de programmation en Python et d'en apprendre plus sur la cryptographie.

# Fonctionnalité du programme "encrypter":

Ce programme de cryptage convertit un texte en une série de nombres en utilisant une table de correspondance entre les caractères et les nombres.

La variable caracteres est un dictionnaire qui associe chaque caractère à un nombre unique. Les caractères sont triés en ordre alphabétique, avec les majuscules avant les minuscules, puis les caractères spéciaux et les chiffres. Chaque caractère est représenté par une valeur numérique entière allant de 1 à 86, en fonction de son ordre dans le dictionnaire caracteres.

La variable texto est utilisée pour demander à l'utilisateur d'entrer le texte à crypter.

Le programme itère ensuite sur chaque caractère du texte à l'aide d'une boucle for et vérifie si le caractère est présent dans le dictionnaire caracteres. Si le caractère est présent, le programme ajoute la valeur numérique correspondante à la liste numeros.

Ensuite, le programme itère sur chaque élément de la liste numeros à l'aide d'une autre boucle for. Pour chaque élément de la liste, le programme multiplie la valeur par 2 et ajoute 2, et stocke le résultat dans une nouvelle liste appelée resultados.

Enfin, le programme affiche la liste des résultats en les séparant par des espaces en utilisant la méthode join de Python.

En résumé, le programme prend un texte en entrée et le convertit en une liste de nombres en utilisant une table de correspondance pré-définie, où chaque caractère est représenté par un nombre unique. Il multiplie ensuite chaque nombre par 2 et ajoute 2, et stocke les résultats dans une nouvelle liste. Le résultat final est une série de nombres affichés à l'écran.

# Fonctionnalité du programme "decrypter":

Ce programme est un programme de décryptage qui prend en entrée un texte crypté et utilise un dictionnaire pour retrouver les caractères originaux.

Le dictionnaire "caracteres" est utilisé pour stocker chaque caractère possible associé à un numéro de 1 à 86. Chaque numéro est associé à un caractère spécifique, comme la lettre A, le point d'exclamation ou l'espace.

Le programme demande à l'utilisateur de saisir le texte crypté avec la commande "input". Le texte est stocké dans la variable "texto_encriptado".

Le programme commence par décomposer le texte en entrée en une liste de chaînes de caractères séparées par des espaces à l'aide de la méthode "split()". Chaque chaîne de caractères correspond à un numéro crypté.

Le programme itère ensuite sur chaque élément de la liste des numéros cryptés. Pour chaque numéro, il applique la formule (int(numero_encriptado) - 2) // 2 pour récupérer le numéro original. Cette formule fonctionne car lors du cryptage, chaque numéro original a été multiplié par 2, puis additionné à 2. La formule inverse permet de retrouver le numéro original.

Si le numéro original se trouve dans le dictionnaire "caracteres", le programme ajoute ce numéro à une liste appelée "numeros". Si le numéro n'est pas dans le dictionnaire, le programme ne le récupère pas.

Le programme utilise ensuite la méthode "join()" pour combiner tous les caractères décodés dans la liste "numeros" en une chaîne de caractères. Le résultat final est stocké dans la variable "texto_descifrado".

Enfin, le programme affiche le texte décrypté à l'utilisateur à l'aide de la commande "print()".

En résumé, pour décrypter le message crypté, l'opération inverse de celle utilisée dans le programme de cryptage est apliqué, c'est-à-dire la formule inverse : (x - 2) / 2.

# Questions de sécurité :

Le programme donné utilise un chiffrement par substitution, où chaque caractère dans le texte clair est remplacé par un numéro correspondant dans le dictionnaire 'caracteres'. Ensuite, chaque numéro est multiplié par 2 et additionné avec 2 pour obtenir le chiffre final. Ce chiffrement est faible car il est facilement réversible.Voici quelques recommandations pour améliorer le cryptage du code:

Il est recommandé d'utiliser un dictionnaire de caractères plus grand et plus complexe pour rendre l'analyse fréquentielle plus difficile. En outre, il est possible d'appliquer une permutation aléatoire aux caractères avant de les convertir en nombres pour ajouter une couche de complexité supplémentaire.

Utiliser une clé de cryptage: Le code actuel utilise un cryptage à clé fixe, ce qui signifie que la même clé est utilisée à chaque fois que le code est exécuté. Il est recommandé d'utiliser une clé de cryptage unique pour chaque message, ce qui rend le décryptage plus difficile.

Hacher les données avant de les crypter: Le hachage est une méthode de cryptage qui transforme les données en une chaîne de caractères de longueur fixe. Il est recommandé de hacher les données avant de les crypter, car cela rend le décryptage plus difficile.
