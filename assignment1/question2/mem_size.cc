/*Program to find the memory size of datatypes int,
float, bool, and char*/

#include<iostream>
#include<limits.h>
#include<cfloat>
using namespace std;

int main(){
    cout<<"Size of int is "<<sizeof(int)<<" bytes"<<endl;
    cout<<"Size of float is "<<sizeof(float)<<" bytes"<<endl;
    cout<<"Size of bool is "<<sizeof(bool)<<" bytes"<<endl;
    cout<<"Size of char is "<<sizeof(char)<<" bytes"<<endl;

    cout<<"Maximum and minimum value of int is: "<<INT_MAX<< " and "<< INT_MIN<<endl;
    cout<<"Maximum and minimum value of long int is: "<<LONG_MAX<< " and "<< LONG_MIN<<endl;
    cout<<"Maximum and minimum value of float is: "<<FLT_MAX<< " and "<< FLT_MIN<<endl;
    return 0;
}
