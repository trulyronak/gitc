#include <stdlib.h>
#include <iostream>

int main(int argc, char *argv[]) {
  std::string str = "";

  if (argc < 2) {
    //This is your default commit msg. Change this if you want!
    str = "Quick Commit";
  }

  else {
    for (int j = 1; j < argc; j++) {
      str += argv[j];
      str += " ";
    }
    std::cout << str;
  }
  std::system("git add -A");
  str = "git commit -m '" + str + "'";
  std::system(str.c_str());
  std::system("git status");
  /*
    Uncomment if you want to be extra lazy - don't worry, there are no bad
    consequences to running 'git push' if you don't have any remotes
  */

  //std::system("git push");

  std::cout<< std::endl << std::endl << "Commit Message: " << str << std::endl;

  return 0;
}
