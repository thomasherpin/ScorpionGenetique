# ScorpionGenetique
Scorpion Romain - IA - Algorithme génétique

Reproduction des caractéristiques d'un ancien scorpion romain.

Le but est d'utiliser un algorithme génétique afin de trouver le scorpion le plus optimisé, celui qui parviendra à tirer le plus fort en touchant sa cible et en essayant de respecter des limites prédéfinies.

Historique scorpion:
https://leg8.fr/armee-romaine/scorpion-vitruvien

Choix des matériaux:
https://www.simulationmateriaux.com/ComportementMecanique/comportement_mecanique_Liste_modules_de_Young.php

Le graphique final représente un score établi en prenant en compte différents paramètres, tels que:
- La cohérence (physisque) du scorpion
- La portée (300m de base)
- La puissance de tir (correspond à un équivalent TNT)
    https://en.wikipedia.org/wiki/TNT_equivalent

A chaque génération, on affiche également le score, la portée et toutes les caractéristiques du meilleur individu

L'ensemble des règles métiers qui régissent le fonctionnement du scorpion est défini dans le fichier "TP Algorithmes Génétiques"
https://github.com/thomasherpin/ScorpionGenetique/blob/master/TP%20Algorithmes%20g%C3%A9n%C3%A9tiques.pdf


Pour modifier le scorpion et son environnement, les "constantes" définies au début du fichier peuvent être ajuster.
Pour modifier le comportement des générations de scorpions, il faut modifier la fonction de fitness (eval).
