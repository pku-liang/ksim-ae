#include <sys/wait.h>
#include<unistd.h>
#include<wait.h>
#include<chrono>
#include<iostream>
namespace chrono=std::chrono;

int main(int argc, char ** argv) {
  auto start = chrono::system_clock::now();
  pid_t pid = fork();
  if(pid == 0) {
    return execvp(argv[1], argv + 1);
  }
  else {
    int status;
    waitpid(pid, &status, 0);
    auto stop = chrono::system_clock::now();
    std::cerr << "Wall Time: " << chrono::duration_cast<chrono::milliseconds>(stop - start).count() << "\n";
    return WEXITSTATUS(status);
  }
}