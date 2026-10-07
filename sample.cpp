#include<vector>
#include<iostream>
#include<string>

void call_run_container(std::vector<std::string>& vec){
	std::string container_name;
	std::string image_name;
	std::vector<std::string> commands;
	std::vector<std::string> ports;
	std::vector<std::string> volumes;
	bool detach_mode= false;

	size_t i= 2;

	while(i< vec.size()){
		if((vec[i] == "--name"|| vec[i] == "-n" )&& i+1<vec.size()){
			container_name= vec[++i];
		}
		else if((vec[i] == "--detach" || vec[i] == "-d") && image_name.empty()){
			detach_mode = true;
		}
		else if((vec[i] == "-p" || vec[i] == "--publish")&& i+1<vec.size()){
			ports.push_back(vec[++i]);
		}
		else if((vec[i] == "-v" || vec[i] == "--volume") && i+1 <vec.size()){
			volumes.push_back(vec[++i]);
		}
		else if(image_name.empty()){
			image_name = vec[i];
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
	
	if(!ports.empty()){
		std::cout<<"	ports:\n";
		for(const std::string cmds: ports){
			std::cout<<"		- "<<cmds<<std::endl;
		}
	}
	if(!volumes.empty()){
		std::cout<<"	volumes:\n";
		for(const std::string vlms: volumes){
			std::cout<<"		- "<<vlms<<"\n";
		}
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
