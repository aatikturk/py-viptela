from query_builder import Builder
import HttpMethods

class DataPrefix(object):
    """
    Configuration - Policy Data Prefix List Builder API
    
    Implements GET POST DEL PUT methods for PolicyDataPrefixListBuilder endpoints

    """

    def __init__(self, session, host, port):
        self.host = host
        self.port = port
        self.client = HttpMethods.HttpClient(session=session)
    
    def getPolicyLists(self):
        """
        Get policy lists
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/policy/list/dataprefix"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def createPolicyList(self, policylist):
        """
        Create policy list
        
        Parameters:
        policylist:	Policy list
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/policy/list/dataprefix"
        response = self.client.apiCall(HttpMethods.POST, endpoint, policylist)
        return response


    def previewPolicyList(self, policylist):
        """
        Preview a policy list based on the policy list type
        
        Parameters:
        policylist:	Policy list
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/policy/list/dataprefix/preview"
        response = self.client.apiCall(HttpMethods.POST, endpoint, policylist)
        return response


    def previewPolicyListById(self, id):
        """
        Preview a specific policy list entry based on id provided
        
        Parameters:
        id	 (string):	Policy Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/policy/list/dataprefix/preview/{id}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getListsById(self, id):
        """
        Get a specific policy list based on the id
        
        Parameters:
        id	 (string):	Policy Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/policy/list/dataprefix/{id}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def editPolicyList(self, policylist, id):
        """
        Edit policy list entries for a specific type of policy list
        
        Parameters:
        policylist:	Policy list
		id	 (string):	Policy Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/policy/list/dataprefix/{id}"
        response = self.client.apiCall(HttpMethods.PUT, endpoint, policylist)
        return response


    def deletePolicyList(self, id):
        """
        Delete policy list entry for a specific type of policy list
        
        Parameters:
        id	 (string):	Policy Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/policy/list/dataprefix/{id}"
        response = self.client.apiCall(HttpMethods.DELETE, endpoint)
        return response


