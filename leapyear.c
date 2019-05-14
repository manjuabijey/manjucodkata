#include<stdio.h>
void main()
{
int year;
printf("enter any year");
scanf("%d",&year);
if((year%400)==0)
printf("year is a leap year",year);
if((year%4)==0)
printf("year is a leap year",year);
if((year%100)==0)
printf("year is not a leap year",year);
else
printf("year is not a leap year",year);
}
