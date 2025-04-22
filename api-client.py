import requests
import json


def metodo_get():
    try:
        response = requests.get("http://localhost:8081")
        if response.status_code == 200:
            print("Response GET: ", response.json())
        else:
            print("Error GET: ", response.status_code)
    except Exception as e:
        print("Exception GET: ", e)

def metodo_post():
    try:
        data = {"username": "example"}
        headers = {'Content-Type': 'application/json'}
        response = requests.post("http://localhost:8081/post", data=json.dumps(data), headers=headers) 
        if response.status_code == 200:
            print("Response POST: ", response.json())
        else:
            print("Error POST: ", response.status_code)
    except Exception as e:
        print("Exception POST: ", e)


if __name__ == "__main__":
    metodo_get()
    metodo_post()







"""
- - - - -- - - - - - -- - -- - -- - -- - - METODO GET -
let fetchRes = fetch(
"http://localhost:8081");
    fetchRes.then(res =>
      res.json()).then(d => {
        console.log(d)
      })

- - - - -- - - - - - -- - -- - -- - -- - - METODO POST -
const data = { username: 'example' };

fetch('http://localhost:8081/post', {
 method: 'POST', // or 'PUT'
 headers: {
  'Content-Type': 'application/json',
 },
 body: JSON.stringify(data),
})
 .then((response) => response.json())
 .then((data) => {
  console.log('Success:', data);
 })
 .catch((error) => {
  console.error('Error:', error);
});

"""