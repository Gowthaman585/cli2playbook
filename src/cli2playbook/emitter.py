def generate_ansible_task(parsed_data):
    """
    Generates an Ansible task dictionary from parsed CLI data,
    processing lists, values, flags, and maps step-by-step.
    """
    ansible_task = {
        "name": "Manage Docker container from CLI input",
        "community.docker.docker_container": {}
    }
    
    docker_args = ansible_task["community.docker.docker_container"]
    
    # 1. Handle LISTS 
    parsed_lists = parsed_data.get("lists", {})
    for key, val_list in parsed_lists.items():
        # Only add if the list container has any value
        # which mean the docker command has the argument usage with value in it
        # Avoid any argument which has it flag but not value if they depends on value
        if val_list: 
            docker_args[key] = val_list

    parsed_values = parsed_data.get("values",{})
    for key, val_values in parsed_values.items():
        if val_values:
            docker_args[key] = val_values
            
    return ansible_task
