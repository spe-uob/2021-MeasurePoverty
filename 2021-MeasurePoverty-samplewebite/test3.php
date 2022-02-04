<!DOCTYPE html>
<html lang="en">
<body>
<?php
    echo isset ($_GET['namelist']) ? 'You choose:' . $_GET['namelist'] : ' Please choose from below';
    ?>
<form action = "" method="get">
    <select name="namelist">
        <option value = "2009"> 2009 </option>
        <option value = "2010"> 2010 </option>
        <option value = "2011"> 2011 </option>
        <option value = "2012"> 2012 </option>
        <option value = "2013"> 2013 </option>
    </option>
    </select>
    <select language="langlst">
        <option value = "English"> English </option>
        <option value = "French"> French </option>
        <option value = "Spanish"> Spanish </option>
        <option value = "German"> German </option>
        <option value = "Chinese"> Chinese </option>
    </select>
    <input type = "submit" value="submit">
</form>
</body></html>
