#include<iostream>
using namespace std;

int main(){
	int opcion;
    int a;
    
	do{
		cout<<"Menu de opciones:\n";
		cout<<"1. Opcion 1\n";
		cout<<"2. Opcion 2\n";
		cout<<"3. Opcion 3\n";
		cin>>opcion;
		if(opcion!=3) cout<<"Has elegido la opcion"<<opcion<<"\n";
	}while(opcion!=3);
	
	cout<<"Has elegido salir";
	
	return 0;
}