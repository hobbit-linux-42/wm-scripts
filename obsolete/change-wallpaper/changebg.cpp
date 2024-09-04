#include <string>
#include <iostream>
#include <filesystem>
#include <stdlib.h> 
#include <thread>
#include <unistd.h>
using namespace std;
namespace fs = filesystem;

void changebg(string path){
  cout<<"change bg in to "<<path<<endl;
  system(("swaybg -m fill -i "+path).c_str());
}

int main(){
  while(true){
    string path = "/home/gian42/Immagini/SFONDI";
    for (const auto & entry : fs::directory_iterator(path)) {
      string image = entry.path();
      thread bg(changebg, image);
      sleep(120);
      bg.detach();
      system("killall swaybg");
      sleep(5);
    }
  }  
  return 0;
}
