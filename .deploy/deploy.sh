export SSHPASS=${SSH_PASS_NETCUP_SERVER}
sshpass -e rsync -e "ssh -o StrictHostKeyChecking=no" -avzP ./docker-compose.production.yml ${SERVER_SSH_ADDRESS}:${DEPLOY_PATH_SERVER}/docker-compose.yml
sshpass -e rsync -e "ssh -o StrictHostKeyChecking=no" --ignore-existing --chmod=u+rw -avzP ./.env.dist ${SERVER_SSH_ADDRESS}:${DEPLOY_PATH_SERVER}/.env
sshpass -e ssh -tt ${SERVER_SSH_ADDRESS} "cd ${DEPLOY_PATH_SERVER} && docker login ${GITLAB_REGISTRY} -u ${CI_USER_NETCUP} -p ${CI_PASS_NETCUP} && docker-compose pull && docker-compose up -d"
