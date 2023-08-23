#include <iostream>
#include <string.h>
using namespace std;
 
int main(){
    int n;
    cin>>n;
    for(int i = 0;i<n;i++){
        string a;
        cin>>a;
        int c = 0;
        if (a[0] != 'c'){
            c+=1;
        }
        if (a[1] != 'o'){
            c+=1;
        }
        if (a[2] != 'd'){
            c+=1;
        }
        if (a[3] != 'e'){
            c+=1;
        }
        if (a[4] != 'f'){
            c+=1;
        }
        if (a[5] != 'o'){
            c+=1;
        }
        if (a[6] != 'r'){
            c+=1;
        }
        if (a[7] != 'c'){
            c+=1;
        }
        if (a[8] != 'e'){
            c+=1;
        }
        if (a[9] != 's'){
            c+=1;
        }
        
        cout<<c<<endl;
    }
}