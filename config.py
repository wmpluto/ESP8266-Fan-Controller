# Begin configuration
FAN_PIN = 2
FAN_DEFAULT_FREQ = 100
FAN_DEFAULT_DUTY = 1023
BTN_PIN = 0
BTN_IDLE = 0
SSID = "*******"
PWD  = "*******"
HTML = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width" />
  <title>控制界面</title>
  <style>
    .board button {
      width: 100px;
      height: 100px;
      border-radius: 50%%;
      border: 4px solid white;
      margin: 1px;
    }
  </style>
  <script type="text/javascript">
    function show_confirm() {
      var r = confirm("是否关机?");
      if (r==true) {
        window.location.href = '/poweroff';
        alert("关机中");
      }
    }
</script>
</head>

<body>
  <table class="board">
    <tr><td><a>开关机</a></td></tr>
    <tr>
      <td><button type="button" style="background-color:green" onclick="window.location.href = '/poweron'">开机</button></td>
      <td></td>
      <td><button type="button" style="background-color:red" onclick="show_confirm()">关机</button></td>
    </tr>
  </table>
  <form action="/fan">
    <br>风扇
    <br>频率: <input type="text" name="freq" value=%d>
    <br>占空: <input type="text" name="duty" value=%d>
    <br><br><input type="submit" value="设置">
  </form> 
</body>
</html>
"""
# End configuration