import random as r
import numpy as np
from math import *
import matplotlib.pyplot as plt
#a
ANGLE_HAUSSE = [0,90]
#lb
LONGUEUR_BRAS = [1,150]
#b
BASE_SECTION_DU_BRAS = [1,150]
#h
HAUTEUR_SECTION_DU_BRAS = [1,150]
#Lc
LONGUEUR_CORDE = [1,150]
#Lf
LONGUEUR_FLECHE = [1,30]
#Df
DIAMETRE_FLECHE = [0.01,0.5]
#p
MASSE_VOLUMIQUE = 7850
#E
MODULE_DE_YOUNG = 210
#v
COEFFICIENT_POISSON = [0.24,0.30]
#g en m.s-²
GRAVITE_TERRE = 9.81
#taille population
TAILLE_POPULATION = 10000

def RessortK(COEFFICIENT_POISSON, MODULE_DE_YOUNG):
	RESSORT = (1/3)*(MODULE_DE_YOUNG/(1-(2*COEFFICIENT_POISSON)))
	return RESSORT

def LongueurAVide(LONGUEUR_BRAS,LONGUEUR_CORDE):
    cT = (pow(LONGUEUR_BRAS,2)) - (pow(LONGUEUR_CORDE,2))
    if cT > 0:
        LONGUEUR_A_VIDE = (1/2)*np.sqrt(cT)
    else:
        LONGUEUR_A_VIDE = 0
    return LONGUEUR_A_VIDE

def LongueurDuDeplacement(LONGUEUR_FLECHE,LONGUEUR_A_VIDE):
    LONGUEUR_DEPLACEMENT = LONGUEUR_FLECHE - LONGUEUR_A_VIDE
    return LONGUEUR_DEPLACEMENT

def MasseDuProjectile(MASSE_VOLUMIQUE,DIAMETRE_FLECHE,LONGUEUR_FLECHE):
    MASSE_PROJECTILE = MASSE_VOLUMIQUE*np.pi*pow((DIAMETRE_FLECHE/2),2)*LONGUEUR_FLECHE
    return MASSE_PROJECTILE

def Velocite(RESSORT,LONGUEUR_DEPLACEMENT,MASSE_PROJECTILE):
	VELOCITE = np.sqrt((RESSORT*pow(LONGUEUR_DEPLACEMENT,2))/MASSE_PROJECTILE)
	return VELOCITE

def Portee(VELOCITE,GRAVITE_TERRE,ANGLE_HAUSSE):
    PORTEE = ((pow(VELOCITE,2))/GRAVITE_TERRE)*(np.sin(2*ANGLE_HAUSSE))
    return PORTEE

def EnergieDimpact(MASSE_PROJECTILE,VELOCITE):
    ENERGIE_IMPACT = (MASSE_PROJECTILE*pow(VELOCITE,2))/2
    return ENERGIE_IMPACT

def EquivalenceJouleTNT(EQUIVALENCE_JOULE):
    EQUIVALENCE_TNT = EQUIVALENCE_JOULE/4184
    return EQUIVALENCE_TNT

def MomentQuadratique(BASE_SECTION_DU_BRAS, HAUTEUR_SECTION_DU_BRAS):
    MOMENT_QUADRATIQUE = BASE_SECTION_DU_BRAS*pow(HAUTEUR_SECTION_DU_BRAS, 3) / 12
    return MOMENT_QUADRATIQUE

def ForceTraction(RESSORT, LONGUEUR_DEPLACEMENT):
    FORCE = RESSORT*LONGUEUR_DEPLACEMENT
    return FORCE
    
def Fleche(FORCE, LONGUEUR_BRAS, MODULE_DE_YOUNG, MOMENT_QUADRATIQUE):
    FLECHE = (FORCE*pow(LONGUEUR_BRAS, 3))/(48*MODULE_DE_YOUNG*MOMENT_QUADRATIQUE)
    return FLECHE

# Génération des scorpions aléatoire
def randomScorpions(TaillePopulation,GRAVITE_TERRE,MASSE_VOLUMIQUE,MODULE_DE_YOUNG):
    ListePopulations = []
    for num in range(0,TaillePopulation):
        Individu = {}
        ANGLE_HAUSSE_DEGRE = r.randrange(0,90)
        ANGLE_HAUSSE  = np.radians(ANGLE_HAUSSE_DEGRE)
        LONGUEUR_BRAS = r.randrange(1,150)
        BASE_SECTION_DU_BRAS  = r.randrange(1,150)
        HAUTEUR_SECTION_DU_BRAS  = r.randrange(1,150)
        LONGUEUR_CORDE = r.randrange(1,150)
        LONGUEUR_FLECHE = r.uniform(1,20)
        COEFFICIENT_POISSON  = r.uniform(0.24,0.30)
        DIAMETRE_FLECHE = r.uniform(0.01,0.05)
        RESSORT  = RessortK(COEFFICIENT_POISSON,MODULE_DE_YOUNG)
        #print(RESSORT)
        LONGUEUR_A_VIDE = LongueurAVide(LONGUEUR_BRAS,LONGUEUR_CORDE)
        LONGUEUR_DEPLACEMENT = LongueurDuDeplacement(LONGUEUR_FLECHE,LONGUEUR_A_VIDE)
        MASSE_PROJECTILE = MasseDuProjectile(MASSE_VOLUMIQUE,DIAMETRE_FLECHE,LONGUEUR_FLECHE)
        VELOCITE  = Velocite(RESSORT,LONGUEUR_DEPLACEMENT,MASSE_PROJECTILE)
        PORTEE  = Portee(VELOCITE,GRAVITE_TERRE,ANGLE_HAUSSE)
        ENERGIE_IMPACT = EnergieDimpact(MASSE_PROJECTILE,VELOCITE)
        EQUIVALENCE_TNT = EquivalenceJouleTNT(ENERGIE_IMPACT)
        MOMENT_QUADRATIQUE = MomentQuadratique(BASE_SECTION_DU_BRAS,HAUTEUR_SECTION_DU_BRAS)
        FORCE = ForceTraction(RESSORT,LONGUEUR_DEPLACEMENT)
        FLECHE = Fleche(FORCE,LONGUEUR_BRAS,MODULE_DE_YOUNG,MOMENT_QUADRATIQUE)
        Individu.update({"ANGLE_HAUSSE":ANGLE_HAUSSE,"LONGUEUR_BRAS":LONGUEUR_BRAS,"BASE_SECTION_DU_BRAS":BASE_SECTION_DU_BRAS,"HAUTEUR_SECTION_DU_BRAS":HAUTEUR_SECTION_DU_BRAS,"LONGUEUR_CORDE":LONGUEUR_CORDE,"LONGUEUR_FLECHE":LONGUEUR_FLECHE,"COEFFICIENT_POISSON":COEFFICIENT_POISSON,"RESSORT":RESSORT,"LONGUEUR_A_VIDE":LONGUEUR_A_VIDE,"LONGUEUR_DEPLACEMENT":LONGUEUR_DEPLACEMENT,"DIAMETRE_FLECHE":DIAMETRE_FLECHE,"MASSE_PROJECTILE":MASSE_PROJECTILE,"VELOCITE":VELOCITE,"PORTEE":PORTEE,"ENERGIE_IMPACT":ENERGIE_IMPACT,"EQUIVALENCE_TNT":EQUIVALENCE_TNT,"MOMENT_QUADRATIQUE":MOMENT_QUADRATIQUE,"FORCE":FORCE,"FLECHE":FLECHE})
        ListePopulations.append(Individu)
    return ListePopulations

# Evaluation des individus
def eval(ListePopulations):
    for Individu in ListePopulations:
        Individu["SCORE"] = 100
        if Individu["LONGUEUR_DEPLACEMENT"] <= Individu["FLECHE"]:
            Individu["SCORE"] -= 100
        if Individu["LONGUEUR_A_VIDE"] >= Individu["LONGUEUR_FLECHE"]:
            Individu["SCORE"] -= 100
        if Individu["LONGUEUR_CORDE"] >= Individu["LONGUEUR_BRAS"]:
            Individu["SCORE"] -= 100

        if Individu["PORTEE"] >= 299 and Individu["PORTEE"] < 300:
            Individu["SCORE"] -= 1
        elif Individu["PORTEE"] > 300 and Individu["PORTEE"] <= 301 :
            Individu["SCORE"] -= 1
        elif Individu["PORTEE"] >= 290 and Individu["PORTEE"] < 299:
            Individu["SCORE"] -= 20
        elif Individu["PORTEE"] > 301 and Individu["PORTEE"] <= 310 :
            Individu["SCORE"] -= 20
        elif Individu["PORTEE"] >= 250 and Individu["PORTEE"] < 290 :
            Individu["SCORE"] -= 50
        elif Individu["PORTEE"] > 310 and Individu["PORTEE"] <= 350 :
            Individu["SCORE"] -= 50
        elif Individu["PORTEE"] >= 200 and Individu["PORTEE"] < 250 :
            Individu["SCORE"] -= 70
        elif Individu["PORTEE"] > 350 and Individu["PORTEE"] <= 400:
            Individu["SCORE"] -= 70
        elif Individu["PORTEE"] < 200 or Individu["PORTEE"] > 400:
            Individu["SCORE"] -= 100

        if Individu["EQUIVALENCE_TNT"] >= 100 and Individu["EQUIVALENCE_TNT"] < 1000:
        	Individu["SCORE"] -= 1
        if Individu["EQUIVALENCE_TNT"] >= 10 and Individu["EQUIVALENCE_TNT"] < 100:
        	Individu["SCORE"] -= 2
        if Individu["EQUIVALENCE_TNT"] >= 1 and Individu["EQUIVALENCE_TNT"] < 10:
        	Individu["SCORE"] -= 5
        if Individu["EQUIVALENCE_TNT"] >= 0.3 and Individu["EQUIVALENCE_TNT"] < 1:
        	Individu["SCORE"] -= 10
        if Individu["EQUIVALENCE_TNT"] >= 0.1 and Individu["EQUIVALENCE_TNT"] < 0.3:
            Individu["SCORE"] -= 20
        elif Individu["EQUIVALENCE_TNT"] <= 0.1:
            Individu["SCORE"] -= 30

        if Individu["SCORE"] <= 0:
            Individu["SCORE"] = 1

    return ListePopulations

# Choix de la meilleur liste de populations
def bestPop(POPULATION,TAILLE_POPULATION,GRAVITE_TERRE,MASSE_VOLUMIQUE,MODULE_DE_YOUNG):
	POPULATION_ENFANT = []
	TAILLE_SELECTIONNEE = TAILLE_POPULATION/2

	for i in range(0,int(TAILLE_SELECTIONNEE)):
		MEILLEURS = r.sample(POPULATION,16)

	#Tournoi entre 16 individus, les deux meilleurs sont selectionne pour la population enfant
		if MEILLEURS[0]["SCORE"] > MEILLEURS[1]["SCORE"]:
			MEILLEUR_1_ROUND_1 = MEILLEURS[0]
		else:
			MEILLEUR_1_ROUND_1 = MEILLEURS[1]
		
		if MEILLEURS[2]["SCORE"] > MEILLEURS[3]["SCORE"]:
			MEILLEUR_2_ROUND_1 = MEILLEURS[2]
		else:
			MEILLEUR_2_ROUND_1 = MEILLEURS[3]
		
		if MEILLEURS[4]["SCORE"] > MEILLEURS[5]["SCORE"]:
			MEILLEUR_3_ROUND_1 = MEILLEURS[4]
		else:
			MEILLEUR_3_ROUND_1 = MEILLEURS[5]
		
		if MEILLEURS[6]["SCORE"] > MEILLEURS[7]["SCORE"]:
			MEILLEUR_4_ROUND_1 = MEILLEURS[6]
		else:
			MEILLEUR_4_ROUND_1 = MEILLEURS[7]
		
		if MEILLEURS[8]["SCORE"] > MEILLEURS[9]["SCORE"]:
			MEILLEUR_5_ROUND_1 = MEILLEURS[8]
		else:
			MEILLEUR_5_ROUND_1 = MEILLEURS[9]
		
		if MEILLEURS[10]["SCORE"] > MEILLEURS[11]["SCORE"]:
			MEILLEUR_6_ROUND_1 = MEILLEURS[10]
		else:
			MEILLEUR_6_ROUND_1 = MEILLEURS[11]
		
		if MEILLEURS[12]["SCORE"] > MEILLEURS[13]["SCORE"]:
			MEILLEUR_7_ROUND_1 = MEILLEURS[12]
		else:
			MEILLEUR_7_ROUND_1 = MEILLEURS[13]
		
		if MEILLEURS[14]["SCORE"] > MEILLEURS[15]["SCORE"]:
			MEILLEUR_8_ROUND_1 = MEILLEURS[14]
		else:
			MEILLEUR_8_ROUND_1 = MEILLEURS[15]
		
		if MEILLEUR_1_ROUND_1["SCORE"] > MEILLEUR_2_ROUND_1["SCORE"]:
			MEILLEUR_1_ROUND_2 = MEILLEUR_1_ROUND_1
		else:
			MEILLEUR_1_ROUND_2 = MEILLEUR_2_ROUND_1
		
		if MEILLEUR_3_ROUND_1["SCORE"] > MEILLEUR_4_ROUND_1["SCORE"]:
			MEILLEUR_2_ROUND_2 = MEILLEUR_3_ROUND_1
		else:
			MEILLEUR_2_ROUND_2 = MEILLEUR_4_ROUND_1
		
		if MEILLEUR_5_ROUND_1["SCORE"] > MEILLEUR_6_ROUND_1["SCORE"]:
			MEILLEUR_3_ROUND_2 = MEILLEUR_5_ROUND_1
		else:
			MEILLEUR_3_ROUND_2 = MEILLEUR_6_ROUND_1
		
		if MEILLEUR_7_ROUND_1["SCORE"] > MEILLEUR_8_ROUND_1["SCORE"]:
			MEILLEUR_4_ROUND_2 = MEILLEUR_7_ROUND_1
		else:
			MEILLEUR_4_ROUND_2 = MEILLEUR_8_ROUND_1
		
		if MEILLEUR_1_ROUND_2["SCORE"] > MEILLEUR_2_ROUND_2["SCORE"]:
			MEILLEUR_1_FINAL = MEILLEUR_1_ROUND_2
		else:
			MEILLEUR_1_FINAL = MEILLEUR_2_ROUND_2
		
		if MEILLEUR_3_ROUND_2["SCORE"] > MEILLEUR_4_ROUND_2["SCORE"]:
			MEILLEUR_2_FINAL = MEILLEUR_3_ROUND_2
		else:
			MEILLEUR_2_FINAL = MEILLEUR_4_ROUND_2

		ENFANTS = populationEnfant(MEILLEUR_1_FINAL,MEILLEUR_2_FINAL,GRAVITE_TERRE,MASSE_VOLUMIQUE,MODULE_DE_YOUNG)

		POPULATION_ENFANT.append(ENFANTS)
		POPULATION_ENFANT.append(ENFANTS)

	return POPULATION_ENFANT

#Création de la population enfant
def populationEnfant(PARENT_1, PARENT_2, GRAVITE_TERRE, MASSE_VOLUMIQUE, MODULE_DE_YOUNG):
	INDIVIDU = {}
	ANGLE_HAUSSE = PARENT_1["ANGLE_HAUSSE"]
	LONGUEUR_BRAS = PARENT_1["LONGUEUR_BRAS"]
	BASE_SECTION_DU_BRAS = PARENT_1["BASE_SECTION_DU_BRAS"]
	HAUTEUR_SECTION_DU_BRAS = PARENT_1["HAUTEUR_SECTION_DU_BRAS"]

	LONGUEUR_CORDE = PARENT_2["LONGUEUR_CORDE"]
	LONGUEUR_FLECHE = PARENT_2["LONGUEUR_FLECHE"]
	COEFFICIENT_POISSON = PARENT_2["COEFFICIENT_POISSON"]
	DIAMETRE_FLECHE = PARENT_2["DIAMETRE_FLECHE"]


	toChange = r.randrange(1,100)
	if toChange == 1:
		valueToChange = r.randrange(1,8)
		if valueToChange == 1:
			ANGLE_HAUSSE  = radians(r.randrange(0,90))
		elif valueToChange == 2:
			LONGUEUR_BRAS = r.randrange(1,15)
		elif valueToChange == 3:
			BASE_SECTION_DU_BRAS  = r.randrange(1,15)
		elif valueToChange == 4:
			HAUTEUR_SECTION_DU_BRAS  = r.randrange(1,15)
		elif valueToChange == 5:
			LONGUEUR_CORDE = r.randrange(1,15)
		elif valueToChange == 6:
			LONGUEUR_FLECHE = r.uniform(1,2)
		elif valueToChange == 7:
			COEFFICIENT_POISSON  = r.uniform(0.24,0.30)
		elif valueToChange == 8:
			DIAMETRE_FLECHE = r.uniform(0.01,0.05)


	RESSORT = RessortK(COEFFICIENT_POISSON,MODULE_DE_YOUNG)
	LONGUEUR_A_VIDE = LongueurAVide(LONGUEUR_BRAS,LONGUEUR_CORDE)
	LONGUEUR_DEPLACEMENT = LongueurDuDeplacement(LONGUEUR_FLECHE,LONGUEUR_A_VIDE)
	MASSE_PROJECTILE = MasseDuProjectile(MASSE_VOLUMIQUE,DIAMETRE_FLECHE,LONGUEUR_FLECHE)
	VELOCITE = Velocite(RESSORT,LONGUEUR_DEPLACEMENT,MASSE_PROJECTILE)
	PORTEE = Portee(VELOCITE,GRAVITE_TERRE,ANGLE_HAUSSE)
	ENERGIE_IMPACT = EnergieDimpact(MASSE_PROJECTILE,VELOCITE)
	EQUIVALENCE_TNT = EquivalenceJouleTNT(ENERGIE_IMPACT)
	MOMENT_QUADRATIQUE = MomentQuadratique(BASE_SECTION_DU_BRAS,HAUTEUR_SECTION_DU_BRAS)
	FORCE = ForceTraction(RESSORT,LONGUEUR_DEPLACEMENT)
	FLECHE = Fleche(FORCE,LONGUEUR_BRAS,MODULE_DE_YOUNG,MOMENT_QUADRATIQUE)

	INDIVIDU.update({"ANGLE_HAUSSE":ANGLE_HAUSSE,"LONGUEUR_BRAS":LONGUEUR_BRAS,"BASE_SECTION_DU_BRAS":BASE_SECTION_DU_BRAS,"HAUTEUR_SECTION_DU_BRAS":HAUTEUR_SECTION_DU_BRAS,"LONGUEUR_CORDE":LONGUEUR_CORDE,"LONGUEUR_FLECHE":LONGUEUR_FLECHE,"COEFFICIENT_POISSON":COEFFICIENT_POISSON,"RESSORT":RESSORT,"LONGUEUR_A_VIDE":LONGUEUR_A_VIDE,"LONGUEUR_DEPLACEMENT":LONGUEUR_DEPLACEMENT,"DIAMETRE_FLECHE":DIAMETRE_FLECHE,"MASSE_PROJECTILE":MASSE_PROJECTILE,"VELOCITE":VELOCITE,"PORTEE":PORTEE,"ENERGIE_IMPACT":ENERGIE_IMPACT,"EQUIVALENCE_TNT":EQUIVALENCE_TNT,"MOMENT_QUADRATIQUE":MOMENT_QUADRATIQUE,"FORCE":FORCE,"FLECHE":FLECHE})

	return INDIVIDU


population = []
ybetter = []
yaverage = []
yless = []
xgeneration = []
generation = 100

# Génération de la population
population = randomScorpions(TAILLE_POPULATION,GRAVITE_TERRE,MASSE_VOLUMIQUE,MODULE_DE_YOUNG)

# Pour chaque génération : 
for i in range(0,generation):
# l'évaluer
	population = eval(population)

	print(" Génération %i" % i)
	# Gestion des listes pour l'affichage des courbes
	best_score = 0
	less_score = 0
	listaverage = []
	xgeneration.append(i)
	for indiv in population:

		listaverage.append(indiv["SCORE"])
		if indiv["SCORE"] > best_score:
			best_score = indiv["SCORE"]
			bestIndiv = indiv
		if indiv["SCORE"] < less_score:
			less_score = indiv["SCORE"]

	avg_score = np.average(listaverage)

	yaverage.append(avg_score)
	ybetter.append(best_score)
	yless.append(less_score)
	
	print(bestIndiv["SCORE"])
	print(bestIndiv["PORTEE"])
	print(bestIndiv)
	#print(bestIndiv["EQUIVALENCE_TNT"])
	#print(bestIndiv["ANGLE_HAUSSE"])

		
# Génération de la population enfant
	population = bestPop(population, TAILLE_POPULATION,GRAVITE_TERRE,MASSE_VOLUMIQUE,MODULE_DE_YOUNG)

# Affichage des courbes (Meilleur, moins bon et moyenne de la population pour chaque génération)
plt.plot(xgeneration, ybetter,'r',xgeneration,yaverage,'b',xgeneration,yless,'g')
plt.ylabel('scores')
plt.xlabel('génération')
plt.show()