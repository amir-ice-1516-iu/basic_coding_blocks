#include<bits/stdc++.h>
#include<argp.h>

using namespace std;

static int parse_opt(int key, char *arg, struct argp_state *state){
    switch(key){
        case 'd':
            printf(".\n");
            break;
    }
    return 0;
}

int main(int argc, char **argv){
    struct argp_option options[]={
        {0,'d',0,0,"Show a dot on the screen"},
        {0}
    };
    struct argp argp = { options, parse_opt };
    return argp_parse(&argp, argc, argv, 0,0,0);
}
