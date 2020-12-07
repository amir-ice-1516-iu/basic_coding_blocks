#include<bits/stdc++.h>
#include <argp.h>

const char *argp_program_bug_address ="amir@nybsys.com";
const char *argp_program_version     ="version 1.0";

static int parse_opt (int key, char *arg, struct argp_state *state)
{
    //int *arg_count = state->input;
    switch (key)
    {
        case 'd':
        {
            unsigned int i;
            unsigned int dots=0;
            if (arg==NULL)
            {
                dots = 1;
                break;
            }
            else
            {
                dots = atoi(arg);
                printf("%s [ ",arg);
            }
            for (i = 0; i < dots; i++)
                printf (".");
            printf (" ] \n");
            break;
        }
        case 's':
        {
            unsigned int i;
            printf("%s [ ",arg);
            for (i = 0; i < atoi (arg); i++)
                printf ("*");
            printf (" ] \n");
            break;
        }
        case 777:
            return parse_opt('d', "3", state);
        case ARGP_KEY_ARG:
        {
            printf("ka");
        }
        case ARGP_KEY_END:
        {
            printf("ke");
        }
    }
return 0;
}

int main (int argc, char **argv)
{
    struct argp_option options[] =
    {
        { "dots", 'd', "NUM", OPTION_ARG_OPTIONAL, "Show some dots on the screen"},
        { "points",0,"NUM", OPTION_ALIAS, "Alias of dots"},
        { "stars", 's', "NUM", 0, "Show some stars on the screen"},
        { "ellipsis", 777, 0, 0, "aliasing with callback"},
        { 0 }
    };
    struct argp ArgumentParser = { options, parse_opt, 0, 0 };
    bool arguments_are_valid = argp_parse (&ArgumentParser, argc, argv, 0, 0, 0);
    if(arguments_are_valid){
    // do the job
    }
    else{
        return arguments_are_valid;
    }
    return 0;
}

