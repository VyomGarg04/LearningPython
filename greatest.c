#include<stdio.h>

int main(){
    int a,b;
    printf("Enter two numbers\n");
    scanf("%d %d",&a,&b);

    if(a<b){
        printf("Greatest = %d",b);
    }
    else if(a>b){
        printf("Greatest = %d",a);
    }
    else
        printf("Equal");

}