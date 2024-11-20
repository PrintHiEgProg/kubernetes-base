# kubernetes-base

## block-scheme
![alt text](https://i124.fastpic.org/big/2024/1120/fc/2b098ed697d53ca8fc39c5972aac9efc.png)

## testing

```sh
cd kubernetes-base
'''venv activate'''
pip install -r requirements.txt
python main.py
python test-api1.py
python test-api2.py
python test-api3.py
curl -X GET "http://127.0.0.1:8000/hello"
```





