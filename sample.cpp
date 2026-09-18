#include<vector>
#include<iostream>
class parse{
	public:
		std::string container_name;

		parse(const std::string name): container_name(name){
		}

		void display(){
			std::cout<<"- name: get logs for "<<container_name<<"\n";
			std::cout<<"  container.podman.podman_logs:\n";
		}
};
int main(){
	parse pr("tampertrace");
	pr.display();
	return 0;
}
