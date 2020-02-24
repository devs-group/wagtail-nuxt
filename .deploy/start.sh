set -x

export ENV_REGEX="(\w+)=(.+)"
export ENV_PATH=".env.dist"
export DEPLOY_PATH_SERVER="websites/COOKIECUTTER_PLACEHOLDER_PROJECTNAME"

# Mind: The context runs at root directory
sh ./.deploy/replace_dotenv.sh &&
sh ./.deploy/validate_dotenv.sh &&
sh ./.deploy/deploy.sh
