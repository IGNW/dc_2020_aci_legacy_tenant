from SourceControlMgmt.SourceControlMgmt import SourceControlMgmt
from jinja2 import FileSystemLoader, Environment
from datetime import datetime

def pre():
    # No data to pull from anything
    return locals()

def main(**kwargs):
    now = datetime.now()
    str_now = now.strftime("%Y%m%d-%H%M%S")

    templateLoader = FileSystemLoader(searchpath=f'./repos/dc_2020_aci_tenants/gui')
    templateEnv = Environment(loader=templateLoader)
    template = templateEnv.get_template('terraform.j2')

    description = kwargs['description']
    ip_address = kwargs['ip_address']
    ip_octects = ip_address.split('.')
    name = kwargs['name']
    name_ip_w_underscores = f"{name}_{ip_octects[0]}_{ip_octects[1]}_{ip_octects[2]}"
    scope = kwargs['routing']
    new_branch =  f'{name_ip_w_underscores}_{str_now}'


    tf_file_name = f'network_{ name }'

    terraform_file = template.render(
        name_ip_w_underscores=name_ip_w_underscores,
        name=name,
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
        pr_results = s.create_git_hub_pull_request(
            destination_branch="master", 
            source_branch=new_branch, 
            title=f"Pull Request {name_ip_w_underscores}", 
            body="")
        return pr_results 
    else:
        return {'Results:': 'Invalid Credentials'}

if __name__ == "__main__":
    vars = pre()
    main(**vars)
