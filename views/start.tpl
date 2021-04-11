<html>
<head>
<title>Create Election</title>
</head>
<body>
<h1>Create Election</h1>
<h2>People</h2>
<ul>
  % for person in people:
  <li>{{person}}</li>
  % end
</ul>
<h2>Venues</h2>
<ul>
  % for venue in venues:
  <li>{{venue}}</li>
  % end
</ul>
</body>
</html>
