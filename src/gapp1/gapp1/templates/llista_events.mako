<html>
    
<head>
    <title>Llista d'events</title>
</head>

<body>
    <h1>Llista d'events</h1>
    <table>
    % if events:
    % for event in events:
    <tr>
        <td>${event.title}</td>
        <td>${event.description}</td>
        <td>${event.time}</td>
        <td>${event.location}</td>
    </tr>
    % endfor
    % endif
    </table>
</body>

</html>
