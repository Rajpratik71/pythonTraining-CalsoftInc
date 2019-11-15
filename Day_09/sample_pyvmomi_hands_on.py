import ssl
from pyVim import connect
from pyVmomi import vim

def connect_vcenter(vcenterIp, username, password):
     context = ssl._create_unverified_context()
     si = connect.SmartConnect(host=vcenterIp, user=username, pwd=password, port=443, sslContext=context)
     return si

def get_obj(content, vimtype):
        return [item for item in content.viewManager.CreateContainerView(
            content.rootFolder, [vimtype], recursive=True).view]

si_obj = connect_vcenter(<vcenterIp>, <username>, <password>)

for datacenter in get_obj(si_obj.RetrieveContent(), vim.Datacenter):
    number_of_clusters = 0
    number_of_hosts = 0
    for child in datacenter.hostFolder.childEntity:
        if isinstance(child, vim.ClusterComputeResource):
            cluster = child
            number_of_clusters += 1
            for host in cluster.host:
                print(host.config)
