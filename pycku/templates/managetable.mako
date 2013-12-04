
<%inherit file="manage_base.mako"/>

<h1>Tables in ${dbname}</h1>

<table>
    <tr class="tr_heading" >
        <th>Column name</th>
        <th>Type</th>
        <th>Primary key</th>
        <th>default</th>
         <th>nullable</th>



    </tr>
    %for c in table.columns:
        <tr class="${loop.cycle('oddrow', 'evenrow')}">
            <td>${c.name}</td>
            <td>${c.type}</td>
            <td>${c.primary_key}</td>
            <td>${c.default}</td>
             <td>${c.nullable}</td>

            <td>
               
                <a href="">Drop</a> 
            </td>
        </tr>
    %endfor
 <tr class="tr_heading" >
 <th>Add column</th> 
</tr>

</table>