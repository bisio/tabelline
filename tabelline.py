
import itertools
import random


N_LIVES = 3

def get_combinations():
    combinations = []
    for x,y in itertools.combinations(range(2,10),2):
        combinations.append((x,y))
        combinations.append((y,x))
    random.shuffle(combinations)
    return combinations

if __name__ == "__main__":
    lives = N_LIVES
    points = 0
    for x,y in get_combinations():
        if lives < 0:
            break
        while True:
            try:
                response = input("%d x %d = " %  (x,y))
                result = int(response.strip())
                break
            except:
                pass

        if  result != x*y:
            lives -= 1
            if lives >= 0:
                print("Errore! Fa %d hai ancora %d vite punteggio: %d " % (x*y,lives,points))
            else: 
                print("Errore! Fa %d " % (x*y,))
        else:
            points +=1
            print("Bene! punteggio: %d" % (points,))
        
    print("Partita conclusa con %d punti" % points)

