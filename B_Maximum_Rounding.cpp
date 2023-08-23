#include <iostream>
using namespace std;

int main() {
  int tes; 
  cin >> tes;
  while (tes--) {
    string st; cin >> st;
    int i = 0;
    while (st[i] < '5' && i < st.length()) {
      i++;}
    if (i == st.length()) {
      cout << st << endl;}
    else {
      for (int m = i + 1; m < st.length(); m++) {
        st[m] = '0';
      }
      for (int m = i; m > 0; m--) {
        if (st[m] >= '5') {
          st[m - 1] += 1;
          st[m] = '0';
        }
      }
      if (st[0] >= '5') {
        cout << 10;
      }
      else cout << st[0];
      for (int i = 1; i < st.length(); i++) cout << st[i];
      cout << endl;
    }
  }
  return 0;
}