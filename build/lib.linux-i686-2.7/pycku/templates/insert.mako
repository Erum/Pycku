<%inherit file="base.mako"/>
<h1>insert</h1>
<form action="${request.route_url('insert')}" method="POST">
<html>
<body>

<div id="container" style="width=100%" "height=50%">

<div id="header" style="background-color:#FFA500;" align=center>
<h1 style="margin-bottom:0;">PYCK</h1></div>



<div id="menu" align=center style="background-color:#FFD700;height:1000px;width:200px;float:left; ">
<b>PYCKU</b><br>

   <dl >
      <dt>erum</dt>
      <dt>Table 2</dt>
      <dt>Table 3</dt>
      <dt>Table 4</dt>
	</dl>

</div>

<div id="header" style="background-color:#EEEEEE;" align=center>
<table >
     <tr>
          <td><a href="Structure.mako">Structure</a></td>
		  <td><a href="Insert.mako">Insert</a></td>
	 </tr>

    </table>
</div>

<div id="content" style="background-color:#EEEEEE;height:1000px;width:1000px;float:left;">
<table border="1">
	    <tr>
		<td width="5%">Column </td>
		<td width="3%">Type</td>
		<td width="10%">Function</td>
		<td width="1%">Null</td>
		<td width="20%">Value</td>
		</tr>
		
		<tr>
		<td>Column</td>
		<td>Type</td>
		<td><form action="">
        <select name="cars">
        <option value="f1">f1</option>
        <option value="f2">f2</option></select>
          </form>
         </td>
		<td>Null</td>
		<td><input type="text" name="value"></td>
		</tr>
		
		<tr>
		<td>Column</td>
		<td>Type</td>
		<td><form action="">
        <select name="cars">
        <option value="f1">f1</option>
        <option value="f2">f2</option></select>
          </form>
         </td>
		<td>Null</td>
		<td><input type="text" name="value"></td>
		</tr>
		
		<tr>
		<td>Column</td>
		<td>Type</td>
		<td><form action="">
        <select name="cars">
        <option value="f1">f1</option>
        <option value="f2">f2</option></select>
          </form>
         </td>
		<td>Null</td>
		<td><input type="text" name="value"></td>
		</tr>
		
		<tr>
		<td>Column</td>
		<td>Type</td>
		<td><form action="">
        <select name="cars">
        <option value="f1">f1</option>
        <option value="f2">f2</option></select>
          </form>
         </td>
		<td>Null</td>
		<td><input type="text" name="value"></td>
		</tr>
		
		<tr>
		<td>Column</td>
		<td>Type</td>
		<td><form action="">
        <select name="cars">
        <option value="f1">f1</option>
        <option value="f2">f2</option></select>
          </form>
         </td>
		<td>Null</td>
		<td><input type="text" name="value"></td>
		</tr>

    </table>
</div>


</div>
 
</body>
</html>
