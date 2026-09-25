#include<vector>
#include<iostream>
#include<string>

void call_run_container(std::vector<std::string>& vec){
	std::string container_name;
	std::string image_name;
	std::vector<std::string> commands;
	bool detach_mode= false;

	size_t i= 2;

	while(i< vec.size()){
		if(vec[i] == "--name"&& i+1<vec.size()){
			container_name= vec[++i];
		}
		else if((vec[i] == "--detach" || vec[i] == "-d") && image_name.empty()){
			detach_mode = true;
		}
		else if(image_name.empty()){
			image_name= vec[i];
		}
		else{
			commands.push_back(vec[i]);
		}
		++i;
	}

	std::cout<<"- name: run container\n";
	std::cout<<"  containers.podman.podman_container:\n";
	std::cout<<"	image: "<<image_name<<"\n";
	
	if(!container_name.empty()){
		std::cout<<"	name: "<<container_name<<"\n";
	}

	std::cout<<"	state: started\n";
	if(detach_mode){
		std::cout<<"	detach: true\n";
	}

	if(!commands.empty()){
		std::cout<<"	command: ";
		size_t t = 0;
		while(t<commands.size()){
			std::cout<<commands[t]<<(t+1 < commands.size()?" ":"");
			++t;
		}
	std::cout<<std::endl;
	}
}
int main(int argc,char* argv[]){
	std::vector<std::string> args(argv+1,argv + argc);
	
	if(args.size() >=3 && args[0] == "podman" && args[1] == "run"){
			call_run_container(args);
	}
	return 0;
}
