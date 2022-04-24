from query_builder import Builder
import HttpMethods

class Mesh(object):
    """
    Configuration - Policy Mesh Definition Builder API
    
    Implements GET POST DEL PUT methods for PolicyMeshDefinitionBuilder endpoints

    """

    def __init__(self, session, host, port):
        self.host = host
        self.port = port
        self.client = HttpMethods.HttpClient(session=session)
    
    
    def getDefinitions(self):
        """
        Get policy definitions
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/policy/definition/mesh"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def createPolicyDefinition(self, policydefinition):
        """
        Create policy definition
        
        Parameters:
        policydefinition:	Policy definition
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/policy/definition/mesh"
        response = self.client.apiCall(HttpMethods.POST, endpoint, policydefinition)
        return response


    def savePolicyDefinitionInBulk(self, policydefinition):
        """
        Create/Edit policy definitions in bulk
        
        Parameters:
        policydefinition:	Policy definition
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/policy/definition/mesh/bulk"
        response = self.client.apiCall(HttpMethods.PUT, endpoint, policydefinition)
        return response


    def editMultiplePolicyDefinition(self, policydefinition, id):
        """
        Edit multiple policy definitions
        
        Parameters:
        policydefinition:	Policy definition
		id	 (string):	Policy Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/policy/definition/mesh/multiple/{id}"
        response = self.client.apiCall(HttpMethods.PUT, endpoint, policydefinition)
        return response


    def previewPolicyDefinition(self, policydefinition):
        """
        Preview policy definition
        
        Parameters:
        policydefinition:	Policy definition
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/policy/definition/mesh/preview"
        response = self.client.apiCall(HttpMethods.POST, endpoint, policydefinition)
        return response


    def previewPolicyDefinitionById(self, id):
        """
        Preview policy definition
        
        Parameters:
        id	 (string):	Policy Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/policy/definition/mesh/preview/{id}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getPolicyDefinition(self, id):
        """
        Get a specific policy definitions
        
        Parameters:
        id	 (string):	Policy Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/policy/definition/mesh/{id}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def editPolicyDefinition(self, policydefinition, id):
        """
        Edit a policy definitions
        
        Parameters:
        policydefinition:	Policy definition
		id	 (string):	Policy Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/policy/definition/mesh/{id}"
        response = self.client.apiCall(HttpMethods.PUT, endpoint, policydefinition)
        return response


    def deletePolicyDefinition(self, id):
        """
        Delete policy definition
        
        Parameters:
        id	 (string):	Policy Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/policy/definition/mesh/{id}"
        response = self.client.apiCall(HttpMethods.DELETE, endpoint)
        return response


