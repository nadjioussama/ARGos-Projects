DELTA = 0.001
function init()
	robot.colored_blob_omnidirectional_camera.enable()
    if robot.id =="fb0" then
        robot.leds.set_all_colors("red")
    end
end


function moving(distance, angle)

	--as we noticed in the making squares project, at angular velocity =110 we get 90° turn, we used it to get other angles but deviding by 90
	if angle ~=0 then --the target is not at 0° of the robot, so adjust the robot accordingly
		ratio = angle/90
		forwardSpeed = distance * ratio
		angularSpeed = 110 * ratio
		leftV = forwardSpeed - angularSpeed
		rightV = forwardSpeed + angularSpeed
		
		robot.wheels.set_velocity(leftV,rightV)
	else
		--the target is directly in line of sight, move forward until distance is 30
		if distance < 30 then
			robot.wheels.set_velocity(0,0)
		else
			robot.wheels.set_velocity(25,25) --if you select higher speed values the robot with red led can't move a lot, so give it a chance to move then flank it
		end
	end
end

function step()
	--this is the same algorithm from avoiding obstacles project
		accum = { x=0, y=0 }
   		for i = 1,24 do
    		local vec = {
				x = robot.proximity[i].value * math.cos(robot.proximity[i].angle),
				y = robot.proximity[i].value * math.sin(robot.proximity[i].angle)
			}
    		accum.x = accum.x + vec.x
    		accum.y = accum.y + vec.y
		end
		angle = math.atan2(accum.y, accum.x)
		length = math.sqrt(accum.x*accum.x + accum.y*accum.y) / 24
		if (length < DELTA) then
	  		robot.wheels.set_velocity(50,50)
		else

			if #robot.colored_blob_omnidirectional_camera>0 then --if the robot detects a blob nearby
                blob = robot.colored_blob_omnidirectional_camera[1]
				distance = math.floor(blob.distance)
				lightAngle = math.floor(math.deg(blob.angle))
				moving(distance,lightAngle) --then the robot goes to that location
            else	--the robot detects no blobs nearby so it continues avoiding robots by moving the oposite side
	  			if angle > 0 then 
	     			robot.wheels.set_velocity(25,-10) --obstacle on the left, so turn to the right
      			else
	     			robot.wheels.set_velocity(-10,25) --obstacle on the right, so turn to left
      			end
			end
		end
	
end


function reset()
	init()
end


function destroy()
end
