import paramiko
import subprocess


def ssh(cmd, host, user, password=None):
    cmds = ' '.join(cmd)
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, port=22, username=user, password=password)

    stdin, stdout, stderr = client.exec_command(cmds)
    retcode = stdout.channel.recv_exit_status()
    client.close()  # @TODO re-use connections
    if retcode > 0:
        output = stderr.read().strip()
        raise subprocess.CalledProcessError(returncode=retcode, cmd=cmd,
                                            output=output)
    return (''.join(stdout), ''.join(stderr))
