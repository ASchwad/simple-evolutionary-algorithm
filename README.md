# Simple evolutionary algorithm

Goal: Chromosomes with each 6 random generated numbers between 1 and 6 should reach the state of [1, 2, 3, 4, 5, 6] by using an evolutionary algorithm

## Steps
1. **Create population**
2. **Determine Fitness**  
*My evaluation function provides one point for each correct number at the correct position*
3. **Select mating pool**  
*Selection by elitsm: In descending order by best fittness value two chromosome breed together*
4. **Breed**  
*Crossover at random position. 2 parents -> 2 childs*
5. **Mutate**  
*1% Chance of mutation and random change at random position*
6. **Repeat at 2 until goal / constraints have been reached (e.g. maximum allowed generations)**  
