#include<stdio.h>
#define MAX 100

int n;
int C[MAX][MAX],distance[MAX];
int i,j,k;
int u,v;
void print_dist(int distance[]){
    printf("\nVextex Distance\n");
    for(i=1;i<=n;i++){
        printf("%d %d\n",i,distance[i]);
    }
}
void bellmanford(int C[][MAX],int source){
    distance[source] = 0;
    for(k=1;k<=n-1;k++){
        for(v=1;v<=n;v++){
            for(u=1;u<=n;u++){
                if(C[u][v] && distance[v]> C[u][v]+ distance[u]){
                    distance[v] = C[u][v]+ distance[u];
                }
            }
            
        }
        for(v=1;v<=n;v++){
            for(u=1;u<=n;u++){
                if(C[u][v] && distance[v]> C[u][v]+ distance[u]){
                    printf("\nNegative cycle detected");
                }
            }
            
        }
        
    }
    print_dist(distance);
}



int main(){
    int source;
    printf("Enter the number of vertices: ");
    scanf("%d",&n);
    printf("\nEnter cost matrix: \n");
    for(i=1;i<=n;i++){
        for(j=1;j<=n;j++){
            scanf("%d",&C[i][j]);
        }
    }
    printf("\nEnter source: ");
    scanf("%d",&source);
    for(i=1;i<=n;i++){
        distance[i] = 10000;
    }

bellmanford(C,source);

    return 0;
}