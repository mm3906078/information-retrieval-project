## Installing steps
This crawler uses selenium and needs to install Chrome on your device. Also, you need to install Chrome drivers according to your Chrome version.
Please follow the steps:
1. find you're Chrome version using this command:
```
google-chrome --version
```
2. find the version on the [chrome driver site](https://googlechromelabs.github.io/chrome-for-testing/)
3. Add chromedriver to env
```
sudo mv chromedriver /usr/bin/chromedriver
sudo chown root:root /usr/bin/chromedriver
sudo chmod +x /usr/bin/chromedriver
```
4. Go to the pip environment
```
python3 -m venv ../.venv
source ../.venv/bin/activate
pip install -r requirement.txt
```
