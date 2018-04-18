# git initialization in CLI

CLI에서 더 빠르게 repo를 생성하자!

1. `mkdir "DIR_NAME"`
2. `cd "DIR_NAME"`&nbsp
3. `git init`
4. `touch README.md`
5. `git add README.md`
6. `git commit -m "first commit"`
7. `git remote add origin https://github.com/"ID"/"REPO_NAME".git`
8. `git push --set-upstream origin master`

### [changed] 2018-04-18 수정사항

CLI command로 Fatal: repository not found 에러가 발생하여
Github API를 사용해 repository를 생성하는 법을 알아보았습니다.

#### postman 이용 시, 

reference: https://developer.github.com/v3/repos/#create

1. 

POST 방식으로 https://api.github.com/user/repos 에 요청을 보냅니다.
<br>
이 때, Authorization을 위해 headers에 access token을 key: Authorization, values:token "자신의 token" 양식으로 넣어줘야 합니다.
<br>
access token발급은 github 사이트에서 우측상단의 계정을 누르시고 
<br>
Settings -> Developer settings -> Personal access tokens에서 발급가능합니다.
<br>
(이미 발급되었는데 모르시는 분은 regenerate를 할 수 있습니다)

![postman-01](https://imgur.com/UbiR1xn.png)

2. 

그 다음엔, headers 옆의 body 탭을 누르고 raw에 체크, JSON으로 변경한 후에
<br>
```
{
    "name": "repo이름",
    "auto_init": true
}
```
를 입력하시고 send를 누르시고 201 created가 return 되면 성공입니다.

![postman-02](https://imgur.com/q0q2Tu3.png)


#### CLI에서 API 이용 시, 
