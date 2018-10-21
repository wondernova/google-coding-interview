# Linux Interview Questions

#### How to check current run level of a linux server ?

```
who -r
```

또는

```
runlevel
```

###  How to check the default gatway in linux ?

```
route -n
```

또는

```
netstat -nr
```


#### 30일 안에 access된 모든 파일을 찾아라

```
$ find . -atime +30
```

#### how to see unallocated hard disk space on linux

```
$ cat /proc/partitions
major minor  #blocks  name

   8        0  250059096 sda
   8        1  250057728 sda1
   8       16  976762584 sdb
   ...
```

####  how do u find remote machine operating system and version?

```
$ uname -r
4.10.0-42-generic
```

####  how do you port scaning with netcat command?

아래의 코드는 1초를 wait time을 갖고,  1 ~ 80 까지의 포트를 검색함. 
nmap같은 경우는 매우 빠른데 반해서 netcat은 각각의 포트를 하나하나씩 검색하기 때문에 매우 느리다. 
실질적으로 -w 1 옵션으로 wait time을 1초로 설정하지 않으면 매우 오래 기달려야 한다. 

```
$ nc -v -w 1 -z naver.com 1-80
```

#### How do you make a connection with netcat command?

TCP connection

```
$ nc -v  google.com 80
Connection to google.com 80 port [tcp/http] succeeded!
```

UDP connection

```
$ nc -v -u google.com 53
```





