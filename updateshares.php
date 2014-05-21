<?php
	while(true) {
		if (file_exists("/tmp/shares-insert.log")) {
			unlink("/tmp/shares-insert.log");
		}
		if (file_exists("/tmp/shares.log")) {
			rename("/tmp/shares.log","/tmp/shares-insert.log");
	
			$db = new mysqli("127.0.0.1","username","password","database");
	
			$res = $db->Query(<<<EOF
LOAD DATA INFILE "/tmp/shares-insert.log" INTO TABLE shares 
FIELDS TERMINATED BY "," 
OPTIONALLY ENCLOSED BY "'" 
LINES TERMINATED BY "\n" 
(@time,coin_id,@rem_host,username,@our_result,@upstream_result,
solution,difficulty) 
SET rem_host=REPLACE(@rem_host,"::ffff:",""),
time=FROM_UNIXTIME(@time),
our_result=@our_result,
upstream_result=@upstream_result,reason=""
EOF
);
			$updates = $db->affected_rows;
	
			echo $updates . " shares added.\n";
			$db->close();
		} else {
			echo "No shares found since last check.\n";
		}
		
		echo "Sleeping...";
		sleep(10);
		echo "\n";
	}
?>
