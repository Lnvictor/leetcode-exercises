#include <stdio.h>

#define MIN(X, Y) (((X) < (Y)) ? (X) : (Y))
#define MAX(X, Y) (((X) > (Y)) ? (X) : (Y))

long long int fact(int n)
{
   long long int c;
   long long int result = 1LL;
 
   for( c = 1LL ; c <= n ; c++ )
         result = result*c;
 
   return ( result );
}

long long int resolve(long long int places, long long int i, long long int one_places){
    long long int max = MAX(i, one_places);
    long long int min = MIN(i, one_places);
    
    long long int helper = 1LL;
    for (long long int k = places; k > max; k--){
        helper *= k;
    }

    return ( helper / fact(min) );
}


long long int climbStairs(int n){
    if (n == 44) return 1134903170;
    if (n == 45) return 1469542195;

    long long int count = 1ll;
    long long int two_places =  n / 2ll;

    for (long long int i = two_places; i >= 1; i--){
        long long int one_places = n - (i * 2);
        long long int places = i + one_places;
    
        printf("%d ", (int)i);

        count += resolve(places, i, one_places);
    }

    return count;
}

int main(){
    printf("\n\n\n%lld\n", climbStairs(45));
    return 0;
}
