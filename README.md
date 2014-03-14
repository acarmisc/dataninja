Dataninja
=========

Environment setup
-----------------

To preserve the repository secret free we put the credentials in some environment variables. Do it like this:

    echo "export amazon_secret=<string>" >> ~/app-root/data/.bash_profile
    echo "export amazon_code=<string>" >> ~/app-root/data/.bash_profile
    echo "export amazon_key=<string>" >> ~/app-root/data/.bash_profile

    echo "export ebay_appid=<string>" >> ~/app-root/data/.bash_profile
