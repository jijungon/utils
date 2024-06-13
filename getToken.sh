#!/bin/bash

## Comman ENV : Echo Color
c_red='\033[0;31m'              ## Red Color
c_blue='\033[0;34m'             ## Blue Color
c_yellow='\033[1;33m'           ## Yello Color
c_orange='\033[0;33m'           ## Orange Color
c_green='\033[0;32m'            ## Green Color
c_lightred='\033[1;31m'
no_color='\033[0m'                    ## Unset Color(NoColor)

script_home=$(echo $0 | xargs dirname)


####### AWS  USER Credential list
PROFILE_NAME=${PROFILE_NAME:-"default"}

### USER modify config field  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
AWS_ACCOUNT_ID={account_id}                                                             ### AWS SITE  IAM Infomation check
AWS_USER_ID="{id}"                                                       ### AWS login Account
AWS_MFA_ARN="arn:aws:iam::{id}:mfa/{user}"   ## <<<+=== IAM USER root

USER_OTP_CODE=""        ### AWS MFA Code
#t_provider_file="${Terraform_HOME}/provider.tf"
#Terraform_HOME="/app/terraform/aws_tbridge_single"                                     ### Terraform provider file path or config file path
## <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

aws_config_env_file="${HOME}/.aws/aws_config_env"


function get_aws_credential {

        #echo "aws --profile ${PROFILE_NAME} sts get-session-token --serial-number arn:aws:iam::${AWS_ACCOUNT_ID}:mfa/${AWS_USER_ID}  --token-code ${MFA_CODE}"
        #rst_credential=$(aws --profile ${PROFILE_NAME} sts get-session-token --serial-number arn:aws:iam::${AWS_ACCOUNT_ID}:mfa/${AWS_USER_ID}  --token-code ${MFA_CODE})
        echo "aws --profile ${PROFILE_NAME} sts get-session-token --serial-number ${AWS_MFA_ARN} --token-code ${MFA_CODE}"
        rst_credential=$(aws --profile ${PROFILE_NAME} sts get-session-token --serial-number ${AWS_MFA_ARN} --token-code ${MFA_CODE})

	get_AccessKeyId=$(echo ${rst_credential}| jq -r ".Credentials.AccessKeyId")
	get_SecretAccessKey=$(echo ${rst_credential}| jq -r ".Credentials.SecretAccessKey")
	get_SessionToken=$(echo ${rst_credential}| jq -r ".Credentials.SessionToken")
	get_Expiration=$(echo ${rst_credential}| jq -r ".Credentials.Expiration")

        if [ -z "${get_SessionToken}" ] ; then
                echo "++ [ERROR] get aws credential ..... Check !!!!!"
                exit 1
        fi

        echo -e "\n\n\n"

        {
                echo "export AWS_ACCESS_KEY_ID=\"${get_AccessKeyId}\""
                echo "export AWS_SECRET_ACCESS_KEY=\"${get_SecretAccessKey}\""
                echo "export AWS_SESSION_TOKEN=\"${get_SessionToken}\""
                echo "export AWS_TOKEN_EXPIRE=\"${get_Expiration}\""
        } | tee ${aws_config_env_file}

        echo -e "\n\n++++  run command ====>     source ${aws_config_env_file}\n\n"

}


main() {
        if [ -z $1 ] ; then
                echo -n "  ++ Input OTP Code (6-digit) ? "
                read MFA_CODE
                echo -e "\n\n "
        else
                MFA_CODE="$1"
        fi


        get_aws_credential
}

main $*
