from SourceControlMgmt.SourceControlMgmt import SourceControlMgmt
from jinja2 import FileSystemLoader, Environment

def pre():
    # No data to pull from anything
    return locals()

def main(**kwargs):

    new_branch = kwargs['github_new_branch']
    data = {}
    for arg, argv in kwargs.items():
        if "github" not in arg:
            data[arg] = argv

    templateLoader = FileSystemLoader(searchpath=f'./repos/dc_2020_aci_tenants/gui')
    templateEnv = Environment(loader=templateLoader)
    template = templateEnv.get_template('terraform.j2')

    description = kwargs['description']
    ip_address = kwargs['ip_address']
    ip_octects = ip_address.split('.')
    vlan = kwargs['vlan']
    ip_vlan_w_underscores = f"{ip_octects[0]}_{ip_octects[1]}_{ip_octects[2]}_V{vlan}"
    ip_vlan_w_dots= f"{ip_octects[0]}.{ip_octects[1]}.{ip_octects[2]}_V{vlan}"
    scope = kwargs['routing']

    tf_file_name = f'network_{ ip_vlan_w_dots }'

    terraform_file = template.render(
        ip_vlan_w_underscores=ip_vlan_w_underscores,
        ip_vlan_w_dots=ip_vlan_w_dots,
        ip_address=ip_address,
        description=description,
        scope=scope
    )

    s = SourceControlMgmt(
        username=kwargs['github_username'],
        password=kwargs['github_password'],
        email=kwargs['github_email_address'],
        repo_name='dc_2020_aci_tenants',
        repo_owner='IGNW',
        friendly_name='DevNet Connect 2020 ACI Tenants'
    )

    if s.validate_scm_creds():
        print('creds validated')
        s.clone_private_repo("/tmp")
        s.create_new_branch_in_repo(new_branch)
        s.write_data_to_file_in_repo(terraform_file, file_path='', file_name=tf_file_name)
        s.push_data_to_remote_repo()
        s.delete_local_copy_of_repo()
        s.get_all_current_branches()
        pr_results = s.create_git_hub_pull_request(destination_branch="master", source_branch=new_branch, title="Test Pull Request", body="A test pull request")
        return pr_results 
    else:
        return {'Results:': 'Invalid Credentials'}

if __name__ == "__main__":
    vars = pre()
    main(**vars)
