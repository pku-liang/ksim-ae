#include <sys/wait.h>
#include<unistd.h>
#include<wait.h>
#include<chrono>
#include<iostream>
namespace chrono=std::chrono;

int main(int argc, char ** argv) {
  auto start = chrono::system_clock::now();
  pid_t pid = fork();
  bool is_microseconds = false;
  if(std::string(argv[1]) == "--us") {
    is_microseconds = true;
    argv++;
  }
  if(pid == 0) {
    return execvp(argv[1], argv + 1);
  }
  else {
    int status;
    waitpid(pid, &status, 0);
    auto stop = chrono::system_clock::now();
    if(is_microseconds) {
      std::cout << chrono::duration_cast<chrono::microseconds>(stop - start).count() << "\n";
    }
    else {
      std::cerr << "Wall Time: " << chrono::duration_cast<chrono::milliseconds>(stop - start).count() << "\n";
    }
    return WEXITSTATUS(status);
  }
}