from SourceControlMgmt.SourceControlMgmt import SourceControlMgmt

def pre():
    # No data to pull from anything
    return locals()

def main(**kwargs):
    s = SourceControlMgmt(
        username=kwargs['github_username'],
        password=kwargs['github_password'],
        email=kwargs['github_email_address'],
        repo_name='dc_2020_aci_tenants',
        repo_owner='IGNW',
        friendly_name='DevNet Connect 2020 ACI Tenants'
    )

    new_branch = kwargs['github_new_branch']

    if s.validate_scm_creds():
        s.clone_private_repo("tmp")
        s.create_new_branch_in_repo(new_branch)
        data = {
            "value_1": kwargs['value_1'],
            "value_2": kwargs['value_2']
        }
        s.write_data_to_file_in_repo(data, file_path='data', file_name='myfile')
        s.push_data_to_remote_repo()
        s.delete_local_copy_of_repo()
        s.get_all_current_branches()
        pr_results = s.create_git_hub_pull_request(destination_branch="master", source_branch=new_branch, title="Test Pull Request", body="A test pull request")

    return pr_results 

if __name__ == "__main__":
    vars = pre()
    main(**vars)
