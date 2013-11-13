<%inherit file="manage_base.mako"/>

<h1>Tables in ${dbname}</h1>

<table>
    <tr class="tr_heading">
        <th>Tablename</th>
        <th>Actions</th>
    </tr>
    %for tablename in tablenames:
        <tr class="${loop.cycle('oddrow', 'evenrow')}">
            <td>${tablename}</td>
            <td>
                <a href="">View Structure</a> |
                <a href="">Browse</a>
            </td>
        </tr>
    %endfor
    
</table>