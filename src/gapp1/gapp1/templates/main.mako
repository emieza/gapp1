<html>
    
<head>
    <title>${project}</title>
</head>

    <%  
        from google.appengine.api import users
        login_url = users.create_login_url("/")
        logout_url = users.create_logout_url("/")
    %>

<body>
    <img src="${request.application_url}/static/pyramid_ae.png" alt="pyramid"/>
    <h1>SUPER Projecte ${project}</h1>
    <p>Aviam que tal va aixo...</p>
    % if usuari:
    <p>Usuari: ${usuari} | <a href="${logout_url}">Surt</a></p>
    % else:
    <p><a href="${login_url}">Loga't</a></p>
    % endif
</body>

</html>
