#include<vector>
#include<iostream>
#include<string>

void call_run_container(std::vector<std::string>& vec){
        std::string container_name;
        std::string image_name;
        std::string network_mode;
        std::string restart_policy;
        std::string workdir;
        std::string host_name;
        std::string user;
        std::string memory_limit;
        std::string cpus_limit;
        std::string shm_size;
        std::string mac_address;
        std::string ip_address;
        std::string log_driver;
        bool priv_mode = false;
        bool auto_remove = false;
        bool read_only_mode = false;
        bool init_mode = false;
        bool detach_mode = false;

        std::vector<std::string> commands;
        std::vector<std::string> ports;
        std::vector<std::string> volumes;
        std::vector<std::string> envs;
        std::vector<std::string> labels;
        std::vector<std::string> devices;
        std::vector<std::string> cap_adds;
        std::vector<std::string> cap_drops;
        std::vector<std::string> dns_servers;
        std::vector<std::string> extra_hosts;
        std::vector<std::string> sysctls;
        std::vector<std::string> ulimits;
        std::vector<std::string> security_opts;
        std::vector<std::string> tmpfs_mounts;
        std::vector<std::string> log_opts;

        size_t i = 2;

        while(i < vec.size()){
                if((vec[i] == "--name" || vec[i] == "-n") && i + 1 < vec.size()){
                        container_name = vec[++i];
                }
                else if((vec[i] == "--detach" || vec[i] == "-d")){
                        detach_mode = true;
                }
                else if((vec[i] == "-p" || vec[i] == "--publish") && i + 1 < vec.size()){
                        ports.push_back(vec[++i]);
                }
                else if((vec[i] == "-v" || vec[i] == "--volume") && i + 1 < vec.size()){
                        volumes.push_back(vec[++i]);
                }
                else if((vec[i] == "-e" || vec[i] == "--env") && i + 1 < vec.size()){
                        envs.push_back(vec[++i]);
                }
                else if((vec[i] == "-l" || vec[i] == "--label") && i + 1 < vec.size()){
                        labels.push_back(vec[++i]);
                }
                else if(vec[i] == "--device" && i + 1 < vec.size()){
                        devices.push_back(vec[++i]);
                }
                else if(vec[i] == "--cap-add" && i + 1 < vec.size()){
                        cap_adds.push_back(vec[++i]);
                }
                else if(vec[i] == "--cap-drop" && i + 1 < vec.size()){
                        cap_drops.push_back(vec[++i]);
                }
                else if(vec[i] == "--dns" && i + 1 < vec.size()){
                        dns_servers.push_back(vec[++i]);
                }
                else if(vec[i] == "--add-host" && i + 1 < vec.size()){
                        extra_hosts.push_back(vec[++i]);
                }
                else if(vec[i] == "--memory" && i + 1 < vec.size()){
                        memory_limit = vec[++i];
                }
                else if(vec[i] == "--cpus" && i + 1 < vec.size()){
                        cpus_limit = vec[++i];
                }
                else if(vec[i] == "--shm-size" && i + 1 < vec.size()){
                        shm_size = vec[++i];
                }
                else if(vec[i] == "--sysctl" && i + 1 < vec.size()){
                        sysctls.push_back(vec[++i]);
                }
                else if(vec[i] == "--ulimit" && i + 1 < vec.size()){
                        ulimits.push_back(vec[++i]);
                }
                else if(vec[i] == "--security-opt" && i + 1 < vec.size()){
                        security_opts.push_back(vec[++i]);
                }
                else if(vec[i] == "--tmpfs" && i + 1 < vec.size()){
                        tmpfs_mounts.push_back(vec[++i]);
                }
                else if(vec[i] == "--read-only"){
                        read_only_mode = true;
                }
                else if(vec[i] == "--mac-address" && i + 1 < vec.size()){
                        mac_address = vec[++i];
                }
                else if(vec[i] == "--ip" && i + 1 < vec.size()){
                        ip_address = vec[++i];
                }
                else if(vec[i] == "--init"){
                        init_mode = true;
                }
                else if(vec[i] == "--log-driver" && i + 1 < vec.size()){
                        log_driver = vec[++i];
                }
                else if(vec[i] == "--log-opt" && i + 1 < vec.size()){
                        log_opts.push_back(vec[++i]);
                }
                else if((vec[i] == "--network" || vec[i] == "--net") && i + 1 < vec.size()){
                        network_mode = vec[++i];
                }
                else if(vec[i] == "--restart" && i + 1 < vec.size()){
                        restart_policy = vec[++i];
                }
                else if((vec[i] == "--workdir" || vec[i] == "-w") && i + 1 < vec.size()){
                        workdir = vec[++i];
                }
                else if(vec[i] == "--privileged"){
                        priv_mode = true;
                }
                else if(vec[i] == "--rm"){
                        auto_remove = true;
                }
                else if(vec[i] == "--hostname" && i + 1 < vec.size()){
                        host_name = vec[++i];
                }
                else if((vec[i] == "--user" || vec[i] == "-u") && i + 1 < vec.size()){
                        user = vec[++i];
                }
                else if(image_name.empty()){
                        image_name = vec[i];
                }
                else{
                        commands.push_back(vec[i]);
                }
                ++i;
        }

        std::cout << "- name: run container\n";
        std::cout << "  containers.podman.podman_container:\n";
        std::cout << "    image: " << image_name << "\n";

        if(!container_name.empty()){
                std::cout << "    name: " << container_name << "\n";
        }
        if(!host_name.empty()){
                std::cout << "    hostname: \"" << host_name << "\"\n";
        }
        if(!user.empty()){
                std::cout << "    user: \"" << user << "\"\n";
        }
        if(!network_mode.empty()){
                std::cout << "    network: " << network_mode << "\n";
        }
        if(!restart_policy.empty()){
                std::cout << "    restart_policy: \"" << restart_policy << "\"\n";
        }
        if(!workdir.empty()){
                std::cout << "    workdir: \"" << workdir << "\"\n";
        }
        if(priv_mode){
                std::cout << "    privileged: true\n";
        }
        if(auto_remove){
                std::cout << "    rm: true\n";
        }
        if(read_only_mode){
                std::cout << "    read_only: true\n";
        }
        if(init_mode){
                std::cout << "    init: true\n";
        }
        if(!memory_limit.empty()){
                std::cout << "    memory: \"" << memory_limit << "\"\n";
        }
        if(!cpus_limit.empty()){
                std::cout << "    cpus: " << cpus_limit << "\n";
        }
        if(!shm_size.empty()){
                std::cout << "    shm_size: \"" << shm_size << "\"\n";
        }
        if(!mac_address.empty()){
                std::cout << "    mac_address: \"" << mac_address << "\"\n";
        }
        if(!ip_address.empty()){
                std::cout << "    ip: \"" << ip_address << "\"\n";
        }
        if(!log_driver.empty()){
                std::cout << "    log_driver: \"" << log_driver << "\"\n";
        }
        if(!ports.empty()){
                std::cout << "    ports:\n";
                for(const std::string& cmds : ports){
                        std::cout << "      - \"" << cmds << "\"\n";
                }
        }
        if(!volumes.empty()){
                std::cout << "    volumes:\n";
                for(const std::string& vlms : volumes){
                        std::cout << "      - \"" << vlms << "\"\n";
                }
        }
        if(!devices.empty()){
                std::cout << "    device:\n";
                for(const std::string& dev : devices){
                        std::cout << "      - \"" << dev << "\"\n";
                }
        }
        if(!dns_servers.empty()){
                std::cout << "    dns:\n";
                for(const std::string& dns : dns_servers){
                        std::cout << "      - \"" << dns << "\"\n";
                }
        }
        if(!cap_adds.empty()){
                std::cout << "    cap_add:\n";
                for(const std::string& cap : cap_adds){
                        std::cout << "      - \"" << cap << "\"\n";
                }
        }
        if(!cap_drops.empty()){
                std::cout << "    cap_drop:\n";
                for(const std::string& cap : cap_drops){
                        std::cout << "      - \"" << cap << "\"\n";
                }
        }
        if(!sysctls.empty()){
                std::cout << "    sysctl:\n";
                for(const std::string& sys : sysctls){
                        size_t eq = sys.find('=');
                        if(eq != std::string::npos){
                                std::cout << "      " << sys.substr(0, eq) << ": \"" << sys.substr(eq + 1) << "\"\n";
                        }
                }
        }
        if(!ulimits.empty()){
                std::cout << "    ulimit:\n";
                for(const std::string& ulm : ulimits){
                        std::cout << "      - \"" << ulm << "\"\n";
                }
        }
        if(!security_opts.empty()){
                std::cout << "    security_opt:\n";
                for(const std::string& sec : security_opts){
                        std::cout << "      - \"" << sec << "\"\n";
                }
        }
        if(!tmpfs_mounts.empty()){
                std::cout << "    tmpfs:\n";
                for(const std::string& tmp : tmpfs_mounts){
                        std::cout << "      - \"" << tmp << "\"\n";
                }
        }
        if(!log_opts.empty()){
                std::cout << "    log_opt:\n";
                for(const std::string& logopt : log_opts){
                        size_t eq = logopt.find('=');
                        if(eq != std::string::npos){
                                std::cout << "      " << logopt.substr(0, eq) << ": \"" << logopt.substr(eq + 1) << "\"\n";
                        }
                }
        }
        if(!extra_hosts.empty()){
                std::cout << "    etc_hosts:\n";
                for(const std::string& host : extra_hosts){
                        size_t colon = host.find(':');
                        if(colon != std::string::npos){
                                std::cout << "      " << host.substr(0, colon) << ": \"" << host.substr(colon + 1) << "\"\n";
                        }
                }
        }
        if(!envs.empty()){
                std::cout << "    env:\n";
                for(const std::string& var_stat : envs){
                        size_t sep = var_stat.find('=');
                        if(sep != std::string::npos){
                                std::cout << "      " << var_stat.substr(0, sep) << ": \"" << var_stat.substr(sep + 1) << "\"\n";
                        }
                }
        }
        if(!labels.empty()){
                std::cout << "    labels:\n";
                for(const std::string& labs : labels){
                        size_t eq_pos = labs.find('=');
                        if(eq_pos != std::string::npos){
                                std::cout << "      " << labs.substr(0, eq_pos) << ": \"" << labs.substr(eq_pos + 1) << "\"\n";
                        }
                }
        }

        std::cout << "    state: started\n";

        if(detach_mode){
                std::cout << "    detach: true\n";
        }
        if(!commands.empty()){
                std::cout << "    command: ";
                size_t t = 0;
                while(t < commands.size()){
                        std::cout << commands[t] << (t + 1 < commands.size() ? " " : "");
                        ++t;
                }
                std::cout << std::endl;
        }
}

int main(int argc, char* argv[]){
        std::vector<std::string> args(argv + 1, argv + argc);

        if(args.size() >= 3 && args[0] == "podman" && args[1] == "run"){
                call_run_container(args);
        }
        return 0;
}
