<%def name="title()">
Database Manager - ${dbname}
</%def>


<!DOCTYPE html>
<html>
<head>
  
  <title>${self.title()}</title>
  
  <link rel="shortcut icon" href="${request.static_url('pycku:static/favicon.ico')}" />
  <link rel="stylesheet" href="${request.static_url('pycku:static/pyck.css')}" type="text/css" media="screen" charset="utf-8" />
  <link rel="stylesheet" href="http://static.pylonsproject.org/fonts/nobile/stylesheet.css" media="screen" />
  <link rel="stylesheet" href="http://static.pylonsproject.org/fonts/neuton/stylesheet.css" media="screen" />
  <!--[if lte IE 6]>
  <link rel="stylesheet" href="${request.static_url('pycku:static/ie6.css')}" type="text/css" media="screen" charset="utf-8" />
  <![endif]-->
  <link rel="stylesheet" href="http://ajax.googleapis.com/ajax/libs/dojo/1.8.3/dojo/resources/dojo.css" type="text/css" charset="utf-8" />
  <link rel="stylesheet" href="http://ajax.googleapis.com/ajax/libs/dojo/1.8.3/dijit//themes/claro/claro.css" type="text/css" charset="utf-8" />
  <script src="//ajax.googleapis.com/ajax/libs/dojo/1.8.3/dojo/dojo.js" data-dojo-config="isDebug: true, async: true, parseOnLoad: true"></script>
  <script type="text/javascript">
        require(['dojo/parser', 'dojo/domReady'],function(parser,ready){ready(function(){
          parser.parse();
          });});
  </script>

</head>

<body>
<div id="content">
    <div class="flash">
      <% flash_msgs = request.session.pop_flash() %>
      
      %for flash_msg in flash_msgs:
        ${flash_msg}<br />
      %endfor
    </div>
    <table width="100%" style="height: 100%;">
    <tr class="tr_heading">
        <th colspan="2">Manage database: ${dbname}</th>
    </tr>
    <tr>
        <td style="vertical-align: top; background-color: #D8D8D8; font-weight: bold; font-size: 12pt; width: 20%; padding: 5px;">
            <!-- tables come here -->
            %for tablename in tablenames:
                <a href="${request.route_url('manage_table', dbname=dbname, tablename=tablename)}">${tablename}</a><br />
            %endfor
            
        </td>
 s
        <td style="padding: 20px;">
        ${self.body()}
        </td>
    </tr>
    </table>
  
</div>
</body>
</html>
