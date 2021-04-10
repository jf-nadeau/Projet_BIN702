import numpy as np
from operator import itemgetter
import math
import time
import levenshtein
import smithwaterman
import fasta
import jaccard

def read_titles():
    titles = []
    with open(r'C:\Users\JF\Documents\BIN702\titles2.txt', 'r') as file:
        titles = file.readlines()
    return titles

def print_result(algo_name, best_match, start_time):
    print(algo_name)
    print("BEST MATCH: ", best_match.strip())
    print("---execution time: %s seconds ---" % (time.time() - start_time))
    print("")

def main():
    titles = read_titles()
    for P in ["Hidden Treasures Of The Infinite", "Hidden_Treasures_Of_The_Infinite", "Hiden Tresure_Of_de_Infinity", "Hidden The Infinite"]:
        print(P)
        P = P.lower()
        ### LEVENSHTEIN ###
        start_time = time.time()
        bestmatch = ""
        bestscore = math.inf
        for title in titles:
            title = title.lower()
            score = levenshtein.distance(P, title)
            if(score < bestscore):
                bestmatch = title
                bestscore = score
        print_result("LEVENSHTEIN", bestmatch, start_time)


        ### SMITH-WATERMAN ###
        start_time = time.time()
        bestmatch = ""
        bestscore = -math.inf
        for title in titles:
            title = title.lower()
            score = smithwaterman.distance(P, title)
            if(score > bestscore):
                bestmatch = title
                bestscore = score
        print_result("SMITH-WATERMAN", bestmatch, start_time)

        
        ### HOME MADE FASTA ###
        start_time = time.time()
        bestmatch = fasta.find_best_match(P, titles)
        print_result("HOME MADE FASTA + SMITH-WATERMAN", bestmatch, start_time)


        ### JACCARD ###
        start_time = time.time()
        bestmatch = jaccard.find_best_match(P, titles)
        print_result("JACCARD + SMITH-WATERMAN", bestmatch, start_time)

        print("")
if __name__ == "__main__":
    main()