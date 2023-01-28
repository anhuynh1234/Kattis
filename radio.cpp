#include <iostream>
using namespace std;

int main(){
  int n, p;
  cin >> n >> p;
  int group[n];
  int max_sub = 0;
  for (int i = 0; i < n; i++){
    cin >> group[i];
  }
  max_sub = group[0];
  for (int j = 1; j < n; j++){
    max_sub = max(group[j]+max_sub, max_sub);
  }
  cout << max_sub << endl;
}