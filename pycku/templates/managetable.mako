<%inherit file="manage_base.mako"/>

<h1>Tables in ${dbname}</h1>

<table>
    <tr class="tr_heading">
        <th>Tablename</th>
        <th>Actions</th>
    </tr>
    %for c in table.columns:
        <tr class="${loop.cycle('oddrow', 'evenrow')}">
            <td>${c.name}</td>
            <td>${c.type}</td>
            <td>${c.primary_key}</td>
            <td>${c.default}</td>
            <td>
                <a href="">View Structure</a> |
                <a href="">Browse</a>
            </td>
        </tr>
    %endfor
    
</table>