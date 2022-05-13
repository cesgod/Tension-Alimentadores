<?php

	session_start();

  ?>
			<?php  
				
				$commands = escapeshellcmd('/var/www/html/santa/tension.py');
				$outputs = shell_exec($commands);
				#echo "<pre>"; print_r($outputs); echo "</pre>";
				#phpinfo();
				#die();
				$stringvs = file_get_contents("/var/www/html/santa/data.json");

				    
				    if ($stringvs === false) {
				      echo "No content<br>";
				    }

				
               
                $data["stand"] =  json_decode($stringvs);
                $data = (object) $data;
                #echo "<pre>";print_r($data);echo "</pre>";

                #die();
                if (count($data->stand)) {
                    // Open the table
                    #echo "<table>";

                    // Cycle through the array
                    foreach ($data->stand as $idx => $stand) {

                        // Output a row
                        echo "<tr>";
                        echo "<td>$stand->MeterName</td>";
                        echo "<td>$stand->L1MAX</td>";
                        echo "<td>$stand->DateL1MAX</td>";
                        echo "<td>$stand->L2MAX</td>";
                        echo "<td>$stand->DateL2MAX</td>";
                        echo "<td>$stand->L3MAX</td>";
                        echo "<td>$stand->DateL3MAX</td>";
                        echo "<td>$stand->L1MIN</td>";
                        echo "<td>$stand->DateL1MIN</td>";
                        echo "<td>$stand->L2MIN</td>";
                        echo "<td>$stand->DateL2MIN</td>";
                        echo "<td>$stand->L3MIN</td>";
                        echo "<td>$stand->DateL3MIN</td>";
                        echo "</tr>";
                    }

                    // Close the table
                    #echo "</table>";
                }
                echo ' </tbody>
                </table>';
                echo "<pre>"; print_r($data); echo "</pre>";
                die();
				$_SESSION['bill_ad']    = $arrayn['date'][0];
                $_SESSION['bill_a']     = $arrayn['data'][0];
				$_SESSION['bill_bd']    = $arrayn['date'][1];
                $_SESSION['bill_b']     = $arrayn['data'][1];
				$valores   = array_values($arrayn);
				echo json_encode($valores);
				echo "<pre>"; print_r($arrayn); echo "</pre>";
				#die();
                header("Location: ../../../../Charts_Data/dash-master/billingblockware.php");
			?>
		