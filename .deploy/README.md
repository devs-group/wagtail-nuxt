# What is this for?
Those deployment scripts are used for our pipeline to make some prechecks and to make sure that we provide secure credentials when deploying our apps.

## How to use this?
1. Clone this repository into your project root with `git clone git@gitlab.com:devs-group/deployment.git .deploy`
2. Adjust the `<REPLACE_ME>` in [start.sh](./start.sh) and in [replace_dotenv.sh](./replace_dotenv.sh)
3. In your `.gitlab-ci.yml` call the `start.sh` like\
   **Example**:
   ```
   deploy:
     stage: deploy
     environment:
       ...
     before_script:
       ...
     script:
       - sh ./.deploy/start.sh
     only:
       ...
   ```

## Adding new credentials
In case if you add new credentials or variables in the projects `.env.dist` that need to be changed:

1. Edit the [replace_dotenv.sh](./replace_dotenv.sh) to replace the variables you added.
