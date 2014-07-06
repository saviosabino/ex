#include <stdio.h>

int sum(int n){
    unsigned long x = 0; int y;
    for(y = 0; y < n; y++){
        x++;
    }
    return x;
}

void main(int argc, char *argv[]){
    printf("%d\n", atol(argv[1]));
    printf("%d\n", sum(atol(argv[1])));
}

