# kubernetes-base
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




