kasa works just fine as a library but the cli is plenty

e.g. pipx install and then crontab -e

```BASH
USER=curt
0 6 * * * /home/curt/.local/bin/kasa --host 192.168.1.138 on
0 21 * * * /home/curt/.local/bin/kasa --host 192.168.1.138 off
```
