<%inherit file="manage_base.mako"/>

<%def name="title()">
Add column
</%def>

<div>
<h1>Add  column</h1>

<form action="${request.route_url('addcol', dbname=dbname, tablename=tablename)}" method="POST">
    
    <input type="submit" name="form.submitted" value="Add field" />
</form>
<br /><br /><br /><br /><br /><br />
</div>