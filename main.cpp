#include <stdlib.h>
#include <iostream>

int main(int argc, char *argv[]) {
  std::string str = "";

  if (argc < 2) {
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

  std::cout<< "Commit Message: " << str << std::endl;

  return 0;
}
