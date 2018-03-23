<!DOCTYPE html>
<html>
<head>
    <title>Hello World!</title>
</head>
<body>
<p>Welcome {{username}}</p>
<ul>
    %for thing in things:
    <li>{{thing}}</li>
    %end
</ul>
<form action="/favourite_fruit" method="POST">
    What is your favourite fruit?
    <input type="text" name="fruit" size="40" value ="" title="entry"><br>
    <input type="submit" value="Submit">
</form>
</body>
</html>