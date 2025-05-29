from pathlib import Path


aws_config = Path("~/.aws/config")

if aws_config.expanduser().exists():
    print("AWS config file is present")
else:
    print("There is no AWS config")


full_log = Path("full.log")

if full_log.exists():
    print("`full.log` is present")
    if full_log.is_dir():
        print("'full.log' is directory")
        full_log.rmdir()
        print("'full.log' directory is deleted")
    else:
        print("'full.log' is file")
else:
    print("There is no `full.log`")




log_dir = Path("log")
log_dir.mkdir(exist_ok=True)
print("`log` directory is there")