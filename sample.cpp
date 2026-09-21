#include<vector>
#include<iostream>
#include<string>

int main(int argc,char* argv[]){
	std::vector<std::string> args(argv+1,argv + argc);
	for(int i =0;i<args.size();i++){
		std::cout<<args[i]<<" ";
	}
	
	return 0;
}
