import requests

print('real redirect')
response = requests.get('http://httpbin.org/redirect-to?url=httpbin.org/get&status_code=301', allow_redirects=False)

if response.status_code == 301 or response.status_code == 302:
    print("status_code:", response.status_code)
    print("status_text:", response.reason)
    print(response.headers)
    print(response.history)
    if response.history:
        print('리디렉션 발생:')
        for resp in response.history:
            print(resp)
            print(resp.status_code, resp.url)
        print('최종 URL:', response.url)

    print("Redirected to:", response.headers['Location']) ## 이게 진짜 내가 목표로 하는 위치

    # if ("조건 Is True redirection")

    
    print("Test 1 - 2")
    redirect = response.headers['Location']
    response2 = requests.get('http://' + redirect)
    print(response2.status_code)
    print(response2.reason)

    print(response2.headers)
else:
    print("Not redirected")



print('\n-=-=-=-=-=-=-=-=-=-=-=-=-=\n')
print('\nTEST TEST TEST TEST TEST\n')
print('\nTEST TEST TEST TEST TEST\n')
print('\nTEST TEST TEST TEST TEST\n')
print('\nTEST TEST TEST TEST TEST\n')
print('\n-=-=-=-=-=-=-=-=-=-=-=-=-=\n')

print('redirect route test')
response = requests.get('http://httpbin.org/status/301', allow_redirects=True) ## 여기서만 history

print("status_code:", response.status_code)
print("status_text:", response.reason)

## 상태코드 확인과 헤더, history 확인가능
print(response.headers)
print(response.history)
if response.history:
    print('리디렉션 발생:')
    for resp in response.history:
        print(resp)
        print(resp.status_code, resp.url)
    print('최종 URL:', response.url) ## 최종목적지

# print("Redirected to:", response.headers['Location']) ## 이게 진짜 여긴 없어