#include<stdio.h>

int main()
{
char str[100];
FILE *f,*fo;
f=fopen("input.txt","r");
fscanf(f,"%s",str);
fclose(f);

fo=fopen("output.txt","w+");
fprintf(fo,"%s",str);
fclose(fo);
return 0;
}

