import sys
from jira.client import JIRA

if (len(sys.argv)<2):
    print("Please run python script with correct syntax.")
    print("python Log_JIRA_On_Build_DeployFailure.py ${REVISION_NO} ${SVN_URL}")
    sys.exit(1);

revision_no=sys.argv[1];

repo_Url=sys.argv[2];



def jira_auth_and_issue_creator():

    try:

        jira_options={'server': 'XXXXXXXX'}

        jira=JIRA(options=jira_options,basic_auth=('UserName','Password'))



        issue=jira.create_issue(project={'key': 'PDDEV'},

                                issuetype={'name': 'Bug'},

                                assignee={'name': 'Assigne Name'},

                                summary=f'Deployment Failed at Revision number {revision_no} SVN Repository URL {repo_Url}',

                                priority={'name':'Critical'},

                                description=f'Deployment Failed Revision number {revision_no} SVN Repository URL {repo_Url}',

                                components=[{'name':'API'}],

                                versions= [{'name':'7.00.00.00-M1'}]

                                )

        print('Issue created')



    except Exception as err:
		
        print(err)
	

jira_auth_and_issue_creator()