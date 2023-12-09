def solution(bandage, health, attacks):
    max_health = health
    health -= attacks[0][1]
    for i in range(1,len(attacks)):
        tmp = attacks[i][0] - attacks[i-1][0]-1
        health = min(max_health,health + (tmp//bandage[0])*bandage[2] + tmp*bandage[1])
        health -= attacks[i][1]
        
        if health <= 0:
            return -1
        
    return health