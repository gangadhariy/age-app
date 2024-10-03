<h1 align="center">AGE-APP</h1>

## To run this app on Docker, follow the steps:

### 1. First, clone the app by running the following command:
```bash
git clone https://github.com/gangadhariy/age-app.git
```
```bash
cd age-app
```
```bash
docker build -t flask-age-app .
```
```
docker run -d -p 80:5000 flask-age-app
```
# Now open your web browser and access the app using the following URL:
```bash
http://localhost
```
