FAILED=0

# Extend this list to your needs
for CHECK_VALUE in "root" "admin" "local" "development" "localhost" "127.0.0.1"
do
    for ENV_LINE_VALUE in $(cat $ENV_PATH | sed -E "s|$ENV_REGEX|\0|" | xargs)
    do
        VAR=$(echo $ENV_LINE_VALUE | sed -E "s|$ENV_REGEX|\1|")
        VAL=$(echo $ENV_LINE_VALUE | sed -E "s|$ENV_REGEX|\2|")
        case $ENV_LINE_VALUE in *"$CHECK_VALUE"*)
            echo "FAILED: Please add a deployment valid value for \"$VAR\" instead of \"$VAL\""
            FAILED=1
        esac
    done
done

case $FAILED in 1)
    echo "FAILED: Make sure to replace all .env.dist values inside \"replace_dotenv.sh\""
    exit 1
esac
