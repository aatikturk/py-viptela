from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

def getCoLineSpecificStats(vmanage, deviceId):
    """
    Get VDSL service line bonding stats from device
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/vdslService/coLineSpecificStats?deviceId={deviceId}"
    response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
    return response
def getCoStats(vmanage, deviceId):
    """
    Get CO stats from device
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/vdslService/coStats?deviceId={deviceId}"
    response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
    return response
def getCpeLineSpecificStats(vmanage, deviceId):
    """
    Get VDSL service CPE line specific stats from device
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/vdslService/cpeLineSpecificStats?deviceId={deviceId}"
    response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
    return response
def getCpeStats(vmanage, deviceId):
    """
    Get CPE stats from device
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/vdslService/cpeStats?deviceId={deviceId}"
    response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
    return response
def getLineBondingStats(vmanage, deviceId):
    """
    Get VDSL service line bonding stats from device
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/vdslService/lineBondingStats?deviceId={deviceId}"
    response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
    return response
def getLineSpecificStats(vmanage, deviceId):
    """
    Get VDSL service line specific stats from device
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/vdslService/lineSpecificStats?deviceId={deviceId}"
    response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
    return response
def getVdslInfo(vmanage, deviceId):
    """
    Get VDSL info from device
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/vdslService/vdslInfo?deviceId={deviceId}"
    response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
    return response
