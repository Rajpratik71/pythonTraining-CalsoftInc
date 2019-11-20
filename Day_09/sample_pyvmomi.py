import ssl

from pyVim import connect
from pyVmomi import vim


def connectVcenter(vCenterHost, username, password, portNum=443):
    """
    Description : Performs vCenter connection.
    Parameters  : vCenterHost - vCenter server ip address (STRING)
                  username - vCenter server username (STRING)
                  password - vCenter server password (STRING)
                  portNum - Port number for connection, default is 443 (INT)
    Returns     : Service instance object
    """
    context = ssl._create_unverified_context()
    si = connect.SmartConnect(
        host=vCenterHost, user=username, pwd=password, port=portNum, sslContext=context
    )
    return si


def getObj(content, vimtype, name):
    """
    Description: Get the vsphere object associated with a given text name
    Parameters : content - Data object having properties for the
                   ServiceInstance managed object (OBJECT)
                 vimtype - Managed object type (OBJECT)
                 name    - Managed object entity name (STRING)
    Return:      Matched Managed object (OBJECT)
    """
    container = content.viewManager.CreateContainerView(
        content.rootFolder, vimtype, True
    )
    for vmObj in container.view:
        if vmObj.name == name:
            return vmObj


def getDatacenterByName(si, name):
    """
    Description: Find a datacenter by it's name and return it
    Parameters : si   - vCenter connection session (OBJECT)
                 name - datacenter name (STRING)
    Return:      datacenter Object (OBJECT)
    """
    return getObj(si.RetrieveContent(), [vim.Datacenter], name)


def getClusterByName(si, name):
    """
    Description: Find a cluster by it's name and return it
    Parameters : si   - vCenter connection session (OBJECT)
                 name - cluster name (STRING)
    Return: cluster Object (OBJECT)
    """
    return getObj(si.RetrieveContent(), [vim.ClusterComputeResource], name)


def getHostByName(si, name):
    """
    Description: Find a host by it's name and return it
    Parameters : si   - vCenter connection session (OBJECT)
                 name - host name (STRING)
    Return:  host Object (OBJECT)
    """
    return getObj(si.RetrieveContent(), [vim.HostSystem], name)


def getVirtualMachineByName(si, name):
    """
    Description: Find a vm by it's name and return it
    Parameters : si   - vCenter connection session (OBJECT)
                 name - vm name (STRING)
    Return:  virtual machine Object (OBJECT)
    """
    return getObj(si.RetrieveContent(), [vim.VirtualMachine], name)


def getDatastoreByName(si, name):
    """
    Description: Find a datastore by it's name and return it
    Parameters : si   - vCenter connection session (OBJECT)
                 name - datastore name (STRING)
    Return:  datastore Object (OBJECT)
    """
    return getObj(si.RetrieveContent(), [vim.Datastore], name)


def getNetworkByName(si, name, isVDS=False):
    """
    Description: Find a network by it's name and return it
    Parameters : si - vCenter connection session (OBJECT)
                 name - network name (STRING)
    Return:      network Object
    """
    if isVDS is False:
        networkObj = getObj(si.RetrieveContent(), [vim.Network], name)
    else:
        networkObj = getObj(
            si.RetrieveContent(), [vim.dvs.DistributedVirtualPortgroup], name
        )
    return networkObj


# connect vcenter
siObj = connectVcenter(vcenterIp, vcenterUsername, vcenterPassword)
# print(siObj.content.about)
# get datacenter by name
datacenterName = "UCP CI Datacenter"
datacenterObj = getDatacenterByName(siObj, datacenterName)
print("datacenterName is", datacenterObj.name, datacenterObj.datastore[0].name)

# get cluster by name
# clusterName = 'Dockerized'
# clusterObj = getClusterByName(siObj, clusterName)
# print("clusterName is", clusterObj.name)

# get host by name
# hostName = '192.168.25.205'
# hostObj = getHostByName(siObj, hostName)
# print("hostName is", hostObj.name)

# get datastore by name
# datastoreName = 'ds1'
# datastoreObj = getDatastoreByName(siObj, datastoreName)
# print("datastoreName is", datastoreObj.name)

# get network by name
# networkName = 'VM Network'
# networkObj = getNetworkByName(siObj, networkName)
# print("networkName is", networkObj.name)
# print("Vm's in this network", [vm.name for vm in networkObj.vm])

# get all vms inside datacenter
# vmsList = datacenterObj.vmFolder.childEntity
# for vm in vmsList:
#     print("Virtual Machine - ", vm.name)

# get vm by name
# vmObj = getVirtualMachineByName(siObj, 'k8s-master')
# print('VirtualMachineName', vmObj.name, dir(vmObj))

# poweroff the above virtual machine
# vmObj.PowerOff()

# poweron the above virtual machine
# vmObj.PowerOn()
