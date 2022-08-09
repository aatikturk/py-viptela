def preview(vmanage, policyassembly):
    """
    Get policy assembly preview
    
    Parameters:
    policyassembly:	Policy assembly
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/template/policy/assembly/voice"
    response = vmanage.apiCall("POST", endpoint, policyassembly)
    return response


def previewById(vmanage, id):
    """
    Get policy assembly preview
    
    Parameters:
    id	 (string):	Policy Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/template/policy/assembly/voice/{id}"
    response = vmanage.apiCall("GET", endpoint)
    return response
