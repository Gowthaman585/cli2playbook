from cli2playbook.options import OPTION_RULES, OptType

def parse_cli_args(args):
    """
    Parses only the list-type arguments based on the current implementation.
    """
    parsed_data = {
        "lists": {},
        "values" : {},
        "flags" : {}
    }

    i = 0
    while i < len(args):
        current_arg = args[i]
        matched_rule = None
        
        for rule in OPTION_RULES:
            if current_arg in rule["flags"]:
                matched_rule = rule
                break
                
        # If it matched a LIST rule
        if matched_rule:
            
            # for LISTS containers
            if matched_rule["type"] == OptType.LIST:
                key = matched_rule["key"]
                if i + 1 < len(args):
                    val = args[i + 1]
                    i += 1  # Skip the next word since we consumed it
                
                    # If the list doesn't exist yet for this key, create it!
                    if key not in parsed_data["lists"]:
                        parsed_data["lists"][key] = []
                    
                    # Append the value into our list box
                    parsed_data["lists"][key].append(val)


            # for VALUES container
            if matched_rule["type"] == OptType.VALUE:
                key = matched_rule["key"]
                if i + 1 < len(args):
                    val = args[i+1]
                    i = i + 1
                    
                    parsed_data["values"][key] = val


            # for FLAG container
            if matched_rule["type"] == OptType.FLAG:
                key = matched_rule["key"]
                parsed_data["flags"][key] = True

        i = i+ 1

    return parsed_data
