#include<stdio.h>
#include<limits.h>
#include<stdbool.h>
#define MAX 100

int length;

int minDistance(int distance[], bool checkVisited[]) {
    int i, min_index;
    int min = 10000; 
    for(i=1; i<=length; i++) {
        if(!checkVisited[i] && distance[i] <= min) {
            min = distance[i];
            min_index = i;
        }
    }
    return min_index;
}

void printGraph(int distance[]) {
    int i;
    printf("Vertex\t\t\tDistance From Source\n");
    for(i=1; i<=length; i++) {
        printf("%d\t\t\t\t%d\n", i, distance[i]);
    }
}

void dijkstra_algo(int dijkstra[][MAX], int source) {
    int i, j;
    int distance[length];
    bool checkVisited[length];
    
   
    for(i=1; i<=length; i++) {
        distance[i] = (i == source) ? 0 : 999;  
        checkVisited[i] = false;  
    }

    for(i=1; i<=length; i++) {
        int minDist = minDistance(distance, checkVisited);
        checkVisited[minDist] = true;

        for(j=1; j<=length; j++) {
           
            if(!checkVisited[j] && dijkstra[minDist][j] && (distance[minDist] + dijkstra[minDist][j] < distance[j])) {
                distance[j] = distance[minDist] + dijkstra[minDist][j];
            }
        }
    }

    printGraph(distance);
}

int main() {
    int dijkstra[MAX][MAX], i, j, source;
    printf("Enter the number of nodes: ");
    scanf("%d", &length);
    printf("\nEnter the source of the graph: ");
    scanf("%d", &source);
    printf("\nEnter the weighted graph:\n");

   
    for(i=1; i<=length; i++) {
        for(j=1; j<=length; j++) {
            scanf("%d", &dijkstra[i][j]);
        }
    }

    dijkstra_algo(dijkstra, source);
    
    return 0;
}
