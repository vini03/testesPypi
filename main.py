import requests

url_pypi = "https://pypi.org/project/humanizer/"
r_pypi = requests.get(url_pypi)

print(r_pypi.text)
# print(r_pypi.status_code)

# if r_pypi.status_code == 200:
  # print("O Site esta online")
# else:
  # print("O Site esta off")