#include<bits/stdc++.h>
#include<argp.h>
using namespace std;

int main(int argc, char **argv){
    if (argc>0){
        printf("%s\n",argv[argc-1]);
    }
    return argp_parse(0, argc, argv, 0, 0, 0);
}
